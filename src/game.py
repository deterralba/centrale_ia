from time import sleep, time
from draw import start_GUI, draw
from player import RamdomPlayer
from const import HUM, WOLV, VAMP
from board import Board


def generate_play(player1, player2, board):
    def play(*args):
        current_player = player1
        while not board.is_over():
            board.currentPlayer = current_player.race
            start_time = time()
            actions = current_player.get_next_move(board)
            sleep(0.5)
            if time() - start_time > 2:
                print('player {} timeout and looses!'.format(current_player))
                break
            board.do_actions(actions)
            draw(board.grid)
            sleep(0.5)
            current_player = player2 if current_player == player1 else player1
        print(board.is_over() + ' won!')
    return play


if __name__ == '__main__':

    initial_pop = [{'x': 0, 'y': 0, HUM: 0, VAMP: 4, WOLV: 0},
                   {'x': 1, 'y': 3, HUM: 5, VAMP: 0, WOLV: 0},
                   {'x': 3, 'y': 3, HUM: 0, VAMP: 0, WOLV: 1},
                   {'x': 3, 'y': 1, HUM: 3, VAMP: 0, WOLV: 0},
                   {'x': 4, 'y': 3, HUM: 0, VAMP: 0, WOLV: 3}]

    board = Board((4, 5), initial_pop)
    player1 = RamdomPlayer(VAMP)
    player2 = RamdomPlayer(WOLV)
    start_GUI(board.grid, generate_play(player1, player2, board))
