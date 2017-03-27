"""Tests for https://www.codewars.com/kata/validate-sudoku-with-size-nxn."""

import pytest


TEST = [
    (
  [7,8,4,  1,5,9,  3,2,6],
  [5,3,9,  6,7,2,  8,4,1],
  [6,1,2,  4,3,8,  7,5,9],

  [9,2,8,  7,1,5,  4,6,3],
  [3,5,7,  8,4,6,  1,9,2],
  [4,6,1,  9,2,3,  5,8,7],

  [8,7,6,  3,9,4,  2,1,5],
  [2,4,3,  5,6,1,  9,7,8],
  [1,9,5,  2,8,7,  6,3,4]
    , True),
]


@pytest.mark.parametrize('m, result', TEST)
def test_sudoku_validator(m, result):
    """Test sudoku_validator returns correct result."""
    from sudoku_validator import sudoku_validator
    assert sudoku_validator(m) == result
