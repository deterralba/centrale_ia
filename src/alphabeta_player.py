from player import Player
from alphabeta import alphabeta


class SmartPlayer(Player):
    DEPTH = 3

    def get_next_move(self, board):
        return alphabeta(board, self.race, self.race_ennemi, self.DEPTH)
