from random import random
import numpy as np
from draw import start_GUI, draw
from const import RACE_ID, HUM, WOLV, VAMP


class ActionInvalidError(Exception):
    pass


class Board:
    SKIP_CHECKS = False
    def __init__(self, dimensions, initial_pop=None, grid=None):
        shape = (dimensions[0], dimensions[1], 3)
        if grid is not None:
            self.grid = grid
        else:
            self.grid = np.zeros(shape, dtype=np.uint8)
        if initial_pop is not None:
            self.update_grid(initial_pop)
        self.current_player = None

    def copy(self):
        board = Board(self.grid.shape, grid=self.grid.copy())
        board.current_player = self.current_player
        return board

    def enumerate_squares(self):
        ''' Returns a generator iterating over the coordinates of the squares of the grid '''
        line, column, _ = self.grid.shape
        for i in range(line):
            for j in range(column):
                yield (i, j)

    def is_over(self):
        ''' Returns the winning race, or False if the game is not over '''
        sum_ = np.sum(self.grid, axis=(0, 1))
        nb_w = sum_[RACE_ID[WOLV]]
        nb_v = sum_[RACE_ID[VAMP]]
        if nb_w and nb_v:
            return False
        return VAMP*(bool(nb_v)) + WOLV*(bool(nb_w)) or HUM

    def update_grid(self, changed_squares):
        for square in changed_squares:
            x = square['x']
            y = square['y']
            # x, y server representation is not equal to our line column matrix model
            self.grid[y, x, RACE_ID[HUM]] = square[HUM]
            self.grid[y, x, RACE_ID[VAMP]] = square[VAMP]
            self.grid[y, x, RACE_ID[WOLV]] = square[WOLV]

    def calc_update(self, changed_squares):
        update = []
        for square in changed_squares:
            x = square[1]
            y = square[0]
            hum = self.grid[y, x, RACE_ID[HUM]]
            vamp = self.grid[y, x, RACE_ID[VAMP]]
            wolv = self.grid[y, x, RACE_ID[WOLV]]
            update.append({'x': x, 'y': y, HUM : hum, VAMP : vamp, WOLV : wolv})
        return update

    def moves(self, action):
        ''' Moves the units, does not resolve any fight'''
        if self.SKIP_CHECKS or action.is_valid(self):
            self.grid[action.from_][RACE_ID[action.race]] -= action.number
            self.grid[action.to][RACE_ID[action.race]] += action.number
        else:
            raise ActionInvalidError('action not valid: {}'.format(action))

    def do_actions(self, actions):
        if not self.SKIP_CHECKS:
            for square in self.enumerate_squares():
                nb_zeros = list(self.grid[square]).count(0)
                if nb_zeros < 2:
                    raise ValueError('Board is not consistent: several races in one square: {}: {}'.format(square, self.grid[square]))
        changed_squares = []
        for action in actions:
            changed_squares.append(action.from_)
            changed_squares.append(action.to)
            self.moves(action)
        for square in self.enumerate_squares():
            self.resolve_square(square)
        return self.calc_update(changed_squares)

    def resolve_square(self, square):
        nb_zeros = list(self.grid[square]).count(0)
        if nb_zeros >= 2:
            return
        elif nb_zeros == 0:
            print(self.grid)
            raise ValueError('impossible to resolve 3 races on one square')
        elif nb_zeros == 1:
            if self.grid[square][RACE_ID[HUM]] > 0:
                attack_humans(self.current_player, self.grid[square])
            else:
                attack_monsters(self.current_player, self.grid[square])


class Action:
    def __init__(self, from_square, to_square, number, race):
        self.from_ = from_square
        self.to = to_square
        self.number = number
        self.race = race
        self.race_ennemi = WOLV if self.race == VAMP else VAMP

    def __repr__(self):
        return '{} {} {} {}'.format(self.from_, self.to, self.number, self.race)

    @staticmethod
    def square_is_on_grid(square, grid):
        return all([
            0 <= square[0] < grid.shape[0], # line played <= number of lines
            0 <= square[1] < grid.shape[1], # column played <= number of columns
        ])

    def is_valid(self, board, actions=None):
        dif_x = abs(self.from_[0] - self.to[0])
        dif_y = abs(self.from_[1] - self.to[1])
        return all([
            dif_x <= 1,
            dif_y <= 1,
            self.from_ != self.to,
            self.race in [VAMP, WOLV],
            Action.square_is_on_grid(self.to, board.grid),
            Action.square_is_on_grid(self.from_, board.grid) and \
                0 < self.number <= board.grid[self.from_][RACE_ID[self.race]],
            not actions or self.to not in [ac.from_ for ac in actions]
        ])


def attack_humans(attacker, square):
    units = square[RACE_ID[attacker]]
    enemies = square[RACE_ID[HUM]]
    if units/enemies >= 1:
        units += enemies
        enemies = 0
    else:
        p = units / (2 * enemies)
        sort = random()
        if sort > p:
            units = 0
            temp_en = 0
            for i in range(enemies):
                lives = random()
                if lives> (1-p):
                    temp_en +=1
            enemies = int(temp_en)
        else:
            units += enemies
            temp_units = 0
            for i in range(units):
                lives = random()
                if lives > p :
                    temp_units +=1
            units = int(temp_units)
            enemies = 0
    square[RACE_ID[attacker]] = units
    square[RACE_ID[HUM]] = enemies


def attack_monsters(attacker, square):
    units = square[RACE_ID[attacker]]
    enemy_race = WOLV if attacker == VAMP else VAMP
    enemies = square[RACE_ID[enemy_race]]
    #print('Enemies : {} {}'.format(enemy_race, enemies))
    if units/enemies >= 1.5:
        enemies = 0
    else:
        if units >= enemies:
            p = units / enemies - 0.5
        else:
            p = units / (2 * enemies)
        sort = random()
        if sort > p:  # defeat of attacker
            units = 0
            temp_en = 0
            for i in range(units):
                lives = random()
                if lives > (1-p):
                    temp_en += 1
            enemies = int(temp_en)
        else:
            temp_unit = 0
            for i in range(units):
                lives = random()
                if lives > p:
                    temp_unit += 1
            units = int(temp_unit)
            enemies = 0
    square[RACE_ID[attacker]] = units
    square[RACE_ID[enemy_race]] = enemies
