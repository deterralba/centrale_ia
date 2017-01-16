import numpy as np

RACE_ID = {
    'H': 0,
    'L': 1,
    'V': 2,
}

class Board:
    def __init__(self, dimensions):
        # line, column, race(humans, loup-garous, vampires)
        self.grid = np.zeros(dimensions, dtype=np.int32)
        self.currentPlayer = 0

    def play_action(self, departure_square, target_cible):
        return None

    def play_actions(self, actions):
        '''fonction qui prend en entree la grille + la square de depart + la square cible
         + le nombre de personnes a bouger et qui retourne la nouvelle grille'''
         # actions need to be grouped by their destination, so that several groups can attak the same square
        return None

class Action:
    def __init__(self, from_square, to_square, number, race):
        self._from = from_square
        self.to = to_square
        self.number = number
        self.race = race

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
    b = Board((2, 3)) # 2 lines & 3 columns
    b.grid = np.array([
        [[1, 2, 3], [3, 4, 6], [2, 7, 0]],
        [[5, 9, 5], [2, 1, 1], [4, 2, 1]]
    ], dtype=np.int32)
    print(b.grid)
    print(b.grid.shape)


