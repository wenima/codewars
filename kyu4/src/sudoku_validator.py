"""Module to solve the code-kata https://www.codewars.com/kata/validate-sudoku-with-size-nxn."""

from math import sqrt

def extract_small_square(m, row, col, square_sides):
    s = []
    total = 0
    for i in range(row, row + square_sides):
        slice = m[i][col:square_sides + col]
        s.append(slice)
    return s


def check_square(matrix, row, square_sides):
    for col in range(0, square_sides * 2 + 1, square_sides):
        square = extract_small_square(matrix, row, col, square_sides)
        return validate_square(square)


def validate_square(square):
    return sum([n for l in square for n in l]) == 45


def sudoku_validator(m):
    """Validate a Sudoku puzzle of size NxN.

    Rules for validation are:
    Data structure dimension: NxN where N > 0 and √N == integer
    Rows may only contain integers: 1..N (N included)
    Columns may only contain integers: 1..N (N included)
    'Little squares' (3x3) may also only contain integers: 1..N (N included).
    """
    if len(m) % 3 != 0:
        return False
    square_sides = int(sqrt(len(m)))
    for i in range(0, square_sides * 2 + 1, square_sides):
        try:
            if not check_square(m, i, square_sides):
                return False
        except TypeError:
            return False
    return True
