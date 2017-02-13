"""Module to solve the code-kata https://www.codewars.com/kata/gap-in-primes

We define 2 helper functions:

    eratosthenes2():
    calculate all the primes up to n by using the sieve of erathostenes
    algorithm. (https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)

    binary_search():
    since the start of where we look for the gap might not be a prime, binary_search
    will return the position of the nearest prime in a given list of primes.
"""


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

def gap(g, m, n):
    """Return the prime factorization of n as a string."""
    primes = eratosthenes2(n)
    pos = binary_search(primes, m)
    for i in range(pos, n):
        try:
            if primes[i+1] - primes[i] == g:
                return (primes[i], primes[i+1])
        except IndexError:
            break
