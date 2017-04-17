"""Solution for kata https://www.codewars.com/kata/next-bigger-number-with-the-same-digits."""

from itertools import permutations

def next_bigger(n):
    """Takes a positive integer and returns the next bigger number formed using
    the same digits. If no bigger number can be formed, return -1."""
    if is_biggest(n):
        return -1
    sn = str(n)
    for pn in permutations(sn, len(sn)):
        num_pn = int(''.join([d for d in pn]))
        if num_pn > n:
            return num_pn
            

def is_biggest(n):
    """Return True if given n is already the biggest number possible to be formed
    of n's digits."""
    return True if int(''.join(sorted([d for d in str(n)], reverse=True))) == n else False
