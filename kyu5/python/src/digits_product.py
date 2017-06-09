"""Test for https://www.codewars.com/kata/simple-fun-number-81-digits-product/."""

def digits_product(n, out):
    """Return the smallest integer composed of products of n."""
    if n == 1 and not out:
        return 11
    elif n == 1:
        if len(out) == 1:
            return int(''.join(['1'] + sorted(out)))
        else:
            return int(''.join(sorted(out)))
    if n == 0: return 10
    for i in range(9, 0, -1):
        if i == 1:return -1
        if n % i:
            continue
        out.append(str(i))
        return digits_product(n//i, out)
