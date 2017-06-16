"""Module to solve the code-kata https://www.codewars.com/kata/best-travel/train/python."""

from itertools import combinations

def choose_best_sum(t, k, ls):
    """Return a value closest to, but not great than, t out of a combination of
    elements in ls with size k.
    """
    best = 0
    for c in combinations(ls, k):
        if best < sum(c) <= t:
            best = sum(c)
    return best if best else None
