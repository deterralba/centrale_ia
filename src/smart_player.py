from player import Player
from algo_mini_max import minimax


class MiniMaxPlayer(Player):
    DEPTH = 2

    def get_next_move(self, board):
        return minimax(board, self.race, self.race_ennemi, self.DEPTH)
