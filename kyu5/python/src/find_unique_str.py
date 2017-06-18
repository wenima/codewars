"""Module to solve the code-kata https://www.codewars.com/kata/find-the-unique-string."""

from collections import defaultdict

def find_uniq(a):
    """Return the unique element from a list of strings."""
    d = {}
    c = defaultdict(int)
    for e in a:
        t = frozenset(e.strip().lower())
        d[t] = e
        c[t] += 1

    return d[next(filter(lambda k: c[k] == 1, c))]
