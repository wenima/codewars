"""Module to solve the code-kata https://www.codewars.com/kata/not-very-secure/train/python.
"""

import re


def alphanumeric(s):
    """Return True if given s is alphanumeric."""
    pattern = r'(?=([^A-Za-z0-9]))'
    m = re.search(pattern, s)
    if len(s) == 0:
        return False
    else:
        return False if m else True
