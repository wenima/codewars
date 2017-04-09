"""Module to solve the code-kata https://www.codewars.com/kata/not-very-secure/train/python.
The kata seems to be broken as the description state a regular expression needs
to be fixed but no regex is given.

Thus, this module offers 2 solutions, the 'pythonic' one and one using regex.
"""

import re


#pythonic

def alphanumeric_py(string):
    """Return True if the given string is alphanumeric."""
    return string.isalnum()


#regex

def alphanumeric(s):
    """Return True if given s is alphanumeric."""
    if len(s) == 0:
        return False
    pattern = r'(?=([^A-Za-z0-9]))' #using lookahead for everything not alphanumeric
    m = re.search(pattern, s)
    return False if m else True
