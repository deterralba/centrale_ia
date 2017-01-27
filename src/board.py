from random import random
import numpy as np
from draw import start_GUI, draw
from const import RACE_ID, HUM, WOLV, VAMP

SKIP_CHECKS = False

class ActionInvalidError(Exception):
    pass

class Board:
    def __init__(self, dimensions, initial_pop):
        shape = (dimensions[0], dimensions[1], 3)
        self.grid = np.zeros(shape, dtype=np.int32)
        self.update_grid(initial_pop)
        self.currentPlayer = None

    def enumerate_squares(self):
        line, column, _ = self.grid.shape
        for i in range(line):
            for j in range(column):
                yield (i, j)

    def is_over(self):
        nb_w = 0
        nb_v = 0
        for square in self.enumerate_squares():
            nb_v += self.grid[square][RACE_ID[VAMP]]
            nb_w += self.grid[square][RACE_ID[WOLV]]
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

    def moves(self, action):
        ''' Moves the units, does not resolve any fight'''
        if SKIP_CHECKS or action.is_valid(self):
            self.grid[action._from][RACE_ID[action.race]] -= action.number
            self.grid[action.to][RACE_ID[action.race]] += action.number
        else:
            raise ActionInvalidError('action not valid: {}'.format(action))

    def do_actions(self, actions):
        if not SKIP_CHECKS:
            for square in self.enumerate_squares():
                nb_zeros = list(self.grid[square]).count(0)
                if nb_zeros < 2:
                    raise ValueError('Board is not consistant: several races in one square: {}: {}'.format(square, self.grid[square]))
        for action in actions:
            self.moves(action)
        for square in self.enumerate_squares():
            self.resolve_square(square)

    def resolve_square(self, square):
        nb_zeros = list(self.grid[square]).count(0)
        if nb_zeros >= 2:
            return
        elif nb_zeros == 0:
            raise ValueError('impossible to resolve 3 races on one square')
        elif nb_zeros == 1:
            if self.grid[square][RACE_ID[HUM]] > 0:
                attack_humans(self.currentPlayer, self.grid[square])
            else:
                attack_monsters(self.currentPlayer, self.grid[square])

class Action:
    def __init__(self, from_square, to_square, number, race):
        self._from = from_square
        self.to = to_square
        self.number = number
        self.race = race
        self.race_ennemi = WOLV if self.race == VAMP else VAMP

    def __repr__(self):
        return '{} {} {} {}'.format(self._from, self.to, self.number, self.race)

    @staticmethod
    def square_is_on_grid(square, grid):
        return all([
            0 <= square[0] < grid.shape[0], # line played <= number of lines
            0 <= square[1] < grid.shape[1], # column played <= number of columns
        ])

    def is_valid(self, board, actions=None):
        dif_x = abs(self._from[0] - self.to[0])
        dif_y = abs(self._from[1] - self.to[1])
        return all([
            dif_x <= 1,
            dif_y <= 1,
            self._from != self.to,
            self.race in [VAMP, WOLV],
            Action.square_is_on_grid(self.to, board.grid),
            Action.square_is_on_grid(self._from, board.grid) and \
                0 < self.number <= board.grid[self._from][RACE_ID[self.race]],
            not actions or self.to not in [ac._from for ac in actions]
        ])

def attack_humans(attacker, square, probabilistic=False):
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
            enemies = int(enemies * (1-p))
        else:
            units += enemies
            units = int(p*units)
            enemies = 0
    square[RACE_ID[attacker]] = units
    square[RACE_ID[HUM]] = enemies

def attack_monsters(attacker, square, probabilistic=False):
    units = square[RACE_ID[attacker]]
    enemy_race = WOLV if attacker == VAMP else VAMP
    enemies = square[RACE_ID[enemy_race]]
    print('Enemies : {} {}'.format(enemy_race, enemies))
    if units/enemies >= 1.5:
        enemies = 0
    else:
        #si victoire (proba p) : chaque attaquant a une proba (p) de survivre
        #                        chaque humain a une proba (p) de devenir allié
        #si défaite (1-p) : aucun survivant coté attaquant
        #                   chaque humain a une proba (1-p) de survivre
        if units >= enemies:
            p = units / enemies - 0.5
        else:
            p = units / (2 * enemies)
        sort = random()
        if sort > p:  # defeat of attacker
            units = 0
            enemies = int(enemies * (1-p))
        else:
            units = int(p*units)
            enemies = 0
    square[RACE_ID[attacker]] = units
    square[RACE_ID[enemy_race]] = enemies
