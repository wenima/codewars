"""Tests for https://www.codewars.com/kata/sudoku-solver."""

import pytest
from math import sqrt
from operator import itemgetter

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

scan = [
    [5,0,0,0,9,0,0,0,8],
    [0,6,0,0,1,0,0,7,0],
    [0,0,0,5,0,2,0,0,0],
    [0,0,4,0,8,0,1,0,0],
    [7,1,0,9,0,5,0,4,6],
    [0,0,5,0,2,0,9,0,0],
    [0,0,0,1,0,6,0,0,0],
    [0,5,0,0,4,0,0,2,0],
    [9,0,0,0,7,0,0,0,4]
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

np = {(1, 5): [(8, 0), (8, 7), (8, 3)]}

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
def immediate_fills_dicts():
    from sudoku_solver_hard import (initialize_dicts, initialize_d,
    fill_given_numbers, populate_dicts)
    square_sides = int(sqrt(len(scan)))
    dicts = initialize_dicts(scan, square_sides)
    dicts, square_coords = populate_dicts(scan, square_sides, dicts)
    return dicts, square_coords

@pytest.fixture
def immediate_fills_candidates(immediate_fills_dicts):
    from sudoku_solver_hard import get_missing, get_starting_spots, get_candidates
    dicts, square_coords = immediate_fills_dicts
    dicts = get_missing(dicts)
    starting_spots = get_starting_spots(scan, dicts, square_coords)
    starting_spots.sort(key=itemgetter(2))
    candidates = get_candidates(starting_spots, dicts, square_coords)
    return candidates

@pytest.fixture
def fiendish_sudoku():
    from sudoku_solver import sudoku_solver
    new_sudoku = sudoku_solver(fiendish)
    return new_sudoku

def test_initialize_dicts():
    """Given a Sudoku test that dicts are initialized correctly."""
    from sudoku_solver_hard import initialize_dicts, initialize_d
    square_sides = int(sqrt(len(scan)))
    rows_missing, cols_missing, squares_missing = initialize_dicts(scan, square_sides)
    assert len(rows_missing) == 9
    assert len(cols_missing) == 9
    assert len(squares_missing) == 9


def test_populate_dicts(immediate_fills_dicts):
    """Given a Sudoku test that dicts to keep information about the Sudoku
    are populated correctly."""
    dicts, square_coords = immediate_fills_dicts
    rows_missing, cols_missing, squares_missing = dicts
    assert rows_missing[0] == [5, 9, 8]
    assert cols_missing[8] == [8, 6, 4]
    assert squares_missing[9] == [2, 4]

def test_get_missing(immediate_fills_dicts):
    """Test that dicts with given numbers swap with missing numbers."""
    from sudoku_solver_hard import get_missing
    dicts, square_coords = immediate_fills_dicts
    dicts = get_missing(dicts)
    rows_missing, cols_missing, squares_missing = dicts
    assert rows_missing[0] == set([1, 2, 3, 4, 6, 7])
    assert cols_missing[8] == set([1, 2, 3, 5, 7, 9])
    assert squares_missing[9] == set([1, 3, 5, 6, 7, 8, 9])


def test_get_sorted_starting_spots(immediate_fills_dicts):
    """Test that function returns best starting spots given a sudoku dicts
    and square coordinates."""
    from sudoku_solver_hard import get_missing, get_starting_spots
    dicts, square_coords = immediate_fills_dicts
    dicts = get_missing(dicts)
    starting_spots = get_starting_spots(scan, dicts, square_coords)
    starting_spots.sort(key=itemgetter(2))
    assert starting_spots[0] == (4, 4, 11)
    assert starting_spots[-1] == (2, 2, 21)


def test_get_candidates(immediate_fills_candidates):
    """Test that function returns a dict of candidates per coordinate."""
    assert immediate_fills_candidates[(4, 4)] == [3]


def test_find_fit(immediate_fills_candidates):
    """Test that given a dict of candidates, a tuple is returned with coordinates
    and value to update the Sudoku."""
    from sudoku_solver_hard import find_fit
    row, col, num = find_fit(immediate_fills_candidates)
    assert row == 4 and col == 4 and num == 3

def test_fill_fit(immediate_fills_candidates, immediate_fills_dicts):
    """Test that given candidates with immediate fits, the Sudoku is updated correctly
    and the fill is removed from Sudoku dicts."""
    from sudoku_solver_hard import (find_fit, fill_fit, update_sudoku, remove_updated_from_dicts,
    remove_from_candidates)
    m = scan
    dicts, square_coords = immediate_fills_dicts
    rm, cm, sm = dicts
    m, candidates = fill_fit(m, immediate_fills_candidates, dicts, square_coords)
    assert m[4][4] == 3
    assert m[2][4] == 6
    assert m[6][4] == 5
    assert 3 not in rm[4]
    assert (4, 4) not in candidates.keys()


def test_scan_sudoku(immediate_fills_candidates, immediate_fills_dicts):
    """Test that function fills in fits as long as it can find one by rebuilding
    list of candidates."""
    from sudoku_solver_hard import (find_fit, fill_fit, update_sudoku, remove_updated_from_dicts,
    remove_from_candidates, scan_sudoku)
    m = scan
    dicts, square_coords = immediate_fills_dicts
    m, candidates = scan_sudoku(m, dicts, square_coords, immediate_fills_candidates)
    total_zeroes = 0
    for row in m:
        total_zeroes += row.count(0)
    assert m[5][5] == 1
    assert total_zeroes == 46
    assert (5, 3) not in candidates.keys()










# def test_scan_for_fills():
#     """Given a Sudoku with naked pairs, test that funtion returns a dict with
#     a naked set as key and coords to be updated."""
#     from sudoku_solver_hard import find_naked_sets, sudoku_solver
#     m, candidates, dicts = sudoku_solver(naked_pairs)
#     assert find_naked_sets(candidates, dicts) == np
#
#
# def test_find_naked_pairs():
#     """Given a Sudoku with naked pairs, test that funtion returns a dict with
#     a naked set as key and coords to be updated."""
#     from sudoku_solver_hard import find_naked_sets, sudoku_solver
#     m, candidates, dicts = sudoku_solver(naked_pairs)
#     assert find_naked_sets(candidates, dicts) == np
#
# def test_solved_sudoku_validator(solved_sudoku):
#     """Test solved sudoku to make sure validtor works."""
#     from sudoku_validator import Sudoku
#     solved_sudoku = Sudoku(solved_sudoku)
#     assert solved_sudoku.is_valid() == True
#
# def test_medium_sudoku_validator(fiendish_sudoku):
#     """Test sudoku_validator returns correct result."""
#     from sudoku_validator import Sudoku
#     fiendish_sudoku = Sudoku(fiendish_sudoku)
#     assert fiendish_sudoku.is_valid() == True
