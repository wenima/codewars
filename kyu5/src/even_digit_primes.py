"""Module for code-kata https://www.codewars.com/kata/primes-with-even-digits."""


def is_prime(n):
    """Return True if n is a prime."""
    if n > 2 and n % 2 == 0:
        return False
    for x in range(3, int(n**0.5 + 1), 2):
        if n % x == 0:
            return False
    return True

def step(n):
    """Yield all primes lower than n"""
    if n % 2 == 0: n -= 1 #need to see an odd number so we can step over known composites
    try:
        return next(x for x in range(n, n - 100, - 2) if is_prime(x))
    except StopIteration:
        return None

def f(p):
    """Return the closest prime number under a certain integer n that has the
    maximum possible amount of even digits.."""
    p = str(p)
    hits = 0
    found[p] = sum([p.count(str(i)) for i in range(0, 10, 2)])
