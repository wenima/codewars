"""Module to solve codewars kata https://www.codewars.com/kata/first-n-prime-numbers."""

from itertools import islice, count

class Primes(object):
    """Create Primes object to store and return prime numbers.

    Methods:
    _eratosthenes(): generate primes infinitely
    _generate_primes: call _eratosthenes and fill up list until n elements
    first(n): will return a list of primes up to n.
    """

    @staticmethod
    def _eratosthenes():
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

    @staticmethod
    def _generate_primes(n):
        """Return a list of primes which is of length n by yielding next prime from
        eratosthenes function."""
        prime_list = []
        for p in Primes._eratosthenes():
            prime_list.append(p)
            if len(prime_list) == n:
                break
        return prime_list

    @classmethod
    def first(self, n):
        """Return the list containing n primes."""
        prime_list = Primes._generate_primes(n)
        return prime_list
