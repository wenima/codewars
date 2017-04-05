"""Module to solve codewars kata https://www.codewars.com/kata/first-n-prime-numbers."""

class Primes(object):
    """Create Primes object to store and return prime numbers.

    Methods:
    first(n): will return a list of primes up to n.
    """

    def __init__(self):
        """Initialize a Prime object."""
        self.prime_list = []

    def _eratosthenes(self, n):
        """Return all primes up to and including n if n is a prime
        Since we know primes can't be even, we iterate in steps of 2."""
        if n >= 2:
            yield 2
        multiples = set()
        for i in range(3, n+1, 2):
            if i not in multiples:
                yield i
                multiples.update(range(i*i, n+1, i))

    def _generate_primes(self, n):
        self.prime_list = [p for p in self._eratosthenes(n)]

    def first(self, n):
        _generate_primes(n)
        return self.prime_list
