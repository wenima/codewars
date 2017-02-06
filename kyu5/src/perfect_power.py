"""Module to solve the code-kata https://www.codewars.com/kata/whats-a-perfect-power-anyway/python

We assume that if all divisors are known then k must be a prime.
In a first attempt, the algorithm iterates through all the divisors it came to
know during prime factorization and uses each and iterates through the list of
primes for k.

If this does not solve for m and k then we check if n is indeed a perfect power
by calling the function gcd_greater_one. The algorithm then solves for m and k by
running through each series of each prime factor excluding 2 and iterating over
all primes for k as long as the result of m**k is smaller than n.

We define a few helper functions:

    eratosthenes2():
    calculate all the primes up to square root of n (rounded up) by using the
    sieve of erathostenes algorithm. (https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)

    gcd_greater_one():
    check if n is a pp by querying the gcd and return True if it's greater than
    1

    def find_m_k():
    solves for the pair (m, k)
"""

import math

def eratosthenes2(n):
    """Calculate all the primes up to square root of n (rounded up)."""
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, n+1, i))

def gcd_greater_one(prime_factors, exponents):
    """Check if n is a pp by querying the gcd and return True if it's greater than
    1."""
    if len(exponents) <= 2:
        gcd = math.gcd(exponents[0], exponents[1])
    return True if gcd > 1 else False

def find_m_k(unique_prime_factors, prime_factors, primes, n):
    for upf in unique_prime_factors:
        if upf == 2:
            continue
        m = upf
        while True:
            if m**primes[0] > n:
                break
            pair = [(m, k) for k in primes if m**k == n]
            if pair:
                return [x for x in pair[0]]
            m += upf


def isPP(n):
    if math.sqrt(n).is_integer():
        return [int(math.sqrt(n)), 2]
    primes = [p for p in eratosthenes2(int(math.ceil(math.sqrt(n))))]
    divisors = []
    prime_factors = []
    m = n
    for p in primes:
        while True:
            if m % p != 0:
                break
            m = m // p
            prime_factors.append(p)
            divisors.append(m)
            if m == 2:
                break
    pair = [(d, p) for d in divisors for p in primes if d**p == n]
    if not pair:
        unique_prime_factors = [upf for upf in set(prime_factors)]
        exponents = [prime_factors.count(upf) for upf in unique_prime_factors]
        if gcd_greater_one(prime_factors, exponents):
            return find_m_k(unique_prime_factors, prime_factors, primes, n)
    return [x for x in pair[0]] if pair else None
