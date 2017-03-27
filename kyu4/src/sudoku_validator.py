"""Module to solve the code-kata https://www.codewars.com/kata/validate-sudoku-with-size-nxn."""

def extract_small_square(m, row, col):
    s = []
    total = 0
    for i in range(row, row + 3):
        slice = m[i][col:3 + col]
        s.append(slice)
    return s


def check_square(matrix, row):
    for col in range(0, 7, 3):
        square = extract_small_square(matrix, row, col)
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
    for i in range(0, 7, 3):
        try:
            if not check_square(m, i):
                return False
        except TypeError:
            return False
        except IndexError:
            return False
    return True
