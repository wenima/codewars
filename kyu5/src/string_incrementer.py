"""Module to solve the code-kata https://www.codewars.com/kata/string-incrementer"""

import re


def string_increment(s):
    """Return a string with the number at the end of the string incremented by 1.
    If no number exists at the end of the string, add 1."""

    pattern = r'[0-9]+$'

    m = re.search(pattern, s)

    return s[:m.start()] + str(int(m.group()) + 1).zfill(len(m.group())) if m else s + '1'
