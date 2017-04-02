"""Test for https://www.codewars.com/kata/primes-with-even-digits."""

import pytest


TEST_DIGITS = [
(1000, 887),
(1210, 1201),
(10000, 8887),
(500, 487),
(487, 467),
]


@pytest.mark.parametrize('n, result', TEST_DIGITS)
def test_fib_digits(n, result):
    """Test fib_digits returns correct integer pairs."""
    from even_digit_primes import f
    assert f(n) == result
