"""Module to solve the code-kata https://www.codewars.com/kata/validate-sudoku-with-size-nxn."""

from math import sqrt
from itertools import islice

class Sudoku(object):

    """Create a Sudoku object.

    Methods:
        is_valid(): Check if the Sudoku object is valid

    Rules for validation are:
    Data structure dimension: NxN where N > 0 and √N == integer
    Rows may only contain integers: 1..N (N included)
    Columns may only contain integers: 1..N (N included)
    'Little squares' (3x3) may also only contain integers: 1..N (N included).
    """
    def __init__(self, matrix=None):
        self.m = None
        self.square_sides = 0
        if matrix:
            self.m = matrix
            self.square_sides = int(sqrt(len(matrix)))

    def _extract_small_square(self, row, col):
        return [islice(self.m[i], col, self.square_sides + col) for i in range(row, row + self.square_sides)]

    def _check_square(self, row):
        for col in range(0, self.square_sides * 2 + 1, self.square_sides):
            square = self._extract_small_square(row, col)
            return self._validate_square(square)

    def _validate_square(self, square):
        return sum([n for l in square for n in l]) == 45

    def is_valid(self):
        """Validate a Sudoku puzzle of size NxN."""
        for i in range(0, self.square_sides * 2 + 1, self.square_sides):
            try:
                if not self._check_square(i):
                    return False
            except TypeError:
                return False
        return True
