"""Test for https://www.codewars.com/kata/simple-fun-number-81-digits-product/."""

import pytest


TEST_DIGITS = [
(12, 26),
(19, -1),
(450, 2559),
(0, 10),
(13, -1),
(1, 11),
(5, 15),
(10, 25),
]


@pytest.mark.parametrize('n, result', TEST_DIGITS)
def test_digits_product(n, result):
    """Test fib_digits returns correct integer pairs."""
    from digits_product import digits_product
    assert digits_product(n) == result
