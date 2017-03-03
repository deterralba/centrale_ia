import numpy as np
from const import RACE_ID, HUM, WOLV, VAMP
from board import Action, Board
from time import sleep, time
from threading import RLock

TRANSPOSITION = True

INF = 10e9

_nb_iterations = 0
_lock = RLock()
def add_count():
    global nb_iterations
    with _lock:
        nb_iterations += 1

def evaluate(board, race, race_ennemi):
    '''heuristic function'''
    sum_ = np.sum(board.grid, axis=(0, 1))
    if sum_[RACE_ID[race]] == 0:
        return -INF
    elif sum_[RACE_ID[race_ennemi]] == 0:
        return INF
    else:
        # evite la dispersion
        dispersion = int(np.sum(board.grid[:,:,RACE_ID[race]] > 0))
        return 50*(int(sum_[RACE_ID[race]]) - int(sum_[RACE_ID[race_ennemi]])) - dispersion


def minimax(board, race, race_ennemi, depth, transposition_table):
    '''without group division and only one action'''

    start_time = time()
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
        if TRANSPOSITION:
            clone_grid = from_numpy_to_tuple(clone_board)
            if clone_grid in transposition_table.keys():
                print('situation already encountered...skipping calculation thks to transposition_table...')
                score = transposition_table[clone_grid]
        else:
            clone_board.current_player = race
            clone_board.do_actions([action])
            score = min_play(clone_board, race, race_ennemi, depth-1, all_actions, transposition_table)
            if TRANSPOSITION:
                transposition_table = add_to_transposition_table(transposition_table, clone_grid, score)
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


def min_play(board, race, race_ennemi, depth, all_actions, transposition_table):
    #print('entering min_play, depth {}'.format(depth))
    winning_race = board.is_over()
    if winning_race:
        return INF if winning_race == race else -INF
    if depth == 0:
        return evaluate(board, race, race_ennemi)

    actions = get_available_moves(board, race_ennemi)
    best_action = actions[0]
    min_score = INF
    for action in actions:
        add_count()
        clone_board = board.copy()
        if TRANSPOSITION:
            clone_grid = from_numpy_to_tuple(clone_board)
            if clone_grid in transposition_table.keys():
                print('situation already encountered...skipping calculation thks to transposition_table...')
                score = transposition_table[clone_grid]
        else:
            clone_board.current_player = race_ennemi
            clone_board.do_actions([action])
            score = max_play(clone_board, race, race_ennemi, depth-1, all_actions, transposition_table)
            #TODO add to transopistion table ?
            # print('score = ' + str(score))
        if score < min_score:
            min_score = score
            best_action = action
            if min_score <= -INF/2:
                #print('returning -inf')
                all_actions.append((action, depth, score))
                return min_score
    all_actions.append((best_action, depth, score))
    # print('min_score = ' + str(min_score))
    return min_score


def max_play(board, race, race_ennemi, depth, all_actions, transposition_table):
    #print('entering max_play, depth {}'.format(depth))
    winning_race = board.is_over()
    if winning_race:
        return INF if winning_race == race else -INF
    if depth == 0:
        return evaluate(board, race, race_ennemi)

    actions = get_available_moves(board, race)  # return a list of possible actions
    best_action = actions[0]
    max_score = -INF
    for action in actions:
        add_count()
        clone_board = board.copy()
        if TRANSPOSITION:
            clone_grid = from_numpy_to_tuple(clone_board)
            if clone_grid in transposition_table.keys():
                print('situation already encountered...skipping calculation thks to transposition_table...')
                score = transposition_table[clone_grid]
        else:
            clone_board.current_player = race
            clone_board.do_actions([action])
            score = min_play(clone_board, race, race_ennemi, depth-1, all_actions, transposition_table)
            #TODO add to transopistion table ?
            # print('score = ' + str(score))
        if score > max_score:
            max_score = score
            best_action = action
            if max_score >= INF/2:
                #print('returning inf')
                all_actions.append((action, depth, score))
                return max_score
    #print('max_score = ' + str(max_score))
    all_actions.append((best_action, depth, score))
    return max_score


def get_available_moves(board, race):
    '''return a list of possible actions'''
    actions = []
    possibles_to = []
    for square in board.enumerate_squares():
        units = board.grid[square][RACE_ID[race]]
        if units > 0:
            possibles_to = [
                (square[0] + i , square[1] + j) for i in range(-1, 2) for j in range(-1, 2)
                if (i != 0 or j != 0) and Action.square_is_on_grid((square[0] + i, square[1] + j), board.grid)
            ]
            actions.extend([Action(square, to, units, race) for to in possibles_to])
    return actions


def add_to_transposition_table(transposition_table, grid, score):
    if grid in transposition_table.keys():
        print('board already in TRANSPOSITION_TABLE')
    else:
        transposition_table[grid] = score
        # print('new grid successfully added to the TRANSPOSITION_TABLE : ')
        print(grid, score)
    return transposition_table


def from_numpy_to_tuple(board):
    '''return a list of tuple with five elements : the square (2) and the number of humans, vampires
    and wolves respectively'''
    res = []
    for square in board.enumerate_squares():
        res.append((square[0], square[1], board.grid[square][RACE_ID[HUM]], board.grid[square][RACE_ID[VAMP]],
                    board.grid[square][RACE_ID[WOLV]]))
    return tuple(res)

