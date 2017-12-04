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

invalid_m_not_symmetric = [
  [1,2,3,4,5],
  [1,2,3,4],
  [1,2,3,4],
  [1]
]

four_by_four = [
    [1,4, 2,3],
    [3,2, 4,1],
    [4,1, 3,2],
    [2,3, 1,4]
]

one_by_one = [
    [1]
]

one_value_true = [
    [True]
]

valid_2 = [
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

@pytest.fixture
def invalid_sudoku_not_symmetric():
    from sudoku_validator import Sudoku
    new_sudoku = Sudoku(invalid_m_not_symmetric)
    return new_sudoku

@pytest.fixture
def valid_sudoku_4x4():
    from sudoku_validator import Sudoku
    new_sudoku = Sudoku(four_by_four)
    return new_sudoku

@pytest.fixture
def valid_sudoku_1x1():
    from sudoku_validator import Sudoku
    new_sudoku = Sudoku(one_by_one)
    return new_sudoku

@pytest.fixture
def ivalid_sudoku_true():
    from sudoku_validator import Sudoku
    new_sudoku = Sudoku(one_value_true)
    return new_sudoku


def test_sudoku_validator_4x4(valid_sudoku_4x4):
    """Test sudoku_validator returns correct result."""
    assert valid_sudoku_4x4.is_valid() == True


def test_sudoku_validator_1x1(valid_sudoku_1x1):
    """Test sudoku_validator returns correct result."""
    assert valid_sudoku_1x1.is_valid() == True


def test_sudoku_validator_false_on_string_element(invalid_sudoku):
    """Test sudoku_validator returns false if element in sudoku is not an integer."""
    assert invalid_sudoku.is_valid() == False


def test_sudoku_validator_false_on_float_element(invalid_sudoku_float):
    """Test sudoku_validator returns false if element in sudoku is not an integer."""
    assert invalid_sudoku_float.is_valid() == False

def test_sudoku_validator_false_not_symmetric(invalid_sudoku_not_symmetric):
    """Test sudoku_validator returns false if element in sudoku is not an integer."""
    assert invalid_sudoku_not_symmetric.is_valid() == False

def test_sudoku_validator_false_bool_as_value(ivalid_sudoku_true):
    """Test sudoku_validator returns false if element in sudoku is not an integer."""
    assert ivalid_sudoku_true.is_valid() == False

def test_sudoku_validator_valid_2():
    """Test sudoku_validator returns correct result."""
    from sudoku_validator import Sudoku
    s = Sudoku(valid_2)
    assert s.is_valid() == True

def test_sudoku_validator():
    """Test sudoku_validator returns correct result."""
    from sudoku_validator import Sudoku
    s = Sudoku(invalid_last_column)
    assert s.is_valid() == False
