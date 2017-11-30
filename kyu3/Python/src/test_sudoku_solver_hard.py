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

brute_force = [
    [5, 0, 0, 7, 9, 0, 0, 0, 8],
    [0, 6, 0, 0, 1, 0, 0, 7, 0],
    [0, 0, 0, 5, 6, 2, 0, 0, 0],
    [0, 9, 4, 6, 8, 7, 1, 0, 0],
    [7, 1, 0, 9, 3, 5, 0, 4, 6],
    [6, 0, 5, 4, 2, 1, 9, 0, 7],
    [0, 0, 0, 1, 5, 6, 0, 0, 0],
    [0, 5, 0, 0, 4, 9, 0, 2, 0],
    [9, 0, 0, 2, 7, 0, 0, 0, 4]
]

np = {(1, 5): [(8, 0), (8, 7), (8, 3)]}

fiendish = [
    [3, 0, 5, 0, 2, 0, 7, 0, 1],
    [0, 0, 0, 8, 0, 3, 0, 0, 2],
    [0, 6, 0, 0, 0, 5, 0, 0, 0],
    [0, 7, 1, 0, 0, 0, 0, 5, 0],
    [0, 0, 6, 0, 0, 0, 9, 0, 0],
    [0, 9, 0, 0, 0, 0, 4, 2, 0],
    [0, 0, 0, 6, 0, 0, 0, 9, 0],
    [9, 0, 0, 5, 0, 4, 0, 0, 5],
    [6, 0, 8, 0, 3, 0, 2, 0, 4]
    ]

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

extreme = [
    [0, 0, 9, 7, 4, 8, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 1, 0, 9, 0, 0, 0],
    [0, 0, 7, 0, 0, 0, 2, 4, 0],
    [0, 6, 4, 0, 1, 0, 5, 9, 0],
    [0, 9, 8, 0, 0, 0, 3, 0, 0],
    [0, 0, 0, 8, 0, 3, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 7, 5, 9, 0, 0],
]


TEST_SUDOKUS = [
    (brute_force, True),
    (hard_1, True),
    (hard_2, True),
    (expert, True),
    (extreme, True),
    (fiendish, True),
]

TEST_FILL_SQUARES = [
    (hard_1, (((6, 0), 9), ((7, 1), 1), ((8, 2), 8)), True),
    (hard_1, (((6, 0), 8), ((7, 1), 9), ((8, 2), 1)), False),
    (hard_1, (((6, 0), 1), ((7, 1), 8), ((8, 2), 9)), False),
    (hard_2, (((6, 4), 9), ((7, 4), 1), ((8, 4), 6), ((8, 5), 7)), False),
]

@pytest.fixture
def medium_sudoku():
    new_sudoku = [
        [5, 0, 0, 0, 9, 0, 0, 0, 8],
        [0, 6, 0, 0, 1, 0, 0, 7, 0],
        [0, 0, 0, 5, 0, 2, 0, 0, 0],
        [0, 0, 4, 0, 8, 0, 1, 0, 0],
        [7, 1, 0, 9, 0, 5, 0, 4, 6],
        [0, 0, 5, 0, 2, 0, 9, 0, 0],
        [0, 0, 0, 1, 0, 6, 0, 0, 0],
        [0, 5, 0, 0, 4, 0, 0, 2, 0],
        [9, 0, 0, 0, 7, 0, 0, 0, 4]
        ]
    return new_sudoku

@pytest.fixture
def immediate_fills_dicts(medium_sudoku):
    from sudoku_solver_hard import (initialize_dicts, initialize_d,
    fill_given_numbers, populate_dicts)
    m = medium_sudoku
    # candidates, dicts, square_coords = setup(m)
    square_sides = int(sqrt(len(medium_sudoku)))
    dicts = initialize_dicts(m, square_sides)
    dicts, square_coords = populate_dicts(m, square_sides, dicts)
    return dicts, square_coords

@pytest.fixture
def immediate_fills_candidates(immediate_fills_dicts, medium_sudoku):
    from sudoku_solver_hard import get_missing, get_starting_spots, get_candidates
    m = medium_sudoku
    dicts, square_coords = immediate_fills_dicts
    dicts = get_missing(dicts)
    candidates = get_candidates(m, dicts, square_coords)
    return candidates

@pytest.fixture
def naked_sets_sudoku(medium_sudoku, immediate_fills_dicts, immediate_fills_candidates):
    from sudoku_solver_hard import scan_sudoku, fill_fit, single_candidate
    m = medium_sudoku
    dicts, square_coords = immediate_fills_dicts
    rm, cm, sm = dicts
    m, candidates = scan_sudoku(m, dicts, square_coords, immediate_fills_candidates)
    single_candidates = single_candidate(candidates, square_coords, dicts)
    m, candidates = fill_fit(m, dicts, square_coords, single_candidates=single_candidates)
    return m

@pytest.fixture
def naked_sets_dicts(naked_sets_sudoku):
    from sudoku_solver_hard import (initialize_dicts, initialize_d,
    fill_given_numbers, populate_dicts, get_missing, get_candidates)
    m = naked_sets_sudoku
    square_sides = int(sqrt(len(naked_sets_sudoku)))
    dicts = initialize_dicts(m, square_sides)
    dicts, square_coords = populate_dicts(m, square_sides, dicts)
    dicts = get_missing(dicts)
    return dicts, square_coords


def test_initialize_dicts(medium_sudoku):
    """Given a Sudoku test that dicts are initialized correctly."""
    from sudoku_solver_hard import initialize_dicts, initialize_d
    square_sides = int(sqrt(len(medium_sudoku)))
    rows_missing, cols_missing, squares_missing = initialize_dicts(medium_sudoku, square_sides)
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

def test_get_missing(medium_sudoku):
    """Test that dicts with given numbers swap with missing numbers."""
    from sudoku_solver_hard import setup, get_missing
    c, dicts, square_coords = setup(medium_sudoku)
    rows_missing, cols_missing, squares_missing = dicts
    assert rows_missing[0] == set([1, 2, 3, 4, 6, 7])
    assert cols_missing[8] == set([1, 2, 3, 5, 7, 9])
    assert squares_missing[9] == set([1, 3, 5, 6, 7, 8, 9])


def test_get_sorted_starting_spots(medium_sudoku):
    """Test that function returns best starting spots given a sudoku dicts
    and square coordinates."""
    from sudoku_solver_hard import setup, get_missing, get_starting_spots
    c, dicts, square_coords = setup(medium_sudoku)
    starting_spots = get_starting_spots(medium_sudoku, dicts, square_coords)
    starting_spots.sort(key=itemgetter(2))
    assert starting_spots[0] == (4, 4, 11)
    assert starting_spots[-1] == (2, 2, 21)

def test_get_candidates(immediate_fills_candidates):
    """Test that function returns a dict of candidates per coordinate."""
    assert immediate_fills_candidates[(4, 4)] == [3]

def test_get_candidates_account_for_naked_sets(medium_sudoku):
    """Test that function returns a dict of candidates per coordinate but omits
    numbers for coordinates from naked sets if provided."""
    from sudoku_solver_hard import setup, get_missing, get_candidates
    c, dicts, square_coords = setup(medium_sudoku)
    naked_sets = {(3, 8): [(8, 7), (8, 6), (8, 2)]}
    c = get_candidates(medium_sudoku, dicts, square_coords, naked_sets)
    assert 3, 8 not in c[(8, 6)]
    assert 3, 8 not in c[(8, 2)]
    assert 3, 8 not in c[(8, 7)]

def test_find_fit(immediate_fills_candidates):
    """Test that given a dict of candidates, a tuple is returned with coordinates
    and value to update the Sudoku."""
    from sudoku_solver_hard import find_fit
    row, col, num = find_fit(immediate_fills_candidates)
    assert row == 4 and col == 4 and num == 3

def test_fill_fit_candidates(medium_sudoku):
    """Test that given candidates with immediate fits, the Sudoku is updated correctly
    and the fill is removed from Sudoku dicts."""
    from sudoku_solver_hard import setup, fill_fit
    m = medium_sudoku
    c, dicts, square_coords = setup(m)
    rm, cm, sm = dicts
    m, candidates = fill_fit(m, dicts, square_coords, candidates=c)
    assert m[4][4] == 3
    assert m[2][4] == 6
    assert m[6][4] == 5
    assert 3 not in rm[4]
    assert (4, 4) not in candidates.keys()


def test_fill_fit_single_candidates(medium_sudoku):
    """Test that given single_candidates, the Sudoku is updated correctly and
    the fill is removed from Sudoku dicts."""
    from sudoku_solver_hard import setup, get_missing, fill_fit
    m = medium_sudoku
    c, dicts, square_coords = setup(m)
    rm, cm, sm = dicts
    single_candidates = [(7, (0, 3)), (9, (3, 1)), (6, (5, 0)), (7, (5, 8)), (9, (7, 5)), (2, (8, 3))]
    m, candidates = fill_fit(m, dicts, square_coords, single_candidates=single_candidates)
    assert m[0][3] == 7
    assert m[5][0] == 6
    assert m[8][3] == 2
    assert 7 not in rm[0]


def test_scan_sudoku(medium_sudoku, immediate_fills_candidates, immediate_fills_dicts):
    """Test that function fills in fits as long as it can find one by rebuilding
    list of candidates."""
    from sudoku_solver_hard import scan_sudoku
    m = medium_sudoku
    dicts, square_coords = immediate_fills_dicts
    m, candidates = scan_sudoku(m, dicts, square_coords, immediate_fills_candidates)
    total_zeroes = 0
    for row in m:
        total_zeroes += row.count(0)
    assert m[5][5] == 1
    assert total_zeroes == 46
    assert (5, 3) not in candidates.keys()


def test_squares_to_missing(immediate_fills_dicts):
    """Test that function returns a dict with squares as key and missing fields
    as values."""
    from sudoku_solver_hard import squares_to_missing
    dicts, square_coords = immediate_fills_dicts
    squares_missing = squares_to_missing(square_coords)
    total_missing = 0
    for v in squares_missing.values():
        total_missing += len(v)
    assert len(squares_missing.values()) == 9
    assert total_missing == 53


def test_single_candidate(medium_sudoku, immediate_fills_dicts, immediate_fills_candidates):
    """Test that function returns a fill by using the single candidate technique."""
    from sudoku_solver_hard import scan_sudoku, single_candidate
    m = medium_sudoku
    dicts, square_coords = immediate_fills_dicts
    m, candidates = scan_sudoku(m, dicts, square_coords, immediate_fills_candidates)
    single_candidates = single_candidate(candidates, square_coords, dicts)
    assert len(single_candidates) == 6
    assert (7, (0, 3)) in single_candidates


def test_build_possible_naked_sets(naked_sets_sudoku):
    """Given a Sudoku test that function returns possible naked sets."""
    from sudoku_solver_hard import setup, build_possible_naked_sets
    m = naked_sets_sudoku
    c, dicts, square_coords = setup(m)
    possible_naked_sets = build_possible_naked_sets(c)
    assert possible_naked_sets[(7, 3)] == [3, 8]
    assert possible_naked_sets[(8, 5)] == [3, 8]


def test_coords_per_naked_set(naked_sets_sudoku):
    """Given a dict of possible naked sets, test that function returns the inverted dict."""
    from sudoku_solver_hard import setup, build_possible_naked_sets, build_coords_per_naked_set
    m = naked_sets_sudoku
    c, dicts, square_coords = setup(m)
    possible_naked_sets = build_possible_naked_sets(c)
    coords_per_naked_set = build_coords_per_naked_set(possible_naked_sets)
    for k, v in coords_per_naked_set.items():
        assert len(v) == len([1 for nums in possible_naked_sets.values() if nums == list(k)])


def test_update_naked_set(naked_sets_sudoku):
    """
    Given a dict of possible naked sets and it inverse dict, test that the
    function returns an updated dict.
    """
    from sudoku_solver_hard import (setup, build_possible_naked_sets,
    build_coords_per_naked_set, update_naked_set)
    m = naked_sets_sudoku
    c, dicts, square_coords = setup(m)
    possible_naked_sets = build_possible_naked_sets(c)
    coords_per_naked_set = build_coords_per_naked_set(possible_naked_sets)
    naked_sets = update_naked_set(possible_naked_sets, coords_per_naked_set, 2)
    vals = []
    for v in naked_sets.values():
        if v not in vals: vals.append(v)
    assert len(vals) == 3


def test_find_naked_sets(naked_sets_sudoku):
    """
    Given a dict of naked sets, test that function returns a list
    of coordinates from which a naked set can be removed from
    ."""
    from sudoku_solver_hard import setup, find_naked_sets
    m = naked_sets_sudoku
    c, dicts, square_coords = setup(m)
    rows, cols = find_naked_sets(c, dicts)
    assert (8, 6) in rows[(3, 8)]
    assert (8, 2) in rows[(3, 8)]
    assert (8, 7) in rows[(3, 8)]
    assert (6, 1) in cols[(3, 8)]
    assert (0, 1) in cols[(3, 8)]
    assert (2, 1) in cols[(3, 8)]


def test_remove_naked_sets_from_candidates(naked_sets_sudoku, naked_sets_dicts):
    """
    Given a dict of naked sets, test that function returns a list
    of coordinates from which a naked set can be removed from.
    """
    from sudoku_solver_hard import (get_candidates, find_naked_sets,
    remove_naked_sets_from_candidates)
    m = naked_sets_sudoku
    dicts, square_coords = naked_sets_dicts
    c = get_candidates(m, dicts, square_coords)
    rows, cols = find_naked_sets(c, dicts)
    c = remove_naked_sets_from_candidates(c, rows, cols)
    assert 3, 8 not in c[(8, 6)]
    assert 3, 8 not in c[(8, 2)]
    assert 3, 8 not in c[(8, 7)]

def test_sudoku_solver_handles_unsolvable_sudoku():
    """Test that an unsolvable sudoku is handled correctly by sudoku_solver."""
    from sudoku_solver_hard import setup
    with pytest.raises(Exception) as e_info:
        candidates, dicts, square_coords = setup(unsolvable)
    assert str(e_info.value) == 'Sudoku not solvable at 0, 2'

@pytest.mark.parametrize('m, fit, result', TEST_FILL_SQUARES)
def test_fill_square_handles_invalid_permutations(m, fit, result):
    """Test that fill_square returns correct boolean for a given permutation."""
    from sudoku_solver_hard import setup, fill_square
    from copy import deepcopy
    brute_m = brute_m = deepcopy(m)
    candidates, dicts, square_coords = setup(m)
    assert fill_square(brute_m, candidates, fit) == result

@pytest.mark.parametrize('m, result', TEST_SUDOKUS)
def test_solver_combo_approach(m, result):
    """
    Test that function solver can solve a given sudoku of hard difficulty correctly using a mix of traditional solving techniques and
    brute force.
    """
    from sudoku_solver_hard import solver, valid
    from copy import deepcopy
    brute_m = brute_m = deepcopy(m)
    solved_sudoku = solver(brute_m)
    assert valid(solved_sudoku) == result


# def test_find_naked_pairs(naked_sets_sudoku):
#     """Given a Sudoku with naked pairs, test that funtion returns a dict with
#     a naked set as key and coords to be updated."""
#     from sudoku_solver_hard import (initialize_dicts, initialize_d,
#     fill_given_numbers, populate_dicts, get_missing, get_candidates, find_naked_sets)
#     m = naked_sets_sudoku
#     square_sides = int(sqrt(len(naked_sets_sudoku)))
#     dicts = initialize_dicts(m, square_sides)
#     dicts, square_coords = populate_dicts(m, square_sides, dicts)
#     dicts = get_missing(dicts)
#     candidates = get_candidates(m, dicts, square_coords)
#     print(candidates)
#     naked_sets_fields_row, naked_sets_fields_cols = find_naked_sets(candidates, dicts, setlength=2)
#     assert naked_sets_fields_row == {(3, 8): [(8, 7), (8, 6), (8, 2)]}
#     assert naked_sets_fields_cols == {}

#
#
# def test_find_naked_pairs():
#     """Given a Sudoku with naked pairs, test that funtion returns a dict with
#     a naked set as key and coords to be updated."""
#     from sudoku_solver_hard import find_naked_sets, sudoku_solver
#     m, candidates, dicts = sudoku_solver(naked_pairs)
#     assert find_naked_sets(candidates, dicts) == np

# def test_scan_for_fills():
#     """Given a Sudoku with naked pairs, test that funtion returns a dict with
#     a naked set as key and coords to be updated."""
#     from sudoku_solver_hard import find_naked_sets, sudoku_solver
#     m, candidates, dicts = sudoku_solver(naked_pairs)
#     assert find_naked_sets(candidates, dicts) == np
#
#
# def test_medium_sudoku_validator(fiendish_sudoku):
#     """Test sudoku_validator returns correct result."""
#     from sudoku_validator import Sudoku
#     fiendish_sudoku = Sudoku(fiendish_sudoku)
#     assert fiendish_sudoku.is_valid() == True
