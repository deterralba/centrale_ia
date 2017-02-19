from random import randint
from const import RACE_ID, HUM, WOLV, VAMP
from board import Action


class Player:
    def __init__(self, race, transposition_table):
        self.race = race
        self.race_ennemi = WOLV if self.race == VAMP else VAMP
        self.transposition_table = transposition_table

    def get_next_move(self, board):
        raise NotImplementedError()


class RandomPlayer(Player):
    def get_next_move(self, board):
        actions = []
        for square in board.enumerate_squares():
            units = board.grid[square][RACE_ID[self.race]]
            if units > 0:
                to = get_random_adjacent_square(board.grid, square)
                actions.append(Action(square, to, units, self.race))
        return actions


def get_random_adjacent_square(grid, square):
    not_on_grid = True
    to = None
    while not_on_grid or to == square:
        to = (square[0] + randint(-1, 1), square[1] + randint(-1, 1))
        not_on_grid = not Action.square_is_on_grid(to, grid)
    return to
