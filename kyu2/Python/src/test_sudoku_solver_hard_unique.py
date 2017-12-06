"""Tests for https://www.codewars.com/kata/hard-sudoku-solver-1."""

import pytest
from math import sqrt
from operator import itemgetter


unsolvable = [
    [5, 2, 0, 7, 9, 4, 3, 0, 8],
    [4, 6, 0, 3, 1, 8, 5, 7, 0],
    [0, 0, 0, 5, 6, 2, 4, 0, 0],
    [0, 9, 4, 6, 8, 7, 1, 0, 0],
    [7, 1, 0, 9, 3, 5, 2, 4, 6],
    [6, 3, 5, 4, 2, 1, 9, 8, 7],
    [0, 0, 0, 1, 5, 6, 8, 0, 0],
    [0, 5, 0, 8, 4, 9, 7, 2, 0],
    [9, 8, 1, 2, 7, 3, 6, 0, 4]
]

invalid = [
    [1, 2, 3, 4, 5, 6, 7, 8, 'a'], 
    [4, 0, 6, 7, 8, 9, 1, 2, 3], 
    [7, 8, 9, 1, 2, 3, 4, 5, 6], 
    [2, 3, 4, 5, 6, 7, 8, 9, 1], 
    [5, 6, 7, 8, 9, 1, 2, 3, 4], 
    [8, 9, 1, 2, 3, 4, 5, 6, 7], 
    [3, 4, 5, 6, 7, 8, 9, 1, 2], 
    [6, 7, 8, 9, 1, 2, 3, 4, 5], 
    [9, 1, 2, 3, 4, 5, 6, 7, 8]
    ]

not_unique = [
    [0, 0, 3, 4, 5, 6, 7, 8, 9], 
    [4, 5, 6, 7, 8, 9, 0, 0, 3], 
    [7, 8, 9, 0, 0, 3, 4, 5, 6], 
    [0, 3, 4, 5, 6, 7, 8, 9, 0], 
    [5, 6, 7, 8, 9, 0, 0, 3, 4], 
    [8, 9, 0, 0, 3, 4, 5, 6, 7], 
    [3, 4, 5, 6, 7, 8, 9, 0, 0], 
    [6, 7, 8, 9, 0, 0, 3, 4, 5], 
    [9, 0, 0, 3, 4, 5, 6, 7, 8]
    ]

hard_1 = [
    [0, 0, 0, 2, 0, 0, 0, 6, 3],
    [3, 0, 0, 0, 0, 5, 4, 0, 1],
    [0, 0, 1, 0, 0, 3, 9, 8, 0],
    [0, 0, 0, 0, 0, 0, 0, 9, 0],
    [0, 0, 0, 5, 3, 8, 0, 0, 0],
    [0, 3, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 6, 3, 0, 0, 5, 0, 0],
    [5, 0, 3, 7, 0, 0, 0, 0, 8],
    [4, 7, 0, 0, 0, 1, 0, 0, 0],
]

hard_2 = [
    [0, 1, 0, 0, 0, 4, 0, 0, 0],
    [0, 0, 6, 8, 0, 5, 0, 0, 1],
    [5, 0, 3, 7, 0, 1, 9, 0, 0],
    [8, 0, 4, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 3, 0, 0, 6, 0, 9],
    [0, 0, 1, 5, 0, 8, 2, 0, 4],
    [6, 0, 0, 4, 0, 3, 1, 0, 0],
    [0, 0, 0, 2, 0, 0, 0, 5, 0],
]

expert = [
    [0, 0, 6, 0, 0, 0, 0, 0, 4],
    [0, 0, 0, 8, 6, 0, 7, 3, 0],
    [0, 4, 0, 3, 5, 0, 0, 0, 2],
    [1, 7, 0, 4, 0, 0, 6, 0, 0],
    [0, 9, 0, 0, 0, 0, 0, 8, 0],
    [0, 0, 8, 0, 0, 6, 0, 1, 7],
    [2, 0, 0, 0, 8, 1, 0, 4, 0],
    [0, 6, 7, 0, 4, 3, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 3, 0, 0],
]


diabolical = [
    [3, 6, 0, 0, 0, 0, 1, 7, 0],
    [0, 1, 4, 7, 0, 0, 0, 0, 0],
    [0, 0, 7, 0, 8, 0, 0, 0, 0],
    [0, 0, 1, 2, 0, 6, 0, 0, 5],
    [9, 0, 0, 0, 0, 0, 0, 0, 4],
    [4, 0, 0, 5, 0, 8, 3, 0, 0],
    [0, 0, 0, 0, 5, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 7, 4, 3, 0],
    [0, 4, 9, 0, 0, 0, 0, 5, 6],
]


TEST_SUDOKUS = [
    (hard_1, True),
    (hard_2, True),
    (diabolical, True),
]

def test_sudoku_solver_handles_garbage_input():
    """Test that garbage input in the given sudoku is handled correctly by sudoku_solver."""
    from sudoku_solver_hard_unique import setup
    with pytest.raises(Exception) as e_info:
        candidates, dicts, square_coords = setup(invalid)
    assert str(e_info.value) == "Garbage input: 'a' at coord (0, 8), not a valid Sudoku"

def test_sudoku_solver_handles_non_unique():
    """Test that an non-unique sudoku is handled correctly by sudoku_solver."""
    from sudoku_solver_hard_unique import sudoku_solver
    with pytest.raises(Exception) as e_info:
        sudoku_solver(not_unique)
    assert str(e_info.value) == "Sudoku is not unique"

@pytest.mark.parametrize('m, result', TEST_SUDOKUS)
def test_solver_combo_approach(m, result):
    """
    Test that function solver can solve a given sudoku of hard difficulty correctly using a mix of traditional solving techniques and
    brute force.
    """
    from sudoku_solver_hard_unique import sudoku_solver, valid
    from copy import deepcopy
    brute_m = deepcopy(m)
    solved_sudoku = sudoku_solver(brute_m)
    assert valid(solved_sudoku) == result
