import numpy as np
from board import Board, Action, attack_monsters_with_proba, attack_humans_with_proba, resolve_square, get_outcomes
from const import RACE_ID, HUM, WOLV, VAMP


def test_action():
    shape = (3, 2)  # 3 lines & 2 columns
    board = Board(shape)
    board.grid = np.array([
        [[0, 1, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 2]],
    ], dtype=np.uint8)

    from_case = (0, 0)
    to_case = (0, 1)

    a = Action(from_case, to_case, 1, VAMP)
    assert a.is_valid(board) is True

    b = Action(from_case, (from_case[0] + 2, from_case[1]), 1, HUM)  # to_case is too far
    assert b.is_valid(board) is False

    b = Action(from_case, to_case, 1, HUM)  # human
    assert b.is_valid(board) is False

    b = Action(from_case, to_case, 2, VAMP)  # too many
    assert b.is_valid(board) is False

    b = Action(from_case, from_case, 1, VAMP)  # same case
    assert b.is_valid(board) is False

    b = Action(shape, (shape[0] - 1, shape[1] - 1), 1, VAMP)  # out of board case
    assert b.is_valid(board) is False

    a = Action(from_case, to_case, 1, VAMP)  # to_case is from_case of another action
    assert a.is_valid(board, actions=[Action(to_case, to_case, 1, VAMP)]) is False

    assert Action.square_is_on_grid(shape, board.grid) is False


def test_board_is_over():
    shape = (3, 2)  # 3 lines & 2 columns
    board = Board(shape)

    board.grid = np.array([
        [[0, 1, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 2]],
    ], dtype=np.uint8)
    assert board.is_over() is False

    board.grid[0, 0] = [0, 0, 0]
    print(board.grid)
    assert board.is_over() == WOLV  # only wolves left

    board.grid[0, 0] = [3, 0, 0]
    assert board.is_over() == WOLV  # wolves with humans

    board.grid[2, 1] = [0, 0, 0]
    assert board.is_over() == HUM  # only humans

    board.grid[0, 0] = [0, 0, 0]
    assert board.is_over() == HUM  # empty board


def test_attack_monster_with_proba():
    attacker = VAMP
    square = [0, 0, 0]
    square[RACE_ID[WOLV]] = 2
    square[RACE_ID[VAMP]] = 2

    res_square_win = [0, 0, 0]
    res_square_win[RACE_ID[VAMP]] = 1
    res_square_lose = [0, 0, 0]
    res_square_lose[RACE_ID[WOLV]] = 1
    res = [
        {'proba': 0.5, 'result': res_square_win},
        {'proba': 0.5, 'result': res_square_lose},
    ]
    assert attack_monsters_with_proba(attacker, square) == res

    attacker = WOLV
    square = [0, 0, 0]
    square[RACE_ID[WOLV]] = 5
    square[RACE_ID[VAMP]] = 4

    res_square_win = [0, 0, 0]
    res_square_win[RACE_ID[WOLV]] = 3
    res_square_lose = [0, 0, 0]
    res_square_lose[RACE_ID[VAMP]] = 1
    res = [
        {'proba': 0.75, 'result': res_square_win},
        {'proba': 0.25, 'result': res_square_lose},
    ]
    assert attack_monsters_with_proba(attacker, square) == res

    attacker = WOLV
    square = [0, 0, 0]
    square[RACE_ID[WOLV]] = 6
    square[RACE_ID[VAMP]] = 4

    res_square_win = [0, 0, 0]
    res_square_win[RACE_ID[WOLV]] = 6
    res = [{'proba': 1, 'result': res_square_win}]
    assert attack_monsters_with_proba(attacker, square) == res


def test_attack_human_with_proba():
    attacker = WOLV
    square = [0, 0, 0]
    square[RACE_ID[WOLV]] = 2
    square[RACE_ID[HUM]] = 2

    res_square = [0, 0, 0]
    res_square[RACE_ID[WOLV]] = 4
    res = [{'proba': 1, 'result': res_square}]
    assert attack_humans_with_proba(attacker, square) == res

    attacker = VAMP
    square = [0, 0, 0]
    square[RACE_ID[VAMP]] = 1
    square[RACE_ID[HUM]] = 2

    res_square_win = [0, 0, 0]
    res_square_win[RACE_ID[VAMP]] = 0
    res_square_lose = [0, 0, 0]
    res_square_lose[RACE_ID[HUM]] = 1
    res = [
        {'proba': 0.25, 'result': res_square_win},
        {'proba': 0.75, 'result': res_square_lose},
    ]
    assert attack_humans_with_proba(attacker, square) == res


def test_resolve_square():
    shape = (3, 2)  # 3 lines & 2 columns
    board1 = Board(shape)
    board1.current_player = VAMP
    board1.proba = 0.5
    #HUM: 0, VAMP: 1, WOLV: 2
    board1.grid = np.array([
        [[1, 0, 0], [0, 2, 0]],
        [[0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 2, 2]],
    ], dtype=np.uint8)

    square = (2, 1)
    board2 = board1.copy()

    outcomes = get_outcomes(board1, square)
    for outcome in outcomes:
        outcome['result'] = list(outcome['result'])
    assert outcomes == [
        {'proba': 0.5, 'result': [0, 1, 0]},
        {'proba': 0.5, 'result': [0, 0, 1]},
    ]
    boards = resolve_square([board1, board2], outcomes, square)
    for board in boards:
        assert list(board.grid[square]) in [[0, 1, 0], [0, 0, 1]]
        print(board.proba)
        assert board.proba == 0.25

