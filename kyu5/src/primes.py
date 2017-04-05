"""Module to solve codewars kata https://www.codewars.com/kata/first-n-prime-numbers."""

from itertools import islice, count

class Primes(object):
    """Create Primes object to store and return prime numbers.

    Methods:
    first(n): will return a list of primes up to n.
    """

    def __init__(self):
        """Initialize a Prime object."""
        self.prime_list = []

    def _eratosthenes(self):
        """Yield primes infinitively with a modified version of Eratosthenes.
        Since we know primes can't be even, we iterate in steps of 2."""
        D = {}
        yield 2
        for q in islice(count(3), 0, None, 2):
            p = D.pop(q, None)
            if p is None:
                D[q*q] = q
                yield q
            else:
                x = q + 2*p
                while x in D:
                    x += 2*p
                D[x] = p

    def _generate_primes(self, n):
        for p in self._eratosthenes():
            self.prime_list.append(p)
            if len(self.prime_list) == n:
                break

    def first(self, n):
        self._generate_primes(n)
        return self.prime_list
