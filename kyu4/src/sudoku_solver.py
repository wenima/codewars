"""Module to solve the code-kata https://www.codewars.com/kata/sudoku-solver."""

from math import sqrt, ceil
from itertools import islice
from operator import itemgetter

def sudoku_solver(m):
    """Return a valid Sudoku for a given matrix."""
    pass

square_sides = int(sqrt(len(m)))
rows_missing = {}
cols_missing = {}
squares_missing = {}

#finding missing numbers for square
def missing_sq(square):
    """Return the missing number for a given square."""
    missing = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for row_idx, sr in enumerate(square):
        for col_idx, sv in enumerate(sr):
            try:
                missing.remove(sv)
            except ValueError:
                continue
    return missing

def initalize_missing_numbers_squares(m):
    """Fill a dictionary intitally with all missing numbers in the matrix."""
    sq_nr = 0
    for row in range(0, square_sides ** 2, square_sides):
        for col in range(0, square_sides ** 2, square_sides):
            sq_nr += 1
            square = [islice(m[i], col, square_sides + col) for i in range(row, row + square_sides)]
            squares_missing[sq_nr] = missing_sq(square)


#finding missing rows
def missing_row(row):
    """Return the missing numbers from a given row."""
    missing = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for rv in row:
        try:
            missing.remove(rv)
        except ValueError:
            continue
    return missing

def initalize_missing_numbers_rows(m):
    """Fill a dictionary initially with all missing numbers for all rows of given matrix."""
    for row_nr, row in enumerate(m):
        rows_missing[row_nr] = missing_row(row)

#finding missing cols
def missing_col(col):
    """Return the missing numbers from a given col."""
    missing = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        try:
            missing.remove(m[i][col])
        except ValueError:
            continue
    return missing

def initalize_missing_numbers_cols(m):
    """Fill a dictionary initially with all missing numbers for all cols of given matrix."""
    for i in range(9):
        missing = missing_col(i)
        cols_missing[i] = missing


def get_square_nr(row, col):
    """Return the square number in the Sudoku starting top left being 0 based
    on given row and column."""
    if col < 3:
        if row // 3 == 0:
            square_nr = 1
        elif row // 3 == 1:
            square_nr = 4
        elif row // 3 > 1:
            square_nr = 7
    elif 2 < col < 6:
        if row // 3 == 0:
            square_nr = 2
        elif row // 3 == 1:
            square_nr = 5
        elif row // 3 > 1:
            square_nr = 8
    else:
        if row // 3 == 0:
            square_nr = 3
        elif row // 3 == 1:
            square_nr = 6
        elif row // 3 > 1:
            square_nr = 9
    return square_nr


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
