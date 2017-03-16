from random import random
import numpy as np
from const import RACE_ID, HUM, WOLV, VAMP

from game import RANDOM_MATCH_OUTPUT

activate_pop = False

class ActionInvalidError(Exception):
    pass


class Board:
    SKIP_CHECKS = False

    def __init__(self, dimensions, initial_pop=None, grid=None):
        self.pop = {}
        shape = (dimensions[0], dimensions[1], 3)
        if grid is not None:
            self.grid = grid
        else:
            self.grid = np.zeros(shape, dtype=np.uint8)
        if initial_pop is not None:
            self.update_grid(initial_pop)
        self.current_player = None
        self.proba = 1

    def copy(self):
        board = Board(self.grid.shape, grid=self.grid.copy())
        board.current_player = self.current_player
        board.proba = self.proba
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
        return VAMP * (bool(nb_v)) + WOLV * (bool(nb_w)) or HUM

    def update_grid(self, changed_squares):
        for square in changed_squares:
            x = square['x']
            y = square['y']
            humans = square[HUM]
            vampires = square[VAMP]
            wolves = square[WOLV]
            # x, y server representation is not equal to our line column matrix model
            self.grid[y, x, RACE_ID[HUM]] = humans
            self.grid[y, x, RACE_ID[VAMP]] = vampires
            self.grid[y, x, RACE_ID[WOLV]] = wolves

            if activate_pop:
                if humans > 0:
                    self.pop[(y, x)] = (HUM, humans)
                elif vampires > 0:
                    self.pop[(y, x)] = (VAMP, vampires)
                elif wolves > 0:
                    self.pop[(y, x)] = (WOLV, wolves)
                else:
                    del self.pop[(y, x)]

    def get_humans(self):
        return {new_key: self.pop[new_key][1] for new_key in self.pop.keys() if self.pop[new_key][0] == HUM}

    def get_vampires(self):
        return {new_key: self.pop[new_key][1] for new_key in self.pop.keys() if self.pop[new_key][0] == VAMP}

    def get_wolves(self):
        return {new_key: self.pop[new_key][1] for new_key in self.pop.keys() if self.pop[new_key][0] == WOLV}

    def moves(self, action):
        ''' Moves the units, does not resolve any fight'''
        if self.SKIP_CHECKS or action.is_valid(self):
            # print(action.number)
            self.grid[action.from_][RACE_ID[action.race]] -= action.number
            self.grid[action.to][RACE_ID[action.race]] += action.number
        else:
            print(self.grid)
            raise ActionInvalidError('action not valid: {}'.format(action))

    def do_actions(self, actions, simulation):
        self.proba = 1

        if not self.SKIP_CHECKS:
            for square in self.enumerate_squares():
                # TODO use np.count_nonzero
                nb_zeros = list(self.grid[square]).count(0)
                if nb_zeros < 2:
                    raise ValueError(
                        'Board is not consistent: several races in one square: {}: {}'.format(
                            square, self.grid[square]))

        changed_squares = []
        for action in actions:
            changed_squares.append(action.from_)
            changed_squares.append(action.to)
            self.moves(action)

        if simulation:
            boards = [self]
            for square in changed_squares:
                outcomes = get_outcomes(self, square)  # returns a list of results, proba : {'result':[0,2,0], 'proba':p}
                boards = resolve_square_with_proba(boards, outcomes, square)  # applies to squares and duplicates boards if needed
            return boards
        else:
            for square in changed_squares:
                resolve_square(self, square)
            return self


def resolve_square(board, square):
    # nb_zeros = list(board.grid[square]).count(0)
    nb_zeros = np.sum(board.grid[square] == 0)
    if nb_zeros == 1:
        if board.grid[square][RACE_ID[HUM]] > 0:
            attack_humans(board.current_player, board.grid[square])
        else:
            attack_monsters(board.current_player, board.grid[square])
    elif nb_zeros >= 2:
        return
    elif nb_zeros == 0:
        print(board.grid)
        raise ValueError('impossible to resolve 3 races on one square')


def apply_outcome(board, outcome, square):
    board.grid[square] = outcome['result']
    board.proba *= outcome['proba']


def resolve_square_with_proba(boards, outcomes, square):
    original_proba = boards[0].proba
    for board in boards[:]:
        apply_outcome(board, outcomes[0], square)
        for outcome in outcomes[1:]:
            new_board = board.copy()
            new_board.proba = original_proba
            apply_outcome(new_board, outcome, square)
            boards.append(new_board)
    return boards


def get_outcomes(board, square):
    # nb_zeros = list(board.grid[square]).count(0)
    # nb_zeros = np.count_nonzero(board.grid[square]) # TODO update code to make this works
    nb_zeros = np.sum(board.grid[square] == 0)
    if nb_zeros >= 2:
        return [{'proba': 1, 'result': board.grid[square]}]
    elif nb_zeros == 0:
        print(board.grid)
        raise ValueError('impossible to resolve 3 races on one square')
    elif nb_zeros == 1:
        if board.grid[square][RACE_ID[HUM]] > 0:
            return attack_humans_with_proba(board.current_player, board.grid[square])
        else:
            return attack_monsters_with_proba(board.current_player, board.grid[square])


class Action:

    def __init__(self, from_square, to_square, number, race):
        self.from_ = from_square
        self.to = to_square
        self.number = number
        self.race = race
        self.race_ennemi = WOLV if self.race == VAMP else VAMP

    def __repr__(self):
        return '{}: {}->{} w {}'.format(self.race, self.from_, self.to, self.number)

    @staticmethod
    def square_is_on_grid(square, grid):
        return all([
            0 <= square[0] < grid.shape[0],  # line played <= number of lines
            0 <= square[1] < grid.shape[1],  # column played <= number of columns
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
            Action.square_is_on_grid(self.from_, board.grid) and
            0 < self.number <= board.grid[self.from_][RACE_ID[self.race]],
            not actions or self.to not in [ac.from_ for ac in actions]
        ])

    def format(self):
        return [self.from_[1], self.from_[0], self.number, self.to[1], self.to[0]]


def attack_humans(attacker, square):
    units = square[RACE_ID[attacker]]
    enemies = square[RACE_ID[HUM]]
    if units / enemies >= 1:
        units += enemies
        enemies = 0
    else:
        p = units / (2 * enemies)
        if RANDOM_MATCH_OUTPUT:
            sort = random()
        else:
            sort = 0.5
        if sort > p:
            units = 0
            enemies = int(enemies * (1 - p))
        else:
            units += enemies
            units = int(p * units)
            enemies = 0
    square[RACE_ID[attacker]] = units
    square[RACE_ID[HUM]] = enemies


def attack_monsters(attacker, square):
    units = square[RACE_ID[attacker]]
    enemy_race = WOLV if attacker == VAMP else VAMP
    enemies = square[RACE_ID[enemy_race]]
    # print('Enemies : {} {}'.format(enemy_race, enemies))
    if units / enemies >= 1.5:
        enemies = 0
    else:
        if units >= enemies:
            p = units / enemies - 0.5
        else:
            p = units / (2 * enemies)
        if RANDOM_MATCH_OUTPUT:
            sort = random()
        else:
            sort = 0.5
        if sort > p:  # defeat of attacker
            units = 0
            enemies = int(enemies * (1 - p))
        else:
            units = int(p * units)
            enemies = 0
    square[RACE_ID[attacker]] = units
    square[RACE_ID[enemy_race]] = enemies


def attack_humans_with_proba(attacker, square):
    units = square[RACE_ID[attacker]]
    enemy_race = HUM
    enemies = square[RACE_ID[enemy_race]]
    if units / enemies >= 1:
        square_win = square.copy()
        square_win[RACE_ID[attacker]] += enemies
        square_win[RACE_ID[enemy_race]] = 0
        return [{'proba': 1, 'result': square_win}]
    else:
        p = units / (2 * enemies)

        square_win = square.copy()
        square_win[RACE_ID[attacker]] = int(p * (enemies + units))
        square_win[RACE_ID[enemy_race]] = 0

        square_lose = square.copy()
        square_lose[RACE_ID[attacker]] = 0
        square_lose[RACE_ID[enemy_race]] = int(enemies * (1 - p))

        return [
            {'proba': p, 'result': square_win},
            {'proba': 1 - p, 'result': square_lose},
        ]


def attack_monsters_with_proba(attacker, square):
    units = square[RACE_ID[attacker]]
    enemy_race = WOLV if attacker == VAMP else VAMP
    enemies = square[RACE_ID[enemy_race]]
    #print('Enemies : {} {}'.format(enemy_race, enemies))
    if units / enemies >= 1.5:
        square_win = square.copy()
        square_win[RACE_ID[enemy_race]] = 0
        return [{'proba': 1, 'result': square_win}]
    else:
        if units >= enemies:
            p = units / enemies - 0.5
        else:
            p = units / (2 * enemies)

        square_win = square.copy()
        square_win[RACE_ID[attacker]] = int(p * units)
        square_win[RACE_ID[enemy_race]] = 0

        square_lose = square.copy()
        square_lose[RACE_ID[attacker]] = 0
        square_lose[RACE_ID[enemy_race]] = int(enemies * (1 - p))

        return [
            {'proba': p, 'result': square_win},
            {'proba': 1 - p, 'result': square_lose},
        ]
