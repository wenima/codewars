"""Module for code-kata https://www.codewars.com/kata/primes-with-even-digits."""


def is_prime(n):
    """Return True if n is a prime."""
    for x in range(3, int(n**0.5 + 1), 2):
        if n % x == 0:
            return False
    return True


def get_value_to_subtract(n):
    """Return a value to get to the nearest range to find an even digit prime."""
    p = n - 1
    p = str(p)
    if int(p[0]) == 1 and int(p[1]) % 2 != 0:
        second_msd = int(p[2])
    else:
        return 0
    if int(p[0]) % 2 != 0 and intp[0] != 1:
            second_msd = int(p[1])
    multiples_of_10 = len(p) - 2
    build_str_to_subtract = [str(second_msd)] + multiples_of_10 * ['0']
    return int(''.join(build_str_to_subtract))


def step(n):
    """Yield all primes lower than n"""
    if n % 2 == 0: n -= 1 #need to see an odd number so we can step over known composites
    try:
        return next(x for x in range(n, 0, - 2) if is_prime(x))
    except StopIteration:
        return None


def f(n):
    """Return the closest prime number under a certain integer n that has the
    maximum possible amount of even digits."""
    p = n - 1
    sub = get_value_to_subtract(n)
    p -= sub
    while True:
        p = step(p)
        if sum([str(p).count(str(i)) for i in range(0, 10, 2)]) == len(str(p)) -1 if sub else -2:
            break
        p -= 2
    return p
