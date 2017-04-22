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
    squares_coords = {}
    candidates = {}
    dicts = rows_missing, cols_missing, squares_missing
    sq_nr = 0
    for row in range(0, square_sides ** 2, square_sides):
        for col in range(0, square_sides ** 2, square_sides):
            sq_nr += 1
            square = [islice(m[i], col, square_sides + col) for i in range(row, row + square_sides)]
            fill_given_numbers(square, row, col, sq_nr, dicts, squares_coords)
    for d in dicts:
        d = get_missing(d)
    starting_spots = get_starting_spots(m, dicts, squares_coords)
    starting_spots.sort(key=itemgetter(2)) #sort list with least amount of possibilities first
    for coordinate in starting_spots:
        candidates =  get_candidates(coordinate, candidates, dicts, squares_coords)
    return fill_sudoku(m, candidates, dicts, squares_coords)

#mapping given numbers to respective row, cols and squares
def fill_given_numbers(square, row, col, sq_nr, dicts, squares_coords):
    """Fill dicts with given numbers number for a given square."""
    rm, cm, sm = dicts
    for row_idx, sr in enumerate(square):
        for col_idx, sv in enumerate(sr):
            coord = (row + row_idx, col + col_idx)
            if sv == 0:
                squares_coords[coord] = sq_nr
                continue
            rm[coord[0]].append(sv)
            cm[coord[1]].append(sv)
            sm[sq_nr].append(sv)


def get_missing(d):
    """Return a dictionary with swapped values from given numbers to missing numbers."""
    for k, v in d.items():
        d[k] = set([1, 2, 3, 4, 5, 6, 7, 8, 9]) - set(v)
    return d


def get_starting_spots(m, dicts, squares_coords):
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
                square = squares_coords[(row, col)] - 1
                missing_numbers = len(cm[col]) + len(rm[row]) + len(sm[1 if square < 1 else square])
                starting_spots.append((row, col, missing_numbers))
    return starting_spots


def get_candidates(coordinate, candidates, dicts, squares_coords):
    """Return an updated dict of candidates for a given coordinate in the Sudoko."""
    row, col, missing = coordinate
    rm, cm, sm = dicts
    candidates[(row, col)] = [n for n in cm[col] if n in rm[row] and n in sm[squares_coords[row, col]]]
    return candidates


def find_fit(candidates):
    """Return a tuple with coordinate and value to update from a sorted
    representation of a dict."""
    fit = sorted(candidates.items(), key=lambda x: len(x[1])).pop(0)
    row, col = fit[0]
    n = fit[1].pop()
    if len(fit[1]) == 0:
        return row, col, n
    return None

def update_sudoku(fit, candidates, m, dicts, squares_coords):
    """Return an updated Sudoku and missing number dicts."""
    row, col, n = fit
    rm, cm, sm = dicts
    try:
        if m[row][col] != 0:
            raise ValueError
        m[row][col] = n
#         print('updated {0}, {1} with {2}'.format(row, col, n))
    except ValueError:
        raise ValueError('Trying to update at a coordinate that already holds a non-zero value')
    rm[row].remove(n)
    cm[col].remove(n)
    sm[squares_coords[row, col]].remove(n)
    del candidates[(row, col)]
    for k, v in candidates.items():
        if k[0] == row or k[1] == col:
            try:
                v.remove(n)
#                 print('removed {0} from {1}'.format(n, k))
            except:
#                 print('not in list')
                continue
    return candidates


def fill_sudoku(m, candidates, dicts, squares_coords):
    """Return the solved Sudoku by continously updating numbers from the list of
    candidates. If no immediate candidates, rebuild the starting spots and list
    of candidates and repeat updating process until no more candidates."""
    while True:
        try:
            if candidates:
                candidates = update_sudoku(find_fit(candidates), candidates, m, dicts, squares_coords)
                continue
            break
        except TypeError:
#             print(DataFrame(m))
#             print('Rebuilding')
            starting_spots = get_starting_spots(m, dicts, squares_coords) #Rebuilding starting spots
            starting_spots.sort(key=itemgetter(2))
            if len(starting_spots) == 0:
                break
            for coordinate in starting_spots: #rebuild candidates based off of rebuilt starting_spots
                get_candidates(coordinate, candidates, dicts, squares_coords)
            fill_sudoku(m, candidates, dicts, squares_coords)
    return m
