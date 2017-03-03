from player import Player
from algo_mini_max import minimax

from threading import Thread


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

    def get_next_move(self, board, send_best_move=lambda move:None):
        threads = []
        for i in range(self.nb_thread):
            thread = Thread(target=self.run, args=(i, send_best_move))
            thread.start()
            threads.append(thread)

    @staticmethod
    def run(thread_nb, send_best_move):
        print('hello')
        import time
        time.sleep(thread_nb)
        send_best_move(thread_nb**2)


if __name__ == '__main__':
    from const import RACE_ID, HUM, WOLV, VAMP

    global p1_best_move
    p1_best_move = float('-inf')
    p1 = ThreadMMPlayer(WOLV, depth=3, nb_thread=5)

    def p1_send_best_move(move):
        global  p1_best_move
        p1_best_move = max(move, p1_best_move)
        print('p1 send b m:', move)

    p1.get_next_move(None, p1_send_best_move)
    print(p1_best_move)
    import time
    time.sleep(6)
    print(p1_best_move)

