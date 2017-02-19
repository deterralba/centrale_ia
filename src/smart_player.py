from player import Player
from algo_mini_max import minimax


class MiniMaxPlayer(Player):
    DEPTH = 3

    def get_next_move(self, update):
        self.board.update_grid(update)
        print(self.board.grid)
        return minimax(self.board, self.race, self.race_ennemi, self.DEPTH, self.transposition_table)
