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
        self.size = 0
        if matrix:
            self.size = len(matrix)
            self.m = matrix
            self.square_sides = int(sqrt(len(matrix)))
        self.nums = {x for x in range(1, len(self.m))}

    def _extract_small_square(self, row, col):
        return [islice(self.m[i], col, self.square_sides + col) for i in range(row, row + self.square_sides)]

    def _check_square(self, row):
        for col in range(0, self.square_sides * 2, self.square_sides):
            square = self._extract_small_square(row, col)
            return self._validate_square(square)

    def _validate_square(self, square):
        sum_square = sum([n for l in square for n in l])
        sum_expected = sum([n for n in range(1, self.size + 1)])
        return sum_square == sum_expected

    def is_valid(self):
        """Validate a Sudoku puzzle of size NxN."""
        for row in self.m:
            if self.nums - set(row): return False #check all rows for valid numbers
        for i in range(len(self.m)): # check all cols for valid numbers
            nums = set()
            for j in range(len(self.m)):
                nums.add(self.m[j][i])
            if self.nums - set(nums): return False
        for l in self.m:        #because True is mask for 1
            for n in l:
                if isinstance(n, bool):
                    return False
        for i in range(0, 1 if self.square_sides == 1 else self.square_sides * 2, self.square_sides):
            try:
                self._check_square(i)
            except TypeError:
                return False
        return True
