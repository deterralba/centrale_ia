from client import ComServer
from board import Board
from minmax_player_map import MapPlayer
from player import RandomPlayer
from const import HUM, WOLV, VAMP
from time import sleep
from evaluation import evaluate_inf, evaluate_disp, evaluate_fred
from minmax_player import SmartPlayer, ThreadMMPlayer, SmartPlayerAlpha

if __name__ == '__main__':
    #Parameters
    host = 'localhost'
    port = 5555

    name = 'JACK'

    time_to_play = 2
    stop = 0.9       #proportion du time_to_play auquel on arrête


    #Start communication with the server
    com = ComServer(host, port)
    com.connect_with_server()

    com.send_name(name)

    #receive first data
    set = com.get_set()
    hum = com.get_hum()
    hme = com.get_hme()
    map = com.get_map()

    board = Board(set, map)
    race = board.grid[hme[1], hme[0]]

    if race[1] !=0:
        race = VAMP
    else:
        race = WOLV

    #player1 = MapPlayer(race, depth=3)
    #player1 = RandomPlayer(race)
    player1 = SmartPlayerAlpha(VAMP, depth=3, esperance=True, evaluate=evaluate_inf)

    while True:
        msg = com.listen()
        if msg == 'UPD':
            print('UPD')
            upd = com.get_upd()
            board.update_grid(upd)
            actions = player1.get_next_move(board)
            actions = [action.format() for action in actions]
            print(actions)
            com.send_mov(actions)
        elif msg == 'END':
            print('end of the game')
            com.close_connexion()
            break
        elif msg == 'BYE':
            com.close_connexion()
            break
