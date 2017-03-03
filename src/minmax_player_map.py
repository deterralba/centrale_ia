from player import Player
from algo_mini_max import minimax
from random import random
from threading import Thread, Lock
from algo_mini_max import max_play, min_play, SafeCounter, get_available_moves
from board import Board
from time import time

INF = 10e9

def f_maker(player, board, race, race_ennemi, depth, all_actions, counter):
    def f(action):
        counter.add_count()
        clone_board = board.copy()
        clone_board.current_player = race
        clone_board.do_actions([action])
        score = min_play(clone_board, race, race_ennemi, depth - 1, all_actions, counter)
        print('suggesting move ', score)
        return (action, score)
    return f

class MapPlayer(Player):

    def __init__(self, race, depth=3, nb_thread=4):
        super(MapPlayer, self).__init__(race)
        self.depth = depth
        self.nb_thread = nb_thread  # TODO update : not used
        self._best_move = None
        self._best_score = None
        self._lock = Lock()

    def get_next_move(self, board):
        print('%'*50)
        print(self.__class__.__name__)
        print('%'*50)
        self._best_move = None
        self._best_score = None

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

        #from multiprocessing import Pool
        from pathos.multiprocessing import ProcessingPool as Pool
        pool = Pool()

        f = f_maker(self, board, self.race, self.race_ennemi, self.depth, all_actions, counter)
        print(actions)
        result = pool.imap(f, actions)
        result = list(result)
        print('*' * 50)
        print(result)
        best_action, best_score = max(result, key=lambda x: x[1])
        print(best_action, best_score)
        print('.' * 40)

        pool.close()
        pool.join()
        del pool

        print(result)
        best_action, best_score = max(result, key=lambda x: x[1])
        print(best_action, best_score)
        self.set_best_move(best_action, best_score)

        print('+' * 40)
        print('action {}, score {}'.format(best_action, best_score))
        Board.SKIP_CHECKS = old_skip

        end_time = time() - start_time
        print('#position calc: {}, in {:.2f}s ({:.0f}/s)'.format(counter.get_count(), end_time, counter.get_count() / end_time))
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


if __name__ == '__main__':
    from const import RACE_ID, HUM, WOLV, VAMP

    p1 = ThreadMMPlayer(WOLV, depth=3, nb_thread=5)
    p1.get_next_move(None)
    print(p1.get_best_move())
    import time
    time.sleep(6)
    print(p1.get_best_move())
