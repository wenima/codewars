"""Solution for kata https://www.codewars.com/kata/next-bigger-number-with-the-same-digits."""


def next_bigger(n):
    """Takes a positive integer and returns the next bigger number formed using
    the same digits. If no bigger number can be formed, return -1."""
    pass

def is_biggest(n):
    """Return True if given n is already the biggest number possible to be formed
    of n's digits."""
    return -1 if int(''.join(sorted([d for d in str(n)], reverse=True))) == n else 0
