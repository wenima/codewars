"""Module to solve the code-kata https://www.codewars.com/kata/primes-in-numbers

We define a helper functions to yield the next prime:

    eratosthenes2():
    calculate all the primes up to square root of n (rounded up) by using the
    sieve of erathostenes algorithm. (https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)
"""

from math import sqrt, ceil

def eratosthenes2(n):
    """Calculate all the primes up to square root of n (rounded up)."""
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, n+1, i))


def primeFactors(n):
    """Return the prime factorization of n as a string."""
    divisors = []
    prime_factors = []
    m = n
    for p in eratosthenes2(int(ceil(sqrt(n)))):
        if m == 1:
            break
        while True:
            if m % p != 0:
                break
            m = m // p
            prime_factors.append(p)
            divisors.append(m)
            if m == n:
                break
    if not prime_factors:
        return "({0})".format(n)
    pf = [(upf, prime_factors.count(upf)) for upf in sorted(set(prime_factors))]
    if len(pf) == 1 and m > 1:
        if pf[0][1] == 1:
            return "({0})({1}))".format(pf[0][0], m)
    return ''.join(["({0}**{1})".format(t[0], t[1]) if t[1] > 1 else "({0})".format(t[0]) for t in pf])
