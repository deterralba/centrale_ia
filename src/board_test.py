import numpy as np
from board import Board, Action

def test_action():
    shape = (2, 3)
    board = Board(shape)
    board.grid = np.array([
        [[0, 0, 1], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 0]],
        [[0, 0, 0], [0, 0, 2]],
    ], dtype=np.int32)

    from_case = (0, 0)
    to_case = (0, 1)

    a = Action(from_case, to_case, 1, 'V')
    assert a.is_valid(board) is True

    b = Action(from_case, (from_case[0] + 2, from_case[1]), 1, 'H')  # to_case is too far
    assert b.is_valid(board) is False

    b = Action(from_case, to_case, 1, 'H')  # human
    assert b.is_valid(board) is False

    b = Action(from_case, to_case, 2, 'V')  # too many
    assert b.is_valid(board) is False

    b = Action(from_case, from_case, 1, 'V')  # same case
    assert b.is_valid(board) is False

    b = Action(shape, (shape[0] - 1, shape[1] - 1), 1, 'V')  # out of board case
    assert b.is_valid(board) is False

    a = Action(from_case, to_case, 1, 'V')  # to_case is from_case of another action
    assert a.is_valid(board, actions=[Action(to_case, to_case, 1, 'V')]) is False

    assert Action.square_is_on_grid(shape, board.grid) is False

