from time import sleep, time
from draw import start_GUI, draw
from player import RamdomPlayer
from const import HUM, WOLV, VAMP
from board import Board


def generate_play(p1, p2, b):
    def play(*args):
        p = p1
        while not b.is_over():
            b.currentPlayer = p.race
            start_time = time()
            actions = p.get_next_move(b)
            if time() - start_time > 2:
                print('player {} timeout and looses!'.format(p))
                break
            b.do_actions(actions)
            draw(b.grid)
            sleep(0.1)
            p = p2 if p == p1 else p1
        print(b.is_over() + ' won!')
    return play


if __name__ == '__main__':

    initial_pop = [{'x': 0, 'y': 0, HUM: 0, VAMP: 4, WOLV: 0},
                   {'x': 1, 'y': 3, HUM: 5, VAMP: 0, WOLV: 0},
                   {'x': 3, 'y': 3, HUM: 0, VAMP: 0, WOLV: 1},
                   {'x': 3, 'y': 1, HUM: 3, VAMP: 0, WOLV: 0},
                   {'x': 4, 'y': 3, HUM: 0, VAMP: 0, WOLV: 3}]

    b = Board((4, 5), initial_pop)
    p1 = RamdomPlayer(VAMP)
    p2 = RamdomPlayer(WOLV)
    start_GUI(b.grid, generate_play(p1, p2, b))

    #a1 = Action((0,0), (0,1), 1, WOLV)
    #a2 = Action((1,1), (1, 0), 2, WOLV)
    #a3 = Action((1,1), (0,1), 2, WOLV)
    #actions = [a1, a2]

    #print(b2.board_modification(actions))
