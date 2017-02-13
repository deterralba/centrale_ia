import numpy as np
from const import RACE_ID, HUM, WOLV, VAMP
from board import Action


def evaluate(board, race, race_ennemi):
    '''heuristique function'''
    sum_ = np.sum(board.grid, axis=(0, 1))
    print('result = ' + str(sum_[RACE_ID[race]] - sum_[RACE_ID[race_ennemi]]))
    return sum_[RACE_ID[race]] - sum_[RACE_ID[race_ennemi]]


def minimax(board, race, race_ennemi, depth):
    '''without group division and only one action'''
    actions = get_available_moves(board, race)  # return a list of possible actions
    best_action = actions[0]
    best_score = float('-inf')
    print(actions)
    for action in actions:
        clone_board = board
        clone_board.do_actions([action])
        print(clone_board)
        score = min_play(clone_board, race, race_ennemi, depth)
        if score > best_score:
            best_action = action
            best_score = score
    return [best_action]  # return a list with only one move for the moment


def min_play(board, race, race_ennemi, depth):
    winning_race = board.is_over()
    if winning_race:
        return float('inf') if winning_race == race else float('-inf')
    if depth == 0:
        return evaluate(board, race, race_ennemi)

    actions = get_available_moves(board, race_ennemi)
    min_score = float('inf')
    for action in actions:
        clone_board = board
        print(action)
        clone_board.do_actions([action])
        print('done 2')
        score = max_play(clone_board, race, race_ennemi, depth-1)
        if score < min_score:
            min_score = score
    print('min_score = ' + str(min_score))
    return min_score


def max_play(board, race, race_ennemi, depth):
    winning_race = board.is_over()
    if winning_race:
        return float('inf') if winning_race == race else float('-inf')
    if depth == 0:
        print('ici')
        return evaluate(board, race, race_ennemi)

    actions = board.get_available_moves()
    max_score = float('-inf')
    for action in actions:
        clone_board = board
        # clone_board = do_clone_actions(board, [action])
        clone_board.do_actions([action])
        score = min_play(clone_board, race, race_ennemi, depth-1)
        if score > max_score:
            max_score = score
    print('max_score = ' + str(max_score))
    return max_score


def get_available_moves(board, race):
    '''return a list of possible actions'''
    actions = []
    possibles_to = []
    for square in board.enumerate_squares():
        units = board.grid[square][RACE_ID[race]]
        if units > 0:
            possibles_to.append((square[0] - 1, square[1] - 1))
            possibles_to.append((square[0], square[1] - 1))
            possibles_to.append((square[0] + 1, square[1] - 1))
            possibles_to.append((square[0] + 1, square[1]))
            possibles_to.append((square[0] + 1, square[1] + 1))
            possibles_to.append((square[0], square[1] + 1))
            possibles_to.append((square[0] - 1, square[1] + 1))
            possibles_to.append((square[0] - 1, square[1]))
            for to in possibles_to:
                if Action.square_is_on_grid(to, board.grid):
                    actions.append(Action(square, to, units, race))
    return actions


# def do_clone_actions(board, actions):
#     clone_board = board
#     print(clone_board)
#     if not SKIP_CHECKS:
#         for square in clone_board.enumerate_squares():
#             nb_zeros = list(clone_board.grid[square]).count(0)
#             if nb_zeros < 2:
#                 raise ValueError(
#                     'Board is not consistent: several races in one square: {}: {}'.format(square, clone_board.grid[square]))
#     for action in actions:
#         print(action)
#         clone_board.moves(action)
#     for square in clone_board.enumerate_squares():
#         clone_board.resolve_square(square)
#     return clone_board
