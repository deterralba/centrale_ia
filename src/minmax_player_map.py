from player import Player
from algo_mini_max import minimax
from random import random
from threading import Thread, Lock
from algo_mini_max import SafeCounter, get_available_moves, INF, _min_max
from board import Board
from time import time


def f(args):
    action, board, race, race_ennemi, depth, all_actions = args
    counter = SafeCounter()
    counter.add_count()
    clone_board = board.copy()
    clone_board.current_player = race
    clone_board.do_actions([action])
    score = _min_max(False, clone_board, race, race_ennemi, depth - 1, all_actions, counter)
    #player.set_best_move(action, score)
    #print('suggesting move ', score)
    return (action, score, counter.get_count())


class MapPlayer(Player):

    def __init__(self, race, depth=3, nb_thread=4):
        super(MapPlayer, self).__init__(race)
        self.depth = depth
        self.nb_thread = nb_thread  # TODO update : not used
        self._best_move = None
        self._best_score = None
        self._lock = Lock()

    def get_next_move(self, board):
        print('%' * 50)
        print(self.__class__.__name__)
        print('%' * 50)
        self._best_move = None
        self._best_score = None

        old_skip = Board.SKIP_CHECKS
        Board.SKIP_CHECKS = True
        start_time = time()
        counter = 0

        actions = get_available_moves(board, self.race)  # return a list of possible actions
        print('nb actions: {}'.format(len(actions)))
        print('nb positions: {}'.format(counter))
        best_action = actions[0]
        all_actions = []
        best_score = -INF

        args = []
        for action in actions:
            args.append((action, board, self.race, self.race_ennemi, self.depth, all_actions))

        from multiprocessing import Pool
        #from pathos.multiprocessing import ProcessingPool as Pool
        #from multiprocess import Pool as Pool
        pool = Pool()
        #pool.ncpus = 8  # avoid error Pool not running, for a mystirious reason

        result = pool.map(f, args)
        #result = list(result)
        print('*' * 50)
        # print(result)

        pool.close()
        pool.join()

        # print(result)
        best_action, best_score, _ = max(result, key=lambda x: x[1])
        #print(best_action, best_score)
        self.set_best_move(best_action, best_score)

        for tup in result:
            counter += tup[2]

        print('+' * 40)
        print('action {}, score {}'.format(best_action, best_score))
        Board.SKIP_CHECKS = old_skip

        end_time = time() - start_time
        print('#position calc: {}, in {:.2f}s ({:.0f}/s)'.format(counter, end_time, counter / end_time))
        return [self.get_best_move()]  # return a list with only one move for the moment

    def set_best_move(self, best_move, best_score):
        #print('setting best move with ? ', best_move)
        if self._best_score is None or best_score > self._best_score:
            with self._lock:
                self._best_move = best_move
                self._best_score = best_score
                print('best_move is now', self._best_move, self._best_score)

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
