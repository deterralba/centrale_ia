from draw import start_GUI, draw
from player import RamdomPlayer
from const import RACE_ID, HUM, WOLV, VAMP
from board import Board


def play(*args):
    global p1, p2, b
    p = p1
    while not b.is_over():
        b.currentPlayer = p.race
        actions = p.get_next_move(b)
        print(actions)
        b.do_actions(actions)
        draw(b.grid)
        from time import sleep
        sleep(0.1)
        p = p2 if p == p1 else p1
    print(b.is_over() + 'won !')


if __name__ == '__main__':

    initial_pop = [{'x': 0, 'y': 0, HUM: 0, VAMP: 4, WOLV: 0},
                   {'x': 1, 'y': 3, HUM: 5, VAMP: 0, WOLV: 0},
                   {'x': 3, 'y': 3, HUM: 0, VAMP: 0, WOLV: 1},
                   {'x': 3, 'y': 1, HUM: 3, VAMP: 0, WOLV: 0},
                   {'x': 4, 'y': 3, HUM: 0, VAMP: 0, WOLV: 3}]

    global p1, p2, b
    b = Board((4,5), initial_pop)
    p1 = RamdomPlayer(VAMP)
    p2 = RamdomPlayer(WOLV)
    start_GUI(b.grid, play)

    #a1 = Action((0,0), (0,1), 1, WOLV)
    #a2 = Action((1,1), (1, 0), 2, WOLV)
    #a3 = Action((1,1), (0,1), 2, WOLV)
    #actions = [a1, a2]

    #print(b2.board_modification(actions))

