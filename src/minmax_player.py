from player import Player
from algo_mini_max import minimax
from threading import Thread, Lock
from algo_mini_max import SafeCounter, get_available_moves, _min_max
from algo_alpha_beta import alphabeta
from board import Board
from time import time
from game import INF
from threading import Thread
from containers import ContainerBool
from evaluation import evaluate_inf, evaluate_disp, evaluate_fred


class SmartPlayer(Player):

    def __init__(self, race, depth=3, esperance=False, evaluate=None):
        assert evaluate is not None

        super(SmartPlayer, self).__init__(race)
        self.depth = depth
        self.esperance = esperance
        self.transposition_table = {'depth': depth}
        self.evaluate = evaluate

    def get_next_move(self, board):
        return minimax(board, self.race, self.race_ennemi, self.depth, self.evaluate, self.esperance, self.transposition_table)

    def start_search(self, board, actions_container):
        self.threads_containers = []
        for depth in range(1, self.depth + 1):
            should_continue_container = ContainerBool(True)
            thread = Thread(
                target=self.run,
                args=(actions_container, should_continue_container, board, self.race, self.race_ennemi, depth, self.evaluate, self.esperance)
            )
            thread.start()
            self.threads_containers.append(should_continue_container)

    @staticmethod
    def run(actions_container, should_continue_container, board, race, race_ennemi, depth, evaluate, esperance):
        actions, score = minimax(board, race, race_ennemi, depth, evaluate, esperance, with_score=True)
        if should_continue_container.get():
            print('\nsetting action {} for depth {} and score {}'.format(actions, depth, score))
            actions_container.smart_set(actions, depth, score)


class SmartPlayerAlpha(SmartPlayer):
    def get_next_move(self, board):
        return alphabeta(board, self.race, self.race_ennemi, self.depth, self.evaluate, self.esperance, self.transposition_table)

    @staticmethod
    def run(actions_container, should_continue_container, board, race, race_ennemi, depth, evaluate, esperance):
        actions, score = alphabeta(board, race, race_ennemi, depth, evaluate, esperance, with_score=True)
        if should_continue_container.get():
            print('\nsetting action {} for depth {} and score {}'.format(actions, depth, score))
            actions_container.smart_set(actions, depth, score)


class ThreadMMPlayer(Player):
    '''USELESS: 0 gain in speed because of the GIL'''

    def __init__(self, race, depth=3, nb_thread=4):
        raise ValueError('DO NOT USE ME, I AM USELESS')
        super(ThreadMMPlayer, self).__init__(race)
        self.depth = depth
        self.nb_thread = nb_thread  # TODO update : not used
        self._best_move = None
        self._best_score = None
        self._lock = Lock()

    def get_next_move(self, board):
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

    @staticmethod
    def run(thread_nb, player, board, race, race_ennemi, depth, action, all_actions, counter):
        counter.add_count()
        clone_board = board.copy()
        clone_board.current_player = race
        clone_board.do_actions([action])
        score = _min_max(False, clone_board, race, race_ennemi, depth - 1, all_actions, counter)
        print('suggesting move ', score, thread_nb)
        player.set_best_move(action, score)


if __name__ == '__main__':
    from const import WOLV

    p1 = ThreadMMPlayer(WOLV, depth=3, nb_thread=5)
    p1.get_next_move(None)
    print(p1.get_best_move())
    time.sleep(6)
    print(p1.get_best_move())
