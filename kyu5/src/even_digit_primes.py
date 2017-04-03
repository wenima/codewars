"""Module for code-kata https://www.codewars.com/kata/primes-with-even-digits."""


def is_prime(n):
    """Return True if n is a prime."""
    for x in range(3, int(n**0.5 + 1), 2):
        if n % x == 0:
            return False
    return True


def get_range_even_digit_prime(n):
    """Return a value to get to the nearest range to find an even digit prime."""
    sn = [n for n in str(n)]
    if sn[0] == '1':
        i = 1
        while True:
            if sn[i] != '0':
                break
                i += 1
                if i == len(sn) - 1:
                    for j in range(1, len(sn) - 1):
                        sn[j] = '8'
                    sn[-1] = '9'
                del sn[0]
                break
        if int(sn[1]) % 2 != 0:
            sn[1] = str(int(sn[1]) - 1)
            for i in (2, len(sn) - 1):
                sn[i] = '8'
            sn[-1] = '9'
    if sn[0] != '1' and int(sn[0]) % 2 != 0:
        sn[0] = str(int(sn[0]) - 1)
        for i in range(1, len(sn) - 1):
            sn[i] = '8'
        sn[-1] = '9'
    return int(''.join(sn))


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
    p = get_range_even_digit_prime(p)
    while True:
        p = step(p)
        if sum([str(p).count(str(i)) for i in range(0, 10, 2)]) == len(str(p)) - (2 if int(str(p)[0]) == 1 else 1):
            break
        p -= 2
    return p
