"""
Solution for code-kata https://www.codewars.com/kata/hard-sudoku-solver
This version contains less code than the original solution I came up with as implementing the
naked pairs/set/quads strategy increased the run time slightly while adding more complexity so it won't be included
in the final submission on codewars.
For the CW submission, the pre-set version of Python is 2.7.6 so this code targets that version.
"""

from math import sqrt, ceil
from itertools import islice, chain, groupby, permutations, takewhile
from operator import itemgetter
from collections import defaultdict, Counter
from functools import reduce
from copy import deepcopy

def initialize_dicts(m, square_sides):
    """Return a tuple of dicts for a given matrix and the size of the sudoku."""
    rows_missing = defaultdict(list)
    rows_missing = initialize_d(rows_missing, square_sides)
    cols_missing = defaultdict(list)
    cols_missing = initialize_d(cols_missing, square_sides)
    squares_missing = defaultdict(list)
    squares_missing = initialize_d(cols_missing, square_sides, 1)
    return rows_missing, cols_missing, squares_missing

def initialize_d(d, square_sides, offset=0):
    """Return an initialized dict so empty rows or columns in the Sudoku are
    correctly handled."""
    return {key:[] for key in range(offset, square_sides ** 2 + offset)}

def populate_dicts(m, square_sides, dicts):
    """Return dicts holding information about fills in given Sudoku."""
    sq_nr = 0
    square_coords = {}
    for row in range(0, square_sides ** 2, square_sides):
        for col in range(0, square_sides ** 2, square_sides):
            sq_nr += 1
            square = [islice(m[i], col, square_sides + col) for i in range(row, row + square_sides)]
            dicts, square_coords = fill_given_numbers(square, row, col, sq_nr, dicts, square_coords)
    return dicts, square_coords

def get_candidates(m, dicts, square_coords):
    """Return a dict of candidates for all starting_spots in the Sudoku."""
    starting_spots = get_starting_spots(m, dicts, square_coords)
    starting_spots.sort(key=itemgetter(2))
    rm, cm, sm = dicts
    c = {}
    for coordinate in starting_spots:
        row, col, missing = coordinate
        c[(row, col)] = [n for n in cm[col] if n in rm[row] and n in sm[square_coords[row, col]]]
        if not c[(row, col)]:
            raise ValueError
    return c

def get_starting_spots(m, dicts, square_coords):
    """Return a list with coordinates as starting point for sudoku solver."""
    rm, cm, sm = dicts
    starting_spots = []
    row = 0
    col = 0
    max = 20
    start = -1
    for col in range(9):
        for row in range(9):
            if m[row][col] == 0:
                square = square_coords[(row, col)] - 1
                missing_numbers = len(cm[col]) + len(rm[row]) + len(sm[1 if square < 1 else square])
                starting_spots.append((row, col, missing_numbers))
    return starting_spots


def setup(m):
    """
    Return a list of candidates, helper_dicts and square_coords
    Store all starting numbers by looping through the Sudoku square by square
    Find all missing numbers by subtracting the 2 sets
    Generate all starting spots and find the one with the least amount of digits missing
    Generate candidates by finding all possible numbers for a given starting point
    """
    square_sides = int(sqrt(len(m)))
    dicts = initialize_dicts(m, square_sides)
    dicts, square_coords = populate_dicts(m, square_sides, dicts)
    dicts = get_missing(dicts)
    try:
        candidates = get_candidates(m, dicts, square_coords)
    except ValueError as e:
        raise ValueError(e)
    return candidates, dicts, square_coords


def get_missing(dicts):
    """Return dictionaries with swapped values from given numbers to missing numbers."""
    for d in dicts:
        for k, v in d.items():
            d[k] = set([1, 2, 3, 4, 5, 6, 7, 8, 9]) - set(v)
    return dicts


def sudoku_solver(m, setup_return):
    """
    Return a valid Sudoku for a given matrix, helper dicts, a list of candidates and a lookup for coords matching squares.
    Fill in simple numbers using scanning technique
    Find single candidates and fill in
    Look for naked pairs and eliminate from candidates
    Look for naked sets and eliminate from candidates
    """
    candidates, dicts, square_coords = setup_return
    m = scan_sudoku(m, setup(m))
    if candidates:
        single_candidates = single_candidate(setup(m))
    else:
        return m
    m = fill_fit(m, setup(m), single_candidates=single_candidates)
    candidates = get_candidates(m, dicts, square_coords)
    return m


def scan_sudoku(m, setup_return):
    """
    Return an updated Sudoku and a list of candidates akin to the scanning technique where obvious fits are filled in.
    After each fit, list of candidates is rebuild until no further immediate fills are possible.
    """
    candidates, dicts, square_coords = setup_return
    while True:
        if len(sorted(candidates.items(), key=lambda x: len(x[1])).pop(0)[1]) > 1: # no longer easily solvable
            break
        m = fill_fit(m, setup(m))
        starting_spots = get_starting_spots(m, dicts, square_coords)
        starting_spots.sort(key=itemgetter(2))
        candidates = get_candidates(m, dicts, square_coords)
        if not candidates: break
    return m


def single_candidate(setup_return):
    """
    Return a number which is a single candidate for a coordinate in the list of candidates:
    Build a dict with square as key and empty fields as value
    Go through every square and get all missing fields
    For every missing field in that square, get the possible numbers
    Look for a number which is only missing in one field in a square.
    """
    candidates, dicts, square_coords = setup_return
    rm, cm, sm = dicts
    out = []
    coords_missing_in_square = squares_to_missing(square_coords)
    for k, v in coords_missing_in_square.items():
        single_candidates = defaultdict(list)
        seen = set()
        for coord in v:
            pn = set(candidates[coord])
            if pn.issubset(seen):
                continue
            for n in pn:
                if n in seen:
                    continue
                if single_candidates.get(n, 0):
                    seen.add(n)
                    continue
                single_candidates[n] = coord
        if len(seen) == len(sm[k]):
            continue
        out.append([(k, v) for k, v in single_candidates.items() if k not in seen])
    return list(chain.from_iterable(out))


def squares_to_missing(square_coords):
    """Return a dict of square numbers as key and empty fields in the Sudoku as values."""
    squares_missing = defaultdict(list)
    for k, v in square_coords.items():
        squares_missing[v].append(k)
    return squares_missing


def fill_given_numbers(square, row, col, sq_nr, dicts, sq):
    """Fill dicts with given numbers number for a given square."""
    rm, cm, sm = dicts
    for row_idx, sr in enumerate(square):
        for col_idx, sv in enumerate(sr):
            coord = (row + row_idx, col + col_idx)
            if sv == 0:
                sq[coord] = sq_nr
                continue
            rm[coord[0]].append(sv)
            cm[coord[1]].append(sv)
            sm[sq_nr].append(sv)
    return dicts, sq


def fill_fit(m, setup_return, single_candidates=[]):
    """
    Return an updated Sudoku by either finding a fit or taking a fit from a provided
    list of fits and filling it in as long as a fit is found.
    """
    candidates, dicts, square_coords = setup_return
    while True:
        try:
            if single_candidates:
                num, coord = single_candidates.pop()
                fit = (coord[0], coord[1], num)
            else:
                fit = find_fit(candidates)
        except IndexError:
            return m
        if fit:
            m = update_sudoku(fit, m)
            candidates, dicts, square_coords = setup(m)
        else:
            return m


def find_fit(candidates):
    """Return a tuple with coordinate and value to update from a sorted
    representation of a dict. If no fit can be found, return None."""
    fit = sorted(candidates.items(), key=lambda x: len(x[1])).pop(0)
    row, col = fit[0]
    n = fit[1].pop()
    if len(fit[1]) == 0:
        return row, col, n
    return None


def update_sudoku(fit, m):
    """Return an updated Sudoku."""
    row, col, n = fit
    m[row][col] = n
    return m


def fill_square(brute_m, candidates, sq_p):
    """
    Return True if all coordinates an be filled with a given permutation without invalidating the sudoku.
    Else return False.
    """
    for fit in sq_p:
        coord, n = fit
        if n not in candidates[coord]: return False
        row, col = coord
        brute_m = update_sudoku((row, col, n), brute_m)
    return True


def solver(m):
    """Return a solved Sudoku for a given Sudoku or raise a ValueError if not solvable."""
    medium_m = sudoku_solver(list(m), setup(m))
    if valid(medium_m):
        return m #Sudoku solved after the first run
    return rec_solver(medium_m)


def rec_solver(m):
    """Return a sudoku by recursively calling itself which triggers the next brute force of a square."""
    candidates, dicts, sq = setup(m)
    rm, cm, sm = dicts
    square, coords = sorted(squares_to_missing(sq).items(), key = lambda x: len(x[1]), reverse=True).pop()
    missing = sm[square]
    for p in permutations(missing):  #try all combinations of fields and missing numbers
        candidates, dicts, square_coords = setup(m)
        sq_p = tuple(zip(coords, p))
        brute_m = deepcopy(m)
        if not fill_square(brute_m, candidates, sq_p):
            continue
        try:
            brute_m = sudoku_solver(list(brute_m), setup(m))
        except ValueError as e:
            continue
        if not valid(brute_m):
            brute_m = rec_solver(brute_m)
            if not brute_m:
                continue
        return brute_m


def valid(board):
    """Retrun True if the given matrix is a valid and solved sudoku."""
    sq = int(sqrt(len(board)))
    size = sq * sq
    rows = board
    cols = [map(lambda x: x[i], board) for i in range(9)]   
    squares = [reduce(lambda x, y: x + y, map(lambda x: x[i:(i + sq)], board[j:(j + sq)]))  
                     for j in range(0, size, sq)  
                     for i in range(0, size, sq)]
    
    for clusters in (rows, cols, squares):
        for cluster in clusters:
            if len(set(cluster)) != 9:
                return False
    return True