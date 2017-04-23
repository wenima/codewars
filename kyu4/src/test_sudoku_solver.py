"""Tests for https://www.codewars.com/kata/sudoku-solver."""

import pytest

base = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]

kata = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
    ]

medium = [
    [3,0,5,0,2,0,7,0,1],
    [0,0,0,8,0,3,0,0,2],
    [0,6,0,0,0,5,0,0,0],
    [0,7,1,0,0,0,0,5,0],
    [0,0,6,0,0,0,9,0,0],
    [0,9,0,0,0,0,4,2,0],
    [0,0,0,6,0,0,0,9,0],
    [9,0,0,5,0,4,0,0,5],
    [6,0,8,0,3,0,2,0,4]
    ]


@pytest.fixture
def solved_sudoku():
    from sudoku_solver import sudoku_solver
    new_sudoku = base
    return new_sudoku

@pytest.fixture
def kata_sudoku():
    from sudoku_solver import sudoku_solver
    new_sudoku = sudoku_solver(kata)
    return new_sudoku

@pytest.fixture
def medium_sudoku():
    from sudoku_solver import sudoku_solver
    new_sudoku = sudoku_solver(medium)
    return new_sudoku

def test_solved_sudoku_validator(solved_sudoku):
    """Test solved sudoku to make sure validtor works."""
    from sudoku_validator import Sudoku
    solved_sudoku = Sudoku(solved_sudoku)
    assert solved_sudoku.is_valid() == True

def test_kata_sudoku_validator(kata_sudoku):
    """Test sudoku_validator returns correct result."""
    from sudoku_validator import Sudoku
    kata_sudoku = Sudoku(kata_sudoku)
    assert kata_sudoku.is_valid() == True


def test_medium_sudoku_validator(medium_sudoku):
    """Test sudoku_validator returns correct result."""
    from sudoku_validator import Sudoku
    medium_sudoku = Sudoku(medium_sudoku)
    assert medium_sudoku.is_valid() == True
