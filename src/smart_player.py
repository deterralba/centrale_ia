from player import Player
from algo_mini_max import minimax
from algo_alpha_beta import alphabeta


class MiniMaxPlayer(Player):
    DEPTH = 3

    def get_next_move(self, board):
        return minimax(board, self.race, self.race_ennemi, self.DEPTH, self.transposition_table)


class AlphaBetaPlayer(Player):
    DEPTH = 3

    def get_next_move(self, board):
        return alphabeta(board, self.race, self.race_ennemi, self.DEPTH, self.transposition_table)
