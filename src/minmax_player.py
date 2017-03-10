from player import Player
from algo_mini_max import minimax
from random import random
from threading import Thread, Lock
from algo_mini_max import SafeCounter, get_available_moves, _min_max
from board import Board
from time import time
from algo_alpha_beta import alphabeta

from game import INF


class SmartPlayer(Player):
    def __init__(self, race, depth=3):
        super(SmartPlayer, self).__init__(race)
        self.depth = depth
        self.transposition_table = {'depth': depth}

    def get_next_move(self, board):
        return minimax(board, self.race, self.race_ennemi, self.depth, self.transposition_table)


class SmartPlayerAlpha(SmartPlayer):
    def get_next_move(self, board):
        return alphabeta(board, self.race, self.race_ennemi, self.depth, self.transposition_table)


class ThreadMMPlayer(Player):
    def __init__(self, race, depth=3, nb_thread=4):
        super(ThreadMMPlayer, self).__init__(race)
        self.depth = depth
        self.nb_thread = nb_thread  # TODO update : not used
        self._best_move = None
        self._best_score = None
        self._lock = Lock()

    def get_next_move(self, board):
        #return minimax(board, self.race, self.race_ennemi, self.depth)
        self._best_move = None
        self._best_score = None
        threads = []

        old_skip = Board.SKIP_CHECKS
        Board.SKIP_CHECKS = True
        counter = SafeCounter()
        start_time = time()

        actions = get_available_moves(board, self.race)  # return a list of possible actions
        print('nb actions: {}'.format(len(actions)))
        print('nb positions: {}'.format(counter.get_count()))
        best_action = actions[0]
        all_actions = []
        best_score = -INF

        for i, action in enumerate(actions):
            # call the min_palyer for each actions
            thread = Thread(
                target=self.run,
                args=(i, self, board, self.race, self.race_ennemi, self.depth, action, all_actions, counter)
            )
            thread.start()
            threads.append(thread)

        for thread in threads:
            print('waiting for thread', thread)
            thread.join()

        print('+'*40)
        print('action {}, score {}'.format(best_action, best_score))
        Board.SKIP_CHECKS = old_skip

        end_time = time() - start_time
        print('#position calc: {}, in {:.2f}s ({:.0f}/s)'.format(counter.get_count(), end_time, counter.get_count()/end_time))
        return [self.get_best_move()]  # return a list with only one move for the moment

    def set_best_move(self, best_move, best_score):
        print('setting best move with ? ', best_move)
        if self._best_score is None or best_score > self._best_score:
            with self._lock:
                self._best_move = best_move
                self._best_score = best_score
                print(self._best_move, self._best_score)

    def get_best_move(self):
        with self._lock:
            return self._best_move

    @staticmethod
    def run(thread_nb, player, board, race, race_ennemi, depth, action, all_actions, counter):
        #def minimax(board, race, race_ennemi, depth):
        '''without group division and only one action'''
        counter.add_count()
        clone_board = board.copy()
        clone_board.current_player = race
        clone_board.do_actions([action])
        score = _min_max(False, clone_board, race, race_ennemi, depth-1, all_actions, counter)
        print('suggesting move ', score, thread_nb)
        player.set_best_move(action, score)


if __name__ == '__main__':
    from const import RACE_ID, HUM, WOLV, VAMP

    p1 = ThreadMMPlayer(WOLV, depth=3, nb_thread=5)
    p1.get_next_move(None)
    print(p1.get_best_move())
    import time
    time.sleep(6)
    print(p1.get_best_move())

