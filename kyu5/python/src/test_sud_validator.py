"""Tests for https://www.codewars.com/kata/did-i-finish-my-sudoku/."""

import pytest

valid = [
    [1, 3, 2, 5, 7, 9, 4, 6, 8],
    [4, 9, 8, 2, 6, 1, 3, 7, 5],
    [7, 5, 6, 3, 8, 4, 2, 1, 9],
    [6, 4, 3, 1, 5, 8, 7, 9, 2],
    [5, 2, 1, 7, 9, 3, 8, 4, 6],
    [9, 8, 7, 4, 2, 6, 5, 3, 1],
    [2, 1, 4, 9, 3, 5, 6, 8, 7],
    [3, 6, 5, 8, 1, 7, 9, 2, 4],
    [8, 7, 9, 6, 4, 2, 1, 5, 3]
]

invalid_last_column = [
    [1, 3, 2,   5, 7, 9,    4, 6, 8],
    [4, 9, 8,   2, 6, 1,    3, 7, 5],
    [7, 5, 6,   3, 8, 4,    2, 1, 9],

    [6, 4, 3,   1, 5, 8,    7, 9, 2],
    [5, 2, 1,   7, 9, 3,    8, 4, 6],
    [9, 8, 7,   4, 2, 6,    5, 3, 1],

    [2, 1, 4,   9, 3, 5,    6, 8, 7],
    [3, 6, 5,   8, 1, 7,    9, 2, 4],
    [8, 7, 9,   6, 4, 2,    1, 3, 5]
]

INPUTS = [
    (valid, 'Finished!'),
    (invalid_last_column, 'Try again!'),
]
@pytest.mark.parametrize('board, result', INPUTS)
def test_valid_sudoku(board, result):
    """Test if function returns correct message."""
    from sud_validator import done_or_not
    assert done_or_not(board) == result
