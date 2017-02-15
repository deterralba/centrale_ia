import numpy as np
from const import RACE_ID, HUM, WOLV, VAMP
from board import Action, Board


def evaluate(board, race, race_ennemi):
    '''heuristic function'''
    sum_ = np.sum(board.grid, axis=(0, 1))
    if sum_[RACE_ID[race]] == 0:
        return float('-inf')
    elif sum_[RACE_ID[race_ennemi]] == 0:
        return float('inf')
    else:
        return sum_[RACE_ID[race]] - sum_[RACE_ID[race_ennemi]]


def minimax(board, race, race_ennemi, depth):
    '''without group division and only one action'''
    old_skip = Board.SKIP_CHECKS
    Board.SKIP_CHECKS = True
    actions = get_available_moves(board, race)  # return a list of possible actions
    print('nb actions: {}'.format(len(actions)))
    best_action = actions[0]
    best_score = float('-inf')
    for action in actions:
        print('action: {})'.format(action))
        clone_board = board.copy()
        clone_board.current_player = race
        clone_board.do_actions([action])
        score = min_play(clone_board, race, race_ennemi, depth)
        if score > best_score:
            best_action = action
            best_score = score
    print('='*40)
    print('action {}, score {}'.format(best_action, best_score))
    Board.SKIP_CHECKS = old_skip
    return [best_action]  # return a list with only one move for the moment


def min_play(board, race, race_ennemi, depth):
    #print('entering min_play, depth {}'.format(depth))
    winning_race = board.is_over()
    if winning_race:
        return float('inf') if winning_race == race else float('-inf')
    if depth == 0:
        return evaluate(board, race, race_ennemi)

    actions = get_available_moves(board, race_ennemi)
    min_score = float('inf')
    for action in actions:
        clone_board = board.copy()
        clone_board.current_player = race_ennemi
        clone_board.do_actions([action])
        score = max_play(clone_board, race, race_ennemi, depth-1)
        #print('score = ' + str(score))
        if score < min_score:
            min_score = score
            if min_score == float('-inf'):
                #print('returning -inf')
                return min_score
    #print('min_score = ' + str(min_score))
    return min_score


def max_play(board, race, race_ennemi, depth):
    #print('entering max_play, depth {}'.format(depth))
    winning_race = board.is_over()
    if winning_race:
        return float('inf') if winning_race == race else float('-inf')
    if depth == 0:
        return evaluate(board, race, race_ennemi)

    actions = get_available_moves(board, race)  # return a list of possible actions
    max_score = float('-inf')
    for action in actions:
        clone_board = board.copy()
        clone_board.current_player = race
        clone_board.do_actions([action])
        score = min_play(clone_board, race, race_ennemi, depth-1)
        #print('score = ' + str(score))
        if score > max_score:
            max_score = score
            if max_score == float('inf'):
                #print('returning inf')
                return max_score
    #print('max_score = ' + str(max_score))
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

