from client import ComServer
from board import Board
from minmax_player_map import MapPlayer
from player import RandomPlayer
from time import sleep, time
from containers import ContainerList
from minmax_player import SmartPlayer, SmartPlayerAlpha
from const import HUM, WOLV, VAMP, simple_pop_size, simple_pop, real_pop, real_pop_size
from evaluation import evaluate_inf, evaluate_disp, evaluate_fred



name = 'JACK'
time_to_play = 2
stop = 0.95  # proportion du time_to_play auquel on arrête

# Parameters
host = 'localhost'
port = 5555


if __name__ == '__main__':
    # Start communication with the server
    com = ComServer(host, port)
    com.connect_with_server()

    com.send_name(name)

    # receive first data
    set = com.get_set()
    hum = com.get_hum()
    hme = com.get_hme()
    map = com.get_map()

    board = Board(set, map)
    race = board.grid[hme[1], hme[0]]

    if race[1] != 0:
        race = VAMP
    else:
        race = WOLV

    #player1 = MapPlayer(race, depth=3)
    #player1 = SmartPlayerAlpha(VAMP, depth=7, esperance=True, evaluate=evaluate_inf)
    #player1 = RandomPlayer(race)
    player1 = SmartPlayer(VAMP, depth=4, esperance=False, evaluate=evaluate_fred)

    while True:
        msg = com.listen()
        start_time = time()
        if msg == 'UPD':
            print('UPD')
            upd = com.get_upd()
            board.update_grid(upd)

            actions_container = ContainerList()
            player1.start_search(board, actions_container)

            sleep(1.2)
            while time() - start_time < time_to_play * stop:
                sleep(0.05)

            print('stoping search after {:.2f}s'.format(time() - start_time))

            actions = actions_container.get()
            actions = [action.format() for action in actions]
            com.send_mov(actions)
            player1.stop_search()
            print(actions)
        elif msg == 'END':
            print('end of the game')
            com.close_connexion()
            break
        elif msg == 'BYE':
            com.close_connexion()
            break
