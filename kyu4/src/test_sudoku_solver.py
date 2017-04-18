"""Tests for https://www.codewars.com/kata/sudoku-solver."""

import pytest

m = [[5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]]
    

@pytest.fixture
def solved_sudoku():
    from sudoku_solver import sudoku_solver
    new_sudoku = sudoku_solver(m)
    return new_sudoku


def test_sudoku_validator(solved_sudoku):
    """Test sudoku_validator returns correct result."""
    from sudoku_validator import Sudoku
    valid_sudoku = Sudoku(solved_sudoku)
    assert valid_sudoku.is_valid() == True
