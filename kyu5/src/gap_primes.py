"""Module to solve the code-kata https://www.codewars.com/kata/gap-in-primes

We define 2 helper functions:

    rwh_primes1():
    calculate all the primes up to n by using the sieve of erathostenes
    algorithm. (https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)

    binary_search():
    since the start of where we look for the gap might not be a prime, binary_search
    will return the position of the nearest prime in a given list of primes.

    pairwise():
    returns a tuple of pairwise iteration of.
"""


from itertools import tee, islice, compress
from bisect import bisect_left

def rwh_primes1(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + list(compress(range(3,n,2), sieve[1:]))

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
    primes = rwh_primes1(n + 1)
    for p in pairwise(islice(primes, binary_search(primes, m), None)):
        p1, p2 = p
        if p2 - p1 == gap:
            return [p1, p2]
