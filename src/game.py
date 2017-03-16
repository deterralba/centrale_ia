
# Parameters
TRANSPOSITION = False
RANDOM_MATCH_OUTPUT = False
INF = 10e9


def generate_play(player1, player2, board, draw=lambda x: None):
    def play(*args):
        initial_start_time = time()
        current_player = player1
        while not board.is_over():
            board.current_player = current_player.race
            start_time = time()
            actions = current_player.get_next_move(board)
            if time() - start_time > 2:
                print('player {} timeout and looses!'.format(current_player))
                # break # FIXME
            print('action of {} are {}'.format(board.current_player, actions))
            board.do_actions(actions)
            draw(board.grid)
            # sleep(0.2)
            current_player = player2 if current_player == player1 else player1
            #input('waiting')
        print(board.is_over() + ' won!')
        print('lasted {:.2f}s'.format(time() - initial_start_time))
    return play


if __name__ == '__main__':
    from time import sleep, time
    from player import RandomPlayer
    from minmax_player import SmartPlayer, ThreadMMPlayer, SmartPlayerAlpha
    from minmax_player_map import MapPlayer
    from const import HUM, WOLV, VAMP
    from board import Board

    initial_pop = [{'x': 0, 'y': 0, HUM: 0, VAMP: 4, WOLV: 0},
                   {'x': 1, 'y': 3, HUM: 5, VAMP: 0, WOLV: 0},
                   {'x': 3, 'y': 3, HUM: 0, VAMP: 0, WOLV: 1},
                   {'x': 3, 'y': 1, HUM: 3, VAMP: 0, WOLV: 0},
                   {'x': 4, 'y': 3, HUM: 0, VAMP: 0, WOLV: 3}]

    initial_pop2 = [{'x': 0, 'y': 0, HUM: 0, VAMP: 0, WOLV: 5},
                    {'x': 1, 'y': 1, HUM: 1, VAMP: 0, WOLV: 0},
                    {'x': 1, 'y': 3, HUM: 1, VAMP: 0, WOLV: 0},
                    {'x': 2, 'y': 2, HUM: 9, VAMP: 0, WOLV: 0},
                    {'x': 1, 'y': 1, HUM: 1, VAMP: 0, WOLV: 0},
                    {'x': 3, 'y': 1, HUM: 1, VAMP: 0, WOLV: 0},
                    {'x': 3, 'y': 3, HUM: 1, VAMP: 0, WOLV: 0},
                    {'x': 3, 'y': 5, HUM: 2, VAMP: 0, WOLV: 0},
                    {'x': 4, 'y': 5, HUM: 2, VAMP: 0, WOLV: 0},
                    {'x': 5, 'y': 3, HUM: 2, VAMP: 0, WOLV: 0},
                    {'x': 5, 'y': 4, HUM: 2, VAMP: 0, WOLV: 0},
                    {'x': 5, 'y': 6, HUM: 2, VAMP: 0, WOLV: 0},
                    {'x': 5, 'y': 7, HUM: 2, VAMP: 0, WOLV: 0},
                    {'x': 6, 'y': 1, HUM: 5, VAMP: 0, WOLV: 0},
                    {'x': 6, 'y': 5, HUM: 2, VAMP: 0, WOLV: 0},
                    {'x': 7, 'y': 3, HUM: 1, VAMP: 0, WOLV: 0},
                    {'x': 7, 'y': 5, HUM: 2, VAMP: 0, WOLV: 0},
                    {'x': 7, 'y': 7, HUM: 1, VAMP: 0, WOLV: 0},
                    {'x': 7, 'y': 9, HUM: 1, VAMP: 0, WOLV: 0},
                    {'x': 8, 'y': 2, HUM: 1, VAMP: 0, WOLV: 0},
                    {'x': 8, 'y': 8, HUM: 9, VAMP: 0, WOLV: 0},
                    {'x': 9, 'y': 1, HUM: 1, VAMP: 0, WOLV: 0},
                    {'x': 9, 'y': 4, HUM: 5, VAMP: 0, WOLV: 0},
                    {'x': 9, 'y': 7, HUM: 1, VAMP: 0, WOLV: 0},
                    {'x': 9, 'y': 9, HUM: 1, VAMP: 0, WOLV: 0},
                    {'x': 10, 'y': 0, HUM: 1, VAMP: 0, WOLV: 0},
                    {'x': 10, 'y': 10, HUM: 0, VAMP: 5, WOLV: 0},
                    ]

    board = Board((4, 5), initial_pop)
    board2 = Board((11, 11), initial_pop2)

    #player1 = MapPlayer(VAMP, depth=5)
    #player1 = MapPlayer(VAMP, depth=7, type='alphabeta')
    player1 = SmartPlayerAlpha(VAMP, depth=3)

    #player2 = MapPlayer(WOLV, depth=5)
    #player2 = MapPlayer(WOLV, depth=7, type='alphabeta')
    player2 = SmartPlayerAlpha(WOLV, depth=3)
    #player2 = RandomPlayer(WOLV)

    GUI = True
    if GUI:
        from draw import start_GUI, draw
        start_GUI(board2.grid, generate_play(player1, player2, board2, draw))
    else:
        play = generate_play(player1, player2, board2)
        play()
        #import cProfile
        # cProfile.run('play()')
