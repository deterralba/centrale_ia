import numpy as np
from const import RACE_ID, HUM, WOLV, VAMP


def evaluate(board, race, race_ennemi):
    count_race = 0
    count_ennemi = 0
    # TODO replace by a numpy function
    # for square in board.enumerate_squares():
    #     count_race = count_race + board.grid[square][RACE_ID[self.race]]
    #     count_ennemi = count_ennemi + board.grid[square][RACE_ID[self.ennemi]]
    # return count_race - count_ennemi
    return np.sum(board.grid, axis=(0, 1))[RACE_ID[race]] - np.sum(board.grid, axis=(0, 1))[RACE_ID[race_ennemi]]


def minimax(board, race, race_ennemi):
    '''sans division de groupe / tout le monde bouge'''
    moves = board.get_available_moves(race)  # TODO return a list of possible actions
    best_move = moves[0]
    best_score = float('-inf')
    for move in moves:
        clone = board.do_actions(move)
        score = min_play(clone, race, race_ennemi)
        if score > best_score:
            best_move = move
            best_score = score
    return best_move


def min_play(board, race, race_ennemi):
    if board.is_over():
        return evaluate(board, race, race_ennemi)
    moves = board.get_available_moves()
    best_score = float('inf')
    for move in moves:
        clone = board.do_actions(move)
        score = max_play(clone, race, race_ennemi)
        if score < best_score:
            # best_move = move
            best_score = score
    return best_score


def max_play(board, race, race_ennemi):
    if board.is_over():
        return evaluate(board,race, race_ennemi)
    moves = board.get_available_moves()
    best_score = float('-inf')
    for move in moves:
        clone = board.do_actions(move)
        score = min_play(clone)
        if score > best_score:
            # best_move = move
            best_score = score
    return best_score


