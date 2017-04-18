"""Module to solve the code-kata https://www.codewars.com/kata/sudoku-solver."""

def sudoku_solver(m):
    """Return a valid Sudoku for a given matrix."""
    pass

square_sides = int(sqrt(len(m)))
all_rows_missing = {}
all_cols_missing = {}
all_squares_missing = {}

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
            all_squares_missing[sq_nr] = missing_sq(square)


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
        all_rows_missing[row_nr] = missing_row(row)

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
        all_cols_missing[i] = missing
