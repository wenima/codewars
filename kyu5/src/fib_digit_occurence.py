"""Module to solve the code-kata
https://www.codewars.com/kata/calculate-fibonacci-return-count-of-digit-occurrences."""


def fib_digits(n):
    """Return a list of integer pairs, containing number of occurrence for digit,
    sorted in descending order."""
    pass

def generate_fib(n):
    """Return the nth fibonacci number."""
    a, b = 0, 1
    for __ in range(n-1):
        a, b = b, a + b
    return b
