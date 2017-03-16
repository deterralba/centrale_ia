from algo_mini_max import get_available_moves, clone_and_apply_actions, from_numpy_to_tuple
import numpy as np
from time import time, sleep
from const import RACE_ID, HUM, WOLV, VAMP
from board import Action, Board
from threading import RLock
from game import TRANSPOSITION, INF

PRINT_SUMMARY = False
VICTORY_IS_INF = True


def alphabeta(board, race, race_ennemi, depth, evaluate, esperance, transposition_table=None, with_score=False):
    '''without group division and only one action'''
    old_skip = Board.SKIP_CHECKS
    Board.SKIP_CHECKS = True
    start_time = time()

    if TRANSPOSITION:
        assert transposition_table is not None

    counter = 0
    alpha = -INF
    beta = INF

    all_actions = []
    best_action, best_score, total_counter = _alpha_beta(
        True, board, race, race_ennemi, depth, evaluate, esperance, all_actions, counter, alpha, beta, transposition_table
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
    #print('#position calc: {}, in {:.2f}s ({:.0f}/s)'.format(total_counter, end_time, total_counter / end_time))
    if with_score:
        return [best_action], best_score
    return [best_action]  # return a list with only one move for the moment


def _alpha_beta(is_max, board, race, race_ennemi, depth, evaluate, esperance, all_actions, counter, alpha, beta, transposition_table=None):
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
    np.random.shuffle(actions)
    best_action = actions[0]
    for action in actions:
        if esperance:
            clone_boards = clone_and_apply_actions(board, [action], playing_race, True)
            scores = []
            for clone_board in clone_boards:
                _, score, counter = _alpha_beta(
                    not is_max, clone_board, race, race_ennemi, depth - 1, evaluate, esperance, all_actions, counter, alpha, beta
                )
                scores.append(score * clone_board.proba)
            if len(scores) > 1:
                # print('calculated several clone_boards :', scores, sum([clone_board.proba for clone_board in clone_boards]))
                pass
            score = sum(scores)
        else:
            clone_board = clone_and_apply_actions(board, [action], playing_race, False)
            _, score, counter = _alpha_beta(
                not is_max, clone_board, race, race_ennemi, depth - 1, evaluate, esperance, all_actions, counter, alpha, beta
            )

        '''
        # TRANSPOSITION old code
        clone_board = clone_and_apply_actions(board, [action], playing_race, False)
        skip_alpha_beta = False
        if TRANSPOSITION:
            clone_grid = from_numpy_to_tuple(clone_board)
            if clone_grid in transposition_table.keys():
                # print('situation already encountered...skipping calculation thks to transposition_table...')
                score = transposition_table[clone_grid]
                skip_alpha_beta = True
        if not skip_alpha_beta:
            _, score, counter = _alpha_beta(not is_max, clone_board, race, race_ennemi, depth - 1, evaluate, esperance,
                                            all_actions, counter, alpha, beta, transposition_table)
            if TRANSPOSITION:
                if depth == transposition_table['depth']:
                    transposition_table[clone_grid] = score

        '''
        # print('score = ' + str(score))
        if is_max:
            if score > alpha:
                alpha = score
                best_action = action
            if alpha >= beta:
                all_actions.append((best_action, depth, alpha))
                return best_action, alpha, counter

        else:
            if score < beta:
                beta = score
                best_action = action
            if alpha >= beta:
                all_actions.append((best_action, depth, beta))
                return best_action, beta, counter

    if is_max:
        all_actions.append((best_action, depth, alpha))
        return best_action, alpha, counter
    else:
        all_actions.append((best_action, depth, beta))
        return best_action, beta, counter

