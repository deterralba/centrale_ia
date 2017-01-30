import numpy as np
from board import Board, Action
from const import RACE_ID, HUM, WOLV, VAMP

def test_action():
    shape = (3, 2) # 3 lines & 2 columns
    board = Board(shape)
    board.grid = np.array([
        [[0, 1, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 2]],
    ], dtype=np.int32)

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
    shape = (3, 2) # 3 lines & 2 columns
    board = Board(shape)

    board.grid = np.array([
        [[0, 1, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 2]],
    ], dtype=np.int32)
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
