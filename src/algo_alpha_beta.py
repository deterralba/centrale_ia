import numpy as np
from const import RACE_ID, HUM, WOLV, VAMP
from board import Action, Board
from algo_mini_max import evaluate, get_available_moves, add_to_transposition_table, from_numpy_to_tuple


def alphabeta(board, race, race_ennemi, depth, transposition_table):
    '''without group division and only one action'''

    old_skip = Board.SKIP_CHECKS
    Board.SKIP_CHECKS = True
    actions = get_available_moves(board, race)  # return a list of possible actions
    print('nb actions: {}'.format(len(actions)))
    best_action = actions[0]
    alpha = float('-inf')
    beta = float('inf')
    for action in actions:
        print('action: {})'.format(action))
        clone_board = board.copy()
        clone_grid = from_numpy_to_tuple(clone_board)
        if clone_grid in transposition_table.keys():
            print('situation already encountered...skipping calculation thks to transposition_table...')
            score = transposition_table[clone_grid]
        else:
            clone_board.current_player = race
            clone_board.do_actions([action])
            score = min_play_alphabeta(clone_board, race, race_ennemi, depth, transposition_table, alpha, beta)
            transposition_table = add_to_transposition_table(transposition_table, clone_grid, score)
        if score > alpha:
            best_action = action
            alpha = score
    print('='*40)
    print('action {}, score {}'.format(best_action, alpha))
    Board.SKIP_CHECKS = old_skip
    return [best_action]  # return a list with only one move for the moment


def min_play_alphabeta(board, race, race_ennemi, depth, transposition_table, alpha, beta):
    # print('entering min_play, depth {}'.format(depth))
    winning_race = board.is_over()
    if winning_race:
        return float('inf') if winning_race == race else float('-inf')
    if depth == 0:
        return evaluate(board, race, race_ennemi)

    actions = get_available_moves(board, race_ennemi)
    for action in actions:
        clone_board = board.copy()
        clone_grid = from_numpy_to_tuple(clone_board)
        if clone_grid in transposition_table.keys():
            print('situation already encountered...skipping calculation thks to transposition_table...')
            score = transposition_table[clone_grid]
        else:
            clone_board.current_player = race_ennemi
            clone_board.do_actions([action])
            score = max_play_alphabeta(clone_board, race, race_ennemi, depth-1, transposition_table, alpha, beta)
            # print('score = ' + str(score))
        if score < beta:
            beta = score
        if alpha >= beta:
            print('alpha >= beta...')
            print(alpha)
            print('>=')
            print(beta)
            print('skipping calculation in min_play_alphabeta...')
            return beta
    # print('min_score = ' + str(min_score))
    return beta


def max_play_alphabeta(board, race, race_ennemi, depth, transposition_table, alpha, beta):
    # print('entering max_play, depth {}'.format(depth))
    winning_race = board.is_over()
    if winning_race:
        return float('inf') if winning_race == race else float('-inf')
    if depth == 0:
        return evaluate(board, race, race_ennemi)

    actions = get_available_moves(board, race)  # return a list of possible actions
    # max_score = float('-inf')
    # alpha = float('-inf')
    # beta = float('inf')
    for action in actions:
        clone_board = board.copy()
        clone_grid = from_numpy_to_tuple(clone_board)
        if clone_grid in transposition_table.keys():
            print('situation already encountered...skipping calculation thks to transposition_table...')
            score = transposition_table[clone_grid]
        else:
            clone_board.current_player = race
            clone_board.do_actions([action])
            score = min_play_alphabeta(clone_board, race, race_ennemi, depth-1, transposition_table, alpha, beta)
            # print('score = ' + str(score))
        if score > alpha:
            alpha = score
        if alpha >= beta:
            print('alpha >= beta...')
            print(alpha)
            print('>=')
            print(beta)
            print('skipping calculation in max_play_alphabeta...')
            return alpha
    # print('max_score = ' + str(max_score))
    return alpha

