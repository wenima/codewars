"""Module to solve the code-kata https://www.codewars.com/kata/mod4-regex.
"""

import re


def mod4(s):
    """Return True if given s contains a number divisible by 4."""
    pattern = r'.*\[([+-]?0*\d*([02468][048]|[13579][26])]|[+-]?[048]\])'
    m = re.match(pattern, s)
    return True if m else False
