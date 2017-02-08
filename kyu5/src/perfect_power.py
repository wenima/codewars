"""Module to solve the code-kata https://www.codewars.com/kata/whats-a-perfect-power-anyway/python

Note that this can be solved in a few lines if we don't care about k being a
prime but if we make the kata harder and solve for k being a prime, it becomes
more interesting.

We assume that if all divisors are known then k must be a prime.
In a first attempt, the algorithm iterates through all the divisors it came to
know during prime factorization and uses each and iterates through the list of
primes for k.

For very large numbers though, this is quite inefficient so we only use primes
that we will end up using.

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
import sys

major, minor  = (sys.version_info[0], sys.version_info[1])
if major == 3 and minor >= 5:
    from math import gcd
else:
    from fractions import gcd
from math import sqrt, ceil

def eratosthenes2(n):
    """Calculate all the primes up to square root of n (rounded up)."""
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, n+1, i))

def gcd_greater_one(prime_factors, exponents):
    """Check if n is a pp by querying the gcd and return True if it's greater than
    1. If more than 2 exponents, calculate the gcd of the first 2 and then uses
    the result as the first exponent for any further calc of gcd."""
    gcd_result = gcd(exponents[0], exponents[1])
    while True:
        gcd_result = gcd(gcd_result, exponents.pop())
        if len(exponents) < 3:
            break
    return True if gcd_result > 1 else False

def find_m_k(unique_prime_factors, prime_factors, primes, n):
    """Check for each m in a prime_factor's series if m raised to each prime k
    equals n. Return m, k if it does."""
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
    """Check for various approaches to solve for a pair m, k where integer m
    raised to the power of k equals n."""
    if sqrt(n).is_integer():
        return [int(sqrt(n)), 2]
    primes = [p for p in eratosthenes2(int(ceil(sqrt(n))))]
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
    if len(divisors) < 2:
        return None
    subset_primes = []
    while True:
        if divisors[-1] == 1:
            d = divisors[-2]
        else:
            d = divisors[-1]
        for p in primes:
            if d**p > n:
                subset_primes.append(p)
                break
            subset_primes.append(p)
        break
    primes = subset_primes
    pair = [(d, p) for d in divisors for p in primes if d**p == n]
    if not pair:
        unique_prime_factors = [upf for upf in set(prime_factors)]
        exponents = [prime_factors.count(upf) for upf in unique_prime_factors]
        if len(exponents) < 2:
            return None
        if gcd_greater_one(prime_factors, exponents):
            return find_m_k(unique_prime_factors, prime_factors, primes, n)
    return [x for x in pair[0]] if pair else None

if __name__ == '__main__':
    pp = [4,8,9,16,25,27,32,36,49,64,81,100,121,125,128,
 144,169,196,216,225,243,256,289,324,343,361,400,
 441,484,512,529,576,625,676,729,784,841,900,961,
 1000,1024,1089,1156,1225,1296,1331,1369,1444,1521,
 1600,1681,1728,1764]

for x in range(1764):
    print(isPP(x))
