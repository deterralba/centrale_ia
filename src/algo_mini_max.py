import numpy as np
from time import time, sleep
from const import RACE_ID
from board import Action, Board, enumerate_squares
from threading import RLock

from game import TRANSPOSITION, INF


class SafeCounter:

    def __init__(self):
        self._nb_iterations = 0
        self._lock = RLock()

    def add_count(self):
        with self._lock:
            self._nb_iterations += 1

    def get_count(self):
        return self._nb_iterations

    def reset_count(self):
        with self._lock:
            self._nb_iterations = 0
            print('nb iterations reset: ', self._nb_iterations)


def evaluate(board, race, race_ennemi):
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

def evaluate_fred(board, race, race_ennemi):
    ally_squares = []
    enemy_squares = []
    human_squares = []
    H = np.sum(board.grid, axis=(0, 1))
    
    for square in board.enumerate_squares():
        if square[RACE_ID[race]]>0:
            ally_squares += [square]
        elif square[RACE_ID[race_ennemi]]>0:
            enemy_squares += [square]
        elif square[RACE_ID[HUM]]>0:
            human_squares += [square]
    
    for square_ally in ally_squares:
        for square_hum in human_squares:
            dist = L_inf_dist(square_ally, square_hum)
            square_content_fight=0
            H += (0.1**dist) * expected_outcome(square_content_fight)
    
    for square_ally in ally_squares:
        for square_enemy in enemy_squares:
            dist = L_inf_dist(square_ally, square_enemy)
            square_fight=0
            H += (0.1**dist) * expected_outcome(square_content_fight)
    
    for square_enemy in enemy_squares:
        for square_hum in human_squares:
            dist = L_inf_dist(square_enemy, square_hum)
            square_fight=0
            H += (0.1**dist) * expected_outcome(square_content_fight)
    
    return H[RACE_ID[race]]-H[RACE_ID[race_ennemi]]
    
def expected_outcome(square_content):
    pass

def L_inf_dist(square1, square2):
    return max(square1[0]-square2[0],square1[1]-square2[1],square2[0]-square1[0],square2[1]-square1[1])
    
def clone_and_apply_actions(board, actions, race):
    clone_board = board.copy()
    clone_board.current_player = race
    clone_board.do_actions(actions)
    return clone_board


def minimax(board, race, race_ennemi, depth, transposition_table=None):
    '''without group division and only one action'''
    old_skip = Board.SKIP_CHECKS
    Board.SKIP_CHECKS = True

    if TRANSPOSITION:
        assert transposition_table is not None

    start_time = time()

    counter = 0
    all_actions = []
    best_action, best_score, total_counter = _min_max(True, board, race, race_ennemi, depth, all_actions, counter)

    print('=' * 40)
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
    print('#position calc: {}, in {:.2f}s ({:.0f}/s)'.format(total_counter, end_time, total_counter / end_time))
    return [best_action]  # return a list with only one move for the moment


def _min_max(is_max, board, race, race_ennemi, depth, all_actions, counter):
    winning_race = board.is_over()
    if winning_race:
        score = INF if winning_race == race else -INF
        return None, score, counter + 1
    if depth == 0:
        return None, evaluate(board, race, race_ennemi), counter + 1

    playing_race = race if is_max else race_ennemi

    actions = get_available_moves(board, playing_race)  # return a list of possible actions
    best_action = actions[0]
    extrem_score = -INF if is_max else INF
    for action in actions:
        clone_board = clone_and_apply_actions(board, [action], playing_race)
        _, score, counter = _min_max(not is_max, clone_board, race, race_ennemi, depth - 1, all_actions, counter)
        #print('score = ' + str(score))
        if is_max:
            if score > extrem_score:
                extrem_score = score
                best_action = action
                if extrem_score >= INF / 2:
                    break
        else:
            if score < extrem_score:
                extrem_score = score
                best_action = action
                if extrem_score <= - INF / 2:
                    break  # print('max_score = ' + str(max_score))
    all_actions.append((best_action, depth, extrem_score))
    return best_action, extrem_score, counter


def get_available_moves(board, race):
    '''return a list of possible actions'''
    actions = []
    possibles_to = []
    for square in board.enumerate_squares():
        units = board.grid[square][RACE_ID[race]]
        if units > 0:
            possibles_to = [
                (square[0] + i, square[1] + j) for i in range(-1, 2) for j in range(-1, 2)
                if (i != 0 or j != 0) and Action.square_is_on_grid((square[0] + i, square[1] + j), board.grid)
            ]
            actions.extend([Action(square, to, units, race) for to in possibles_to])
    return actions
