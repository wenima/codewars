"""Module to solve the code-kata
https://www.codewars.com/kata/calculate-fibonacci-return-count-of-digit-occurrences."""


def fib_digits(n):
    """Return a list of integer pairs, containing number of occurrence for digit,
    sorted in descending order."""
    fib = str(generate_fib(n))
    found = {}
    for i in range(10):
        found[i] = fib.count(str(i))
    return sorted([(v, k) for k, v in found.items() if v > 0], reverse = True)



def generate_fib(n):
    """Return the nth fibonacci number."""
    a, b = 0, 1
    for __ in range(n-1):
        a, b = b, a + b
    return b
