from player import Player
from algo_mini_max import minimax


class SmartPlayer(Player):
    def get_next_move(self, board):
        return minimax(board, self.race, self.race_ennemi, 1)
