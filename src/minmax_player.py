from player import Player
from algo_mini_max import minimax


class SmartPlayer(Player):
    DEPTH = 3

    def get_next_move(self, board):
        return minimax(board, self.race, self.race_ennemi, self.DEPTH)
