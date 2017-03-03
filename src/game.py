from time import sleep, time
from draw import start_GUI, draw
from player import RamdomPlayer
from alphabeta_player import SmartPlayer
from const import HUM, WOLV, VAMP
from board import Board
from alphabeta import successors
from algo_mini_max import evaluate

def generate_play(player1, player2, board):
    def play(*args):
        current_player = player1
        while not board.is_over():
            board.current_player = current_player.race
            start_time = time()
            actions = current_player.get_next_move(board)
            if time() - start_time > 2:
                print('player {} timeout and looses!'.format(current_player))
                #break # FIXME
            print('action of {} are {}'.format(board.current_player, actions))
            board.do_actions(actions)
            draw(board.grid)
            #sleep(0.2)
            #pause = input()
            current_player = player2 if current_player == player1 else player1
        print(board.is_over() + ' won!')
    return play


if __name__ == '__main__':

    initial_pop = [{'x': 4, 'y': 2, HUM: 0, VAMP: 4, WOLV: 0},
                   {'x': 1, 'y': 3, HUM: 5, VAMP: 0, WOLV: 0},
                   {'x': 3, 'y': 3, HUM: 0, VAMP: 0, WOLV: 1},
                   {'x': 3, 'y': 1, HUM: 3, VAMP: 0, WOLV: 0},
                   {'x': 4, 'y': 3, HUM: 0, VAMP: 0, WOLV: 3}]
    
    board = Board((4, 5), initial_pop)

    i = 0
    for a,s in successors(board, VAMP):
        i += 1
        j = 0
        for b,t in successors(s, WOLV):
            j += 1
            print(i, "-", j, ":", evaluate(t,VAMP,WOLV))
'''
    SmartPlayer.DEPTH = 4
    player1 = SmartPlayer(VAMP)
    player2 = SmartPlayer(WOLV)
    #player2 = RamdomPlayer(WOLV)
    start_GUI(board.grid, generate_play(player1, player2, board))'''
