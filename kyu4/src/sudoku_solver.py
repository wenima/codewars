"""Module to solve the code-kata https://www.codewars.com/kata/sudoku-solver."""

from math import sqrt, ceil
from itertools import islice
from operator import itemgetter
from collections import defaultdict

def sudoku_solver(m):
    """Return a valid Sudoku for a given matrix."""
    square_sides = int(sqrt(len(m)))
    rows_missing = defaultdict(list)
    cols_missing = defaultdict(list)
    squares_missing = defaultdict(list)
    squares_coords = defaultdict(list)
    dicts = rows_missing, cols_missing, squares_missing
    sq_nr = 0
    for row in range(0, square_sides ** 2, square_sides):
        for col in range(0, square_sides ** 2, square_sides):
            sq_nr += 1
            square = [islice(m[i], col, square_sides + col) for i in range(row, row + square_sides)]
            fill_given_numbers(square, row, col, sq_nr)
    for d in dicts:
        d = get_missing(d)
    candidates = {}
    starting_spots = get_starting_spots(m)
    starting_spots.sort(key=itemgetter(2))
    for coordinate in starting_spots:
        get_candidates(coordinate, candidates, rows_missing, cols_missing, squares_missing)
    while True:
        try:
            update_sudoku(find_fit(candidates), candidates, m, rows_missing, cols_missing, squares_missing)
        except TypeError:
            starting_spots = get_starting_spots(m) #rebuilding the starting spots
            starting_spots.sort(key=itemgetter(2))
            if len(starting_spots) == 0: #run until all spaces have been filled
                break
            for coordinate in starting_spots: #rebuild candidates based off of rebuilt starting_spots
                get_candidates(coordinate, candidates, rows_missing, cols_missing, squares_missing)
            run()
    return m

#mapping given numbers to respective row, cols and squares
def fill_given_numbers(square, row, col, sq_nr):
    """Fill dicts with given numbers number for a given square."""
    for row_idx, sr in enumerate(square):
        for col_idx, sv in enumerate(sr):
            coord = (row + row_idx, col + col_idx)
            squares_coords[sq_nr].append(coord)
            rows_missing[coord[0]].append(sv)
            cols_missing[coord[1]].append(sv)
            squares_missing[sq_nr].append(sv)


def get_missing(d):
    """Return a dictionary with swapped values from given numbers to missing numbers."""
    for k, v in d.items():
        d[k] = set([1, 2, 3, 4, 5, 6, 7, 8, 9]) - set(v)
    return d


def get_square_nr(square_coords, row, col):
    """Return the square number in the Sudoku starting top left being 1 based
    on given row and column. If row and column cannot be located, return -1."""
    target = (row, col)
    for k, v in square_coords.items():
        for coord in v:
            if coord == target:
                return k
    return -1


def get_starting_spots(m, rows_missing, squares_missing):
    """Return a sorted list with coordinates as starting point for sudoku solver."""
    starting_spots = []
    row = 0
    col = 0
    max = 20
    start = -1
    for col in range(9):
        for row in range(9):
            if m[row][col] == 0:
                square = get_square_nr(row, col) - 1
                missing_numbers = len(cols_missing[col]) + len(rows_missing[row])
                + len(squares_missing[1 if square < 1 else square])
                starting_spots.append((row, col, missing_numbers))
    return starting_spots.sort(key=itemgetter(2))


def get_candidates(coordinate, candidates, rows_missing, cols_missing, squares_missing):
    """Return an updated dict of candidates for a given coordinate in the Sudoko."""
    row, col, missing = coordinate
    rm = rows_missing[row]
    sm = squares_missing[get_square_nr(row, col)]
    candidates[(row, col)] = [n for n in cols_missing[col] if n in rm and n in sm]
    return candidates

def update_sudoku(coordinate, candidates, m, rows_missing, cols_missing, squares_missing):
    """Return an updated Sudoku and missing number dicts."""
    if len(candidates[(row, col)]) == 1:
    n = candidates[(row, col)].pop()
    m[row][col] = n
    rows_missing[row].remove(n)
    cols_missing[col].remove(n)
    squares_missing[get_square_nr(row, col)].remove(n)
