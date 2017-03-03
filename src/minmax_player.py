from player import Player
from algo_mini_max import minimax
from random import random

from threading import Thread, Lock


class SmartPlayer(Player):
    def __init__(self, *args, depth=3):
        super().__init__(*args)
        self.depth = depth

    def get_next_move(self, board):
        return minimax(board, self.race, self.race_ennemi, self.depth)


class ThreadMMPlayer(Player):
    def __init__(self, *args, depth=3, nb_thread=4):
        super().__init__(*args)
        self.depth = depth
        self.nb_thread = nb_thread
        self._best_move = None
        self._lock = Lock()

    def get_next_move(self, board):
        self._best_move = None
        threads = []
        for i in range(self.nb_thread):
            thread = Thread(
                target=self.run,
                args=(i, self)
            )
            thread.start()
            threads.append(thread)

    def set_best_move(self, best_move):
        print('setting best move with ? ', best_move)
        if self._best_move is None or best_move > self._best_move:
            with self._lock:
                self._best_move = best_move
                print(self._best_move)

    def get_best_move(self):
        with self._lock:
            return self._best_move

    @staticmethod
    def run(thread_nb, player):
        print('hello', thread_nb)
        import time
        time.sleep(thread_nb*random())
        player.set_best_move(thread_nb**2)

        '''without group division and only one action
        old_skip = Board.SKIP_CHECKS
        Board.SKIP_CHECKS = True

        global nb_iterations
        nb_iterations = 0
        start_time = time()

        actions = get_available_moves(board, race)  # return a list of possible actions
        print('nb actions: {}'.format(len(actions)))
        best_action = actions[0]
        all_actions = []
        best_score = -INF
        for action in actions:
            add_count()
            clone_board = board.copy()
            clone_board.current_player = race
            clone_board.do_actions([action])
            score = min_play(clone_board, race, race_ennemi, depth-1, all_actions)
            if score > best_score:
                best_action = action
                best_score = score
        print('='*40)
        print('action {}, score {}'.format(best_action, best_score))
        Board.SKIP_CHECKS = old_skip

        if False:
            print('Action summary')
            all_actions.append((best_action, depth, best_score))
            all_actions.sort(key=lambda x: x[1], reverse=True)

            print('before filter', all_actions)
            print(best_score)
            all_actions = [action for action in all_actions if action[2] == best_score]
            print('after filter')
            print('\n'.join(map(str, all_actions)))

        end_time = time() - start_time
        print('#position calc: {}, in {:.2f}s ({:.0f}/s)'.format(nb_iterations, end_time, nb_iterations/end_time))
        return [best_action]  # return a list with only one move for the moment
        '''


if __name__ == '__main__':
    from const import RACE_ID, HUM, WOLV, VAMP

    global p1_best_move
    p1_best_move = float('-inf')
    p1 = ThreadMMPlayer(WOLV, depth=3, nb_thread=5)

    '''
    def p1_send_best_move(move):
        global  p1_best_move
        p1_best_move = max(move, p1_best_move)
        print('p1 send b m:', move)
    '''
    p1.get_next_move(None)
    print(p1.get_best_move())
    import time
    time.sleep(6)
    print(p1.get_best_move())

