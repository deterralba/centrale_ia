import numpy as np
from draw import start_GUI

RACE_ID = {
    'hum': 0,
    'vamp': 1,
    'wolv': 2,
}

SKIP_CHECKS = False

class ActionInvalidError(Exception):
    pass

class Board:
    def __init__(self, dimensions, initial_pop):
        shape = (dimensions[0], dimensions[1], 3)
        self.grid = np.zeros(shape, dtype=np.int32)
        self.update_grid(initial_pop)
        self.currentPlayer = None

    def update_grid(self, changed_squares):
        for square in changed_squares:
            x = square['x']
            y = square['y']
            # x, y server representation is not equal to our line column matrix model
            self.grid[y, x, RACE_ID['hum']] = square['hum']
            self.grid[y, x, RACE_ID['vamp']] = square['vamp']
            self.grid[y, x, RACE_ID['wolv']] = square['wolv']

    def moves(self, action):
        ''' Moves the units, do not resolve any fight'''
        if SKIP_CHECKS or action.is_valid(self):
            self.grid[action._from][RACE_ID[action.race]] -= action.number
            self.grid[action.to][RACE_ID[action.race]] += action.number
        else:
            raise ActionInvalidError('action not valid')

    def do_actions(self, actions):
        for action in actions:
            self.moves(action)
        self.resolve_grid(self)


class Action:
    def __init__(self, from_square, to_square, number, race):
        self._from = from_square
        self.to = to_square
        self.number = number
        self.race = race
        self.race_ennemi = 'wolv' if self.race == 'vamp' else 'vamp'

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
            self.race in 'LV',
            Action.square_is_on_grid(self.to, board.grid),
            Action.square_is_on_grid(self._from, board.grid) and \
                0 < self.number <= board.grid[self._from][RACE_ID[self.race]],
            not actions or self.to not in [ac._from for ac in actions]
        ])

if __name__ == '__main__':

    initial_pop = [{'x': 0, 'y': 0, 'hum': 0, 'vamp': 4, 'wolv': 0},
                   {'x': 1, 'y': 3, 'hum': 5, 'vamp': 0, 'wolv': 0},
                   {'x': 3, 'y': 1, 'hum': 3, 'vamp': 0, 'wolv': 0},
                   {'x': 4, 'y': 3, 'hum': 0, 'vamp': 0, 'wolv': 3}]

    test_board = Board((4,5), initial_pop)

    start_GUI(test_board.grid, lambda x=None: None)

    #a1 = Action((0,0), (0,1), 1, 'wolv')
    #a2 = Action((1,1), (1, 0), 2, 'wolv')
    #a3 = Action((1,1), (0,1), 2, 'wolv')
    #actions = [a1, a2]

    #print(b2.board_modification(actions))

