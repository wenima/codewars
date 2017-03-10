"""Tests for codewars kata https://www.codewars.com/kata/base-2/train/python."""

import pytest

TESTS = [
    (6, '11010'),
    (-6, '1110'),
    (4, '100'),
    (18, '10110'),
    (-11, '110101'),
]


@pytest.mark.parametrize('n, result', TESTS)
def test_int_to_negabinary(n, result):
    """Test that given number n is being correctly returned as result."""
    from base_neg_2.py import int_to_negabinary
    assert int_to_negabinary(n) == result
