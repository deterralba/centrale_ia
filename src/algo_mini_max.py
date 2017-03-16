import numpy as np
from time import time
from const import RACE_ID, HUM, WOLV, VAMP
from board import Action, Board
from threading import RLock

from game import TRANSPOSITION, INF

PRINT_SUMMARY = True
VICTORY_IS_INF = True


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


def clone_and_apply_actions(board, actions, race, simulation):
    clone_board = board.copy()
    clone_board.current_player = race
    return clone_board.do_actions(actions, simulation)


def minimax(board, race, race_ennemi, depth, evaluate, esperance, transposition_table=None):
    '''without group division and only one action'''
    old_skip = Board.SKIP_CHECKS
    Board.SKIP_CHECKS = True

    if TRANSPOSITION:
        assert transposition_table is not None

    start_time = time()

    counter = 0
    all_actions = []
    best_action, best_score, total_counter = _min_max(
        True, board, race, race_ennemi, depth, evaluate, esperance, all_actions, counter, transposition_table
    )

    print('=' * 40)
    print('action {}, score {}'.format(best_action, best_score))

    Board.SKIP_CHECKS = old_skip

    if PRINT_SUMMARY:
        print('Action summary')
        all_actions = [action for action in all_actions if action[2] == best_score]
        all_actions.sort(key=lambda x: x[1], reverse=True)
        print('\n'.join(map(str, all_actions)))

    end_time = time() - start_time
    print('#position calc: {}, in {:.2f}s ({:.0f}/s)'.format(total_counter, end_time, total_counter / end_time))
    return [best_action]  # return a list with only one move for the moment


def _min_max(is_max, board, race, race_ennemi, depth, evaluate, esperance, all_actions, counter, transposition_table=None):
    winning_race = board.is_over()
    if winning_race:
        if VICTORY_IS_INF:
            score = INF if winning_race == race else -INF
            return None, score, counter + 1
        else:
            return None, 2 * evaluate(board, race, race_ennemi), counter + 1
    if depth == 0:
        return None, evaluate(board, race, race_ennemi), counter + 1

    playing_race = race if is_max else race_ennemi

    actions = get_available_moves(board, playing_race)  # return a list of possible actions
    best_action = actions[0]
    extrem_score = -INF if is_max else INF
    for action in actions:
        if esperance:
            clone_boards = clone_and_apply_actions(board, [action], playing_race, True)
            scores = []
            for clone_board in clone_boards:
                _, score, counter = _min_max(
                    not is_max, clone_board, race, race_ennemi, depth - 1, evaluate, esperance, all_actions, counter
                )
                scores.append(score * clone_board.proba)
            if len(scores) > 1:
                # print('calculated several clone_boards :', scores, sum([clone_board.proba for clone_board in clone_boards]))
                pass
            score = sum(scores)
        else:
            clone_board = clone_and_apply_actions(board, [action], playing_race, False)
            _, score, counter = _min_max(
                not is_max, clone_board, race, race_ennemi, depth - 1, evaluate, esperance, all_actions, counter
            )

            '''
            # TODO update code for the transposition_table
            clone_board = clone_and_apply_actions(board, [action], playing_race, False)
            skip_min_max = False
            if TRANSPOSITION:
                clone_grid = from_numpy_to_tuple(clone_board)
                if clone_grid in transposition_table.keys():
                    #print('situation already encountered...skipping calculation thks to transposition_table...')
                    score = transposition_table[clone_grid]
                    skip_min_max = True
            if not skip_min_max:
                _, score, counter = _min_max(not is_max, clone_board, race, race_ennemi, depth - 1, all_actions, counter, transposition_table)
                if TRANSPOSITION:
                    if depth == transposition_table['depth']:
                        transposition_table[clone_grid] = score
            '''

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


# For the transposition
SERIALIZE_TUPLE = False
if SERIALIZE_TUPLE:
    def from_numpy_to_tuple(board):
        '''return a list of tuple with five elements : the square (2) and the number of humans, vampires
        and wolves respectively'''
        res = []
        for square in board.enumerate_squares():
            res.append((square[0], square[1], board.grid[square][RACE_ID[HUM]], board.grid[square][RACE_ID[VAMP]],
                        board.grid[square][RACE_ID[WOLV]]))
        return tuple(res)
else:
    def from_numpy_to_tuple(board):
        '''return a list of tuple with five elements : the square (2) and the number of humans, vampires
        and wolves respectively'''
        res = []
        indexes = np.where(board.grid > 0)
        array_x, array_y, array_race = indexes
        for i, x in enumerate(array_x):
            y = array_y[i]
            race = array_race[i]
            nb = board.grid[x, y, race]
            t = (x, y, race, nb)
            res.append(t)
        return tuple(res)
