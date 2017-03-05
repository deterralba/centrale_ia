import numpy as np
from time import time, sleep
from const import RACE_ID
from board import Action, Board
from threading import RLock

INF = 10e9
TRANSPOSITION = False


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

    counter = SafeCounter()
    start_time = time()

    all_actions = []
    best_score, best_action = _min_max(True, board, race, race_ennemi, depth - 0, all_actions, counter)
    '''
    actions = get_available_moves(board, race)  # return a list of possible actions
    print('nb actions: {}'.format(len(actions)))
    best_action = actions[0]
    best_score = -INF
    for action in actions:
        counter.add_count()
        clone_board = clone_and_apply_actions(board, [action], race)
        score, _ = _min_max(False, clone_board, race, race_ennemi, depth - 1, all_actions, counter)
        #score = min_play(clone_board, race, race_ennemi, depth - 1, all_actions, counter)
        if score > best_score:
            best_action = action
            best_score = score
            if best_score >= INF/2:
                break
    '''

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
    print('#position calc: {}, in {:.2f}s ({:.0f}/s)'.format(counter.get_count(), end_time, counter.get_count() / end_time))
    return [best_action]  # return a list with only one move for the moment


def _min_max(is_max, board, race, race_ennemi, depth, all_actions, counter):
    winning_race = board.is_over()
    if winning_race:
        return INF if winning_race == race else -INF, None
    if depth == 0:
        return evaluate(board, race, race_ennemi), None

    playing_race = race if is_max else race_ennemi

    actions = get_available_moves(board, playing_race)  # return a list of possible actions
    best_action = actions[0]
    extrem_score = -INF if is_max else INF
    for action in actions:
        counter.add_count()
        clone_board = clone_and_apply_actions(board, [action], playing_race)
        score, _ = _min_max(not is_max, clone_board, race, race_ennemi, depth - 1, all_actions, counter)
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
                    break    #print('max_score = ' + str(max_score))
    all_actions.append((best_action, depth, extrem_score))
    return extrem_score, best_action


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
