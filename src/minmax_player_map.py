from player import Player
from minmax_player import SmartPlayer
from algo_mini_max import minimax, clone_and_apply_actions
from random import random
from threading import Thread, Lock
from algo_mini_max import SafeCounter, get_available_moves, INF, _min_max
from board import Board
from time import time


def f(args):
    action, board, race, race_ennemi, depth, evaluate, esperance, all_actions = args
    playing_race = race
    counter = 0
    if esperance:
        clone_boards = clone_and_apply_actions(board, [action], playing_race, True)
        scores = []
        for clone_board in clone_boards:
            _, score, counter = _min_max(False, clone_board, race, race_ennemi, depth - 1, evaluate, esperance, all_actions, counter)
            scores.append(score*clone_board.proba)
        if len(scores) > 1:
            #print('calculated several clone_boards :', scores, sum([clone_board.proba for clone_board in clone_boards]))
            pass
        score = sum(scores)
    else:
        clone_board = clone_and_apply_actions(board, [action], playing_race, False)
        _, score, counter = _min_max(False, clone_board, race, race_ennemi, depth - 1, evaluate, esperance, all_actions, counter)

    #_, score, total_counter = _min_max(False, clone_board, race, race_ennemi, depth - 1, esperance, all_actions, 0)
    #player.set_best_move(action, score)
    #print('suggesting move ', score)
    #print('total counter', total_counter)
    return (action, score, counter)


class MapPlayer(SmartPlayer):

    def __init__(self, race, depth=3, esperance=True):
        super(MapPlayer, self).__init__(race, depth=depth, esperance=esperance)
        self._best_move = None
        self._best_score = None
        self._lock = Lock()

    def get_next_move(self, board):
        print('%' * 50)
        print(self.__class__.__name__)
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
            args.append((action, board, self.race, self.race_ennemi, self.depth, self.evaluate, self.esperance, all_actions))

        from multiprocessing import Pool
        #from pathos.multiprocessing import ProcessingPool as Pool
        #from multiprocess import Pool as Pool
        pool = Pool()
        # pool.ncpus = 8  # avoid error Pool not running, for a mystirious reason

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

    p1 = ThreadMMPlayer(WOLV, depth=3)
    p1.get_next_move(None)
    print(p1.get_best_move())
    import time
    time.sleep(6)
    print(p1.get_best_move())
