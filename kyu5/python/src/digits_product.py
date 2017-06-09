"""Solution for https://www.codewars.com/kata/simple-fun-number-81-digits-product/."""

def digits_product(n):
    """Return the smallest integer composed of products of n."""
    out = []
    if n == 1: return 11
    if n == 0: return 10
    while True:
        if n > 7 and isprime(n):return -1
        for i in range(9, 0, -1):
            if i == 1 and len(out) == 0:
                return -1
            if n % i:
                continue
            out.append(str(i))
            n //= i
            break
        if n == 1 and len(out) == 1:
            out.append(str(n))
            break
        elif n == 1:break
    return int(''.join(sorted(out)))


def isprime(n):
    """Return True if n is a prime number for all n > 7."""
    if n % 2 == 0:return False
    return all(n % i for i in range(3, int(n**0.5) + 1, 2))
