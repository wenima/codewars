"""Module to solve the code-kata https://www.codewars.com/kata/find-the-unique-string."""


def find_uniq(arr):
    """Return the unique element from a list of strings."""
    for idx, e in enumerate(arr):
        out = [set(e.lower()) - set(n.lower()) for n in arr if set(e.lower()) - set(n.lower())]
        if len(out) > 1: return arr[idx]
