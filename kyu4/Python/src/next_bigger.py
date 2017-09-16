"""Solution for kata https://www.codewars.com/kata/next-bigger-number-with-the-same-digits."""

from itertools import permutations, islice

def next_bigger(n):
    """Takes a positive integer and returns the next bigger number formed using
    the same digits by cutting the number at a certain index, creating sorted permutations
    and compare permutations until next bigger number is found. Checks before if a
    next bigger number can be formed by a simple swap of last 2 digits. If no
    bigger number can be formed, return -1."""
    if is_biggest(n):
        return -1
    sn = str(n)
    idx = cut_number(n)
    slice_at = len(sn) - idx - 1
    if idx == 1:
        out = [sn[-1], sn[-2]]
        return int(''.join([d for d in islice(sn, slice_at)] + out))
    slice = sn[slice_at:]
    n = int(''.join([d for d in slice]))
    next_bigger_num = n * 10
    for pn in sorted(permutations(slice), reverse=True):
        num_pn = int(''.join([d for d in pn]))
        if num_pn <= n:
            return int(''.join([d for d in islice(sn, slice_at)] + out))
        if n < num_pn < next_bigger_num:
            next_bigger_num = num_pn
            out = [d for d in pn]


def cut_number(n):
    """Return an index at which to cut the number to limit permutations to only
    those necessary."""
    i = 0
    while True:
        cur = n % 10
        ahead = n // 10 % 10
        if cur > ahead:
            i += 1
            break
        i += 1
        n //= 10
    return i


def is_biggest(n):
    """Return True if given n is already the biggest number possible to be formed
    of n's digits."""
    return True if int(''.join(sorted([d for d in str(n)], reverse=True))) == n else False
