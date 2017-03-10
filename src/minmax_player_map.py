from player import Player
from algo_mini_max import minimax
from algo_alpha_beta import _alpha_beta
from random import random
from threading import Thread, Lock
from algo_mini_max import SafeCounter, get_available_moves, INF, _min_max
from board import Board
from time import time


def alphabeta_f(args):
    action, board, race, race_ennemi, depth, all_actions = args
    clone_board = board.copy()
    clone_board.current_player = race
    clone_board.do_actions([action])
    alpha = -INF
    beta = INF
    _, score, total_counter = _alpha_beta(False, clone_board, race, race_ennemi, depth - 1, all_actions, 0, alpha, beta)
    return (action, score, total_counter)


def minmax_f(args):
    action, board, race, race_ennemi, depth, all_actions = args
    clone_board = board.copy()
    clone_board.current_player = race
    clone_board.do_actions([action])
    _, score, total_counter = _min_max(False, clone_board, race, race_ennemi, depth - 1, all_actions, 0)
    #player.set_best_move(action, score)
    #print('suggesting move ', score)
    #print('total counter', total_counter)
    return (action, score, total_counter)


class MapPlayer(Player):

    def __init__(self, race, depth=3, type='minmax'):
        assert type in ['minmax', 'alphabeta']
        super(MapPlayer, self).__init__(race)
        self.depth = depth
        self.type = type
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
        # pool.ncpus = 8  # avoid error Pool not running, for a mystirious reason

        if self.type == 'minmax':
            result = pool.map(minmax_f, args)
        elif self.type == 'alphabeta':
            result = pool.map(alphabeta_f, args)

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

