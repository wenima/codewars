"""Module to solve https://www.codewars.com/kata/prime-factorization."""

from collections import defaultdict


class PrimeFactorizer(int):

    def __init__(self, n):
        """Initialize a Prime object."""


    def prime_factors(self):
        """Return a list of prime factors for a given number in ascending order."""
        n = self
        factors = []
        p = 2
        if n < 2:
            return factors
        while n >= (p * p):
            if n % p:
                p += 1
            else:
                n = n // p
                factors.append(p)
        factors.append(n)
        return factors

    @property
    def factor(self):
        """Return a dict where key is the prime and value the number of occurences
        in the prime factorization of n."""
        prime_factors = PrimeFactorizer.prime_factors(self)
        d = defaultdict(int)
        for pf in prime_factors:
            d[pf] += 1
        return dict(d)
