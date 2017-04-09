"""Module to solve the code-kata https://www.codewars.com/kata/base-2/train/python."""


def to_nega_binary(n):
    """Return a string representation of the negabinary value of given n."""
    res = []
    while i != 0:
        remainder = abs(i) % 2
        res.append(str(remainder))
        if i < 0 and remainder:
            i -= 1
        i = math.trunc(i / -2)
    return ''.join(reversed(res)) if res else '0'


def from_nega_binary(bin):
    """Return an integer for a given string representation of a binary in base-2."""
    return sum([pow(-2, idx) for idx, bit in enumerate(reversed(s)) if bit == '1'])
