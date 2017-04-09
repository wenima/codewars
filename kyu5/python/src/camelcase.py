"""Module to solve the code-kata https://www.codewars.com/kata/convert-string-to-camel-case/python.
"""

import re


def to_camel_case(s):
    """Return True if given s contains a number divisible by 4."""
    pattern = r'(?:\_|\-)[a-zA-Z]'
    m = re.findall(pattern, s)
    new_s = s
    for find in m:
        new_s = re.sub(find, find[-1].upper(), new_s)
    return new_s
