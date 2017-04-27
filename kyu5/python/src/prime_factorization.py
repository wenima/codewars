"""Module to solve https://www.codewars.com/kata/prime-factorization."""

from collections import defaultdict


class PrimeFactorizer:

    @staticmethod
    def prime_factors(n):
        """Return a list of prime factors for a given number in ascending order."""
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


    @staticmethod
    def factor(n):
        """Return a dict where key is the prime and value the number of occurences
        in the prime factorization of n."""
        prime_factors = PrimeFactorizer.prime_factors(n)
        d = defaultdict(int)
        for pf in prime_factors:
            d[pf] += 1
        return d
