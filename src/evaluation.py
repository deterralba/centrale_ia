from const import RACE_ID, HUM
from game import INF
import numpy as np


def evaluate_inf(board, race, race_ennemi):
    '''heuristic function'''
    sum_ = np.sum(board.grid, axis=(0, 1))
    if sum_[RACE_ID[race]] == 0:
        return -INF
    elif sum_[RACE_ID[race_ennemi]] == 0:
        return INF
    else:
        # evite la dispersion
        dispersion = int(np.sum(board.grid[:, :, RACE_ID[race]] > 0))
        return 50 * (int(sum_[RACE_ID[race]]) - int(sum_[RACE_ID[race_ennemi]])) - dispersion


def evaluate_disp(board, race, race_ennemi):
    '''heuristic function'''
    sum_ = np.sum(board.grid, axis=(0, 1))
    # evite la dispersion
    dispersion = int(np.sum(board.grid[:, :, RACE_ID[race]] > 0))
    return 50 * (int(sum_[RACE_ID[race]]) - int(sum_[RACE_ID[race_ennemi]])) - dispersion


def evaluate_fred(board, race, race_ennemi):
    ally_squares = []
    enemy_squares = []
    human_squares = []
    sum_ = np.sum(board.grid, axis=(0, 1))
    H = int(sum_[RACE_ID[race]]) - int(sum_[RACE_ID[race_ennemi]])

    for square in board.enumerate_squares():
        if board.grid[square][RACE_ID[race]] > 0:
            ally_squares += [square]
        elif board.grid[square][RACE_ID[race_ennemi]] > 0:
            enemy_squares += [square]
        elif board.grid[square][RACE_ID[HUM]] > 0:
            human_squares += [square]

    for square_ally in ally_squares:
        for square_hum in human_squares:
            dist = L_inf_dist(square_ally, square_hum)
            H += (0.1**dist) * expected_outcome_attack_humans(
                board.grid[square_ally][RACE_ID[race]],
                board.grid[square_hum][RACE_ID[HUM]])

    for square_ally in ally_squares:
        for square_enemy in enemy_squares:
            dist = L_inf_dist(square_ally, square_enemy)
            H += (0.1**dist) * expected_outcome_attack_player(
                board.grid[square_ally][RACE_ID[race]],
                board.grid[square_enemy][RACE_ID[race_ennemi]])
            H -= (0.1**dist) * expected_outcome_attack_player(
                board.grid[square_enemy][RACE_ID[race_ennemi]],
                board.grid[square_ally][RACE_ID[race]])

    for square_enemy in enemy_squares:
        for square_hum in human_squares:
            dist = L_inf_dist(square_enemy, square_hum)
            H += (0.1**dist) * expected_outcome_attack_humans(
                board.grid[square_enemy][RACE_ID[race_ennemi]],
                board.grid[square_hum][RACE_ID[HUM]])

    return H


def expected_outcome_attack_humans(attackingNumberOfPlayer, defendingNumberOfHumans):
    '''Returns the average increase or decrease in warriors after combat'''
    if(attackingNumberOfPlayer >= 1.5 * defendingNumberOfHumans):
        return defendingNumberOfHumans
    elif(attackingNumberOfPlayer >= defendingNumberOfHumans):
        P = attackingNumberOfPlayer / defendingNumberOfHumans - 0.5
    else:
        P = attackingNumberOfPlayer / (2 * defendingNumberOfHumans)

    # We lose units with probability 1-P and gain defending units with prob. P
    winCase = (P - 1) * attackingNumberOfPlayer + P * defendingNumberOfHumans
    # We lose our units
    losingCase = -attackingNumberOfPlayer

    return P * winCase + (1 - P) * losingCase


def expected_outcome_attack_player(attackingNumberOfPlayer, defendingNumberOfPlayer):
    if(attackingNumberOfPlayer >= 1.5 * defendingNumberOfPlayer):
        P = 1
    elif(attackingNumberOfPlayer >= defendingNumberOfPlayer):
        P = attackingNumberOfPlayer / defendingNumberOfPlayer - 0.5
    else:
        P = attackingNumberOfPlayer / (2 * defendingNumberOfPlayer)

    # We don't gain the defending units but the enemy loses it : same thing !
    winCase = (P - 1) * attackingNumberOfPlayer + defendingNumberOfPlayer
    # We lose all our units and the opponents loses them with probability P
    losingCase = -attackingNumberOfPlayer + P * defendingNumberOfPlayer

    return P * winCase + (1 - P) * losingCase


def L_inf_dist(square1, square2):
    return max(square1[0] - square2[0], square1[1] - square2[1],
               square2[0] - square1[0], square2[1] - square1[1])
