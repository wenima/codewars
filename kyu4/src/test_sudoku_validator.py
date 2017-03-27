"""Tests for https://www.codewars.com/kata/validate-sudoku-with-size-nxn."""

import pytest

valid_m = [
[7,8,4,  1,5,9,  3,2,6],
[5,3,9,  6,7,2,  8,4,1],
[6,1,2,  4,3,8,  7,5,9],

[9,2,8,  7,1,5,  4,6,3],
[3,5,7,  8,4,6,  1,9,2],
[4,6,1,  9,2,3,  5,8,7],

[8,7,6,  3,9,4,  2,1,5],
[2,4,3,  5,6,1,  9,7,8],
[1,9,5,  2,8,7,  6,3,4]
]

invalid_m_str = [
['7',8,4,  1,5,9,  3,2,6],
[5,3,9,  6,7,2,  8,4,1],
[6,1,2,  4,3,8,  7,5,9],

[9,2,8,  7,1,5,  4,6,3],
[3,5,7,  8,4,6,  1,9,2],
[4,6,1,  9,2,3,  5,8,7],

[8,7,6,  3,9,4,  2,1,5],
[2,4,3,  5,6,1,  9,7,8],
[1,9,5,  2,8,7,  6,3,4]
]

invalid_m_float = [
[7.9999,8,4,  1,5,9,  3,2,6],
[5,3,9,  6,7,2,  8,4,1],
[6,1,2,  4,3,8,  7,5,9],

[9,2,8,  7,1,5,  4,6,3],
[3,5,7,  8,4,6,  1,9,2],
[4,6,1,  9,2,3,  5,8,7],

[8,7,6,  3,9,4,  2,1,5],
[2,4,3,  5,6,1,  9,7,8],
[1,9,5,  2,8,7,  6,3,4]
]

# TEST = [
#     (sudoku, True),
#     (sudoku[:1], False),
# ]

@pytest.fixture
def valid_sudoku():
    from sudoku_validator import Sudoku
    new_sudoku = Sudoku(valid_m)
    return new_sudoku

@pytest.fixture
def invalid_sudoku():
    from sudoku_validator import Sudoku
    new_sudoku = Sudoku(invalid_m_str)
    return new_sudoku

@pytest.fixture
def invalid_sudoku_float():
    from sudoku_validator import Sudoku
    new_sudoku = Sudoku(invalid_m_float)
    return new_sudoku


# @pytest.mark.parametrize('m, result', TEST)
def test_sudoku_validator(valid_sudoku):
    """Test sudoku_validator returns correct result."""
    assert valid_sudoku.is_valid() == True


def test_sudoku_validator_false_on_string_element(invalid_sudoku):
    """Test sudoku_validator returns false if element in sudoku is not an integer."""
    assert invalid_sudoku.is_valid() == False


def test_sudoku_validator_false_on_float_element(invalid_sudoku_float):
    """Test sudoku_validator returns false if element in sudoku is not an integer."""
    assert invalid_sudoku_float.is_valid() == False
