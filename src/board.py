import numpy as np

RACE_ID = {
    'H': 0,
    'L': 1,
    'V': 2,
}

class Board:
    def __init__(self, dimensions):
        # line, columne, race(humans, loup-garous, vampires)
        self.grid = np.zeros(dimensions, dtype=np.int32)
        self.currentPlayer = 0

    def play_action(self, departure_case, target_cible):
        '''fonction qui prend en entrée la grille + la case de départ + la case cible
         + le nombre de personnes à bouger et qui retourne la nouvelle grille'''
        return None

    def play_actions(self, actions):
        '''fonction qui prend en entrée la grille + la case de départ + la case cible
         + le nombre de personnes à bouger et qui retourne la nouvelle grille'''
        return None

class Action:
    def __init__(self, from_case, to_case, number, race):
        self._from = from_case
        self._to = to_case
        self._number = number
        self._race = race

    @staticmethod
    def square_on_grid(square, grid):
        return all([
            0 <= square[0] < grid.shape[0],
            0 <= square[1] < grid.shape[1],
        ])

    def is_valid(self, board):
        dif_x = abs(self._from[0] - self._to[0])
        dif_y = abs(self._from[1] - self._to[1])
        return all([
            dif_x <= 1,
            dif_y <= 1,
            self._from != self._to,
            self._race != 'H',
            Action.square_on_grid(self._to, board.grid),
            Action.square_on_grid(self._from, board.grid) and 0 < self._number <= board.grid[self._from][RACE_ID[self._race]],
        ])

if __name__ == '__main__':
    b = Board((2, 2))
    b.grid = np.array([
        [[1, 2, 3], [3, 4, 6]],
        [[5, 9, 5], [2, 1, 1]]
    ], dtype=np.int32)


