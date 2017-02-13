"""Tests for kata primes_in_number."""

import pytest

TESTS = [
    (0, '(0)'),
    (1, '(1)'),
    (2, '(2)'),
    (4, '(2**2)'),
    (9, '(3**2)'),
    (11, '(11)'),
    (33, '(3)(11)'),
    (81, '(3**4)'),
    (216, '(2**3)(3**3)'),
    (3199, '(7)(457)'),
    (86240, '(2**5)(5)(7**2)(11)'),
    # (1267650600228229401496703205376, ('(2**100)')),
]


@pytest.mark.parametrize('a, result', TESTS)
def test_last_digit(a, result):
    """Test that the correct prime factorization is returned."""
    from primes_in_numbers import primeFactors
    assert primeFactors(a) == result
