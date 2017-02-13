"""Module to solve the code-kata https://www.codewars.com/kata/gap-in-primes

We define 2 helper functions:

    eratosthenes2():
    calculate all the primes up to n by using the sieve of erathostenes
    algorithm. (https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)

    binary_search():
    since the start of where we look for the gap might not be a prime, binary_search
    will return the position of the nearest prime in a given list of primes.
"""


from itertools import tee, islice
from bisect import bisect_left

def eratosthenes2(n):
    """Calculate all the primes up to square root of n (rounded up)."""
    multiples = set()
    primes = []
    for i in range(2, n+1):
        if i not in multiples:
            primes.append(i)
            multiples.update(range(i*i, n+1, i))
    return primes

def binary_search(a, x, lo=0, hi=None):
    """Return the nearest element from iterable a."""
    hi = hi if hi is not None else len(a)
    pos = bisect_left(a,x,lo,hi)
    return pos

def pairwise(iterable):
    "Return a tuple of pairwise iteration."""
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def gap(gap, m, n):
    """Return the first pair of primes which has the desired gap."""
    primes = eratosthenes2(n)
    for p in pairwise(islice(primes, binary_search(primes, m), None)):
        p1, p2 = p
        if p2 - p1 == gap:
            return [p1, p2]
