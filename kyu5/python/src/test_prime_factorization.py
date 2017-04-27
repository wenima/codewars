"""Tests for kata Prime factorization."""

import pytest

INPUT_NUMS = [1, 24, 13]

TESTS_PF = {
    1: {},
    24: {2: 3, 3: 1},
    13: {13: 1},
}

@pytest.fixture(scope='function', params=INPUT_NUMS)
def PrimeFactorizer(request):
    from prime_factorization import PrimeFactorizer
    new_PrimeFactorizer = PrimeFactorizer(request.param)
    return new_PrimeFactorizer

def test_prime_factorization(PrimeFactorizer):
    """Test that a dict with correct prime factors and count are returned."""
    result = TESTS_PF[PrimeFactorizer]
    assert PrimeFactorizer.factor == result
