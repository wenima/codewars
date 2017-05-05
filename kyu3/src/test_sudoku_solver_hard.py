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

naked_pairs = [
    [4, 0, 0, 2, 7, 0, 6, 0, 0],
    [7, 9, 8, 1, 5, 6, 2, 3, 4],
    [0, 2, 0, 8, 4, 0, 0, 0, 7],
    [2, 3, 7, 4, 6, 8, 9, 5, 1],
    [8, 4, 9, 5, 3, 1, 7, 2, 6],
    [5, 6, 1, 7, 9, 2, 8, 4, 3],
    [0, 8, 2, 0, 1, 5, 4, 7, 9],
    [0, 7, 0, 0, 2, 4, 3, 0, 0],
    [0, 0, 4, 0, 8, 7, 0, 0, 2]
]

np = [1, 5]

fiendish = [
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
def fiendish_sudoku():
    from sudoku_solver import sudoku_solver
    new_sudoku = sudoku_solver(fiendish)
    return new_sudoku


def test_find_naked_pairs():
    """Given a Sudoku with naked pairs, test that funtion returns all naked
    pairs in that Sudoku."""
    from sudoku_solver_hard import find_naked_pairs, sudoku_solver
    m, candidates = sudoku_solver(naked_pairs)
    np = find_naked_pairs(candidates)
    assert sorted(np.values()) == [[1, 5], [1, 5], [1, 5], [3, 6], [8, 5], [9, 3]]

def test_solved_sudoku_validator(solved_sudoku):
    """Test solved sudoku to make sure validtor works."""
    from sudoku_validator import Sudoku
    solved_sudoku = Sudoku(solved_sudoku)
    assert solved_sudoku.is_valid() == True

def test_medium_sudoku_validator(fiendish_sudoku):
    """Test sudoku_validator returns correct result."""
    from sudoku_validator import Sudoku
    fiendish_sudoku = Sudoku(fiendish_sudoku)
    assert fiendish_sudoku.is_valid() == True
