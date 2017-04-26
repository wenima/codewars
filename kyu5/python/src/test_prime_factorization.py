"""Tests for kata Prime factorization."""

import pytest

TESTS_PF = [
    (24, { 2: 3, 3: 1 }),
]

@pytest.fixture
def PrimeFactorizer():
    from prime_factorization import PrimeFactorizer
    new_PrimeFactorizer = PrimeFactorizer()
    return new_PrimeFactorizer

@pytest.mark.parametrize('n, result', TESTS_PF)
def test_prime_factorization(n, result, PrimeFactorizer):
    """Test that a dict with correct prime factors and count are returned."""
    assert PrimeFactorizer.factor(n) == result
