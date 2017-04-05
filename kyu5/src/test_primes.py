"""Test dbl_linked_list data structures."""

import pytest

TESTS = [
    (1, [2]),
    (2, [2, 3]),
    (5, [2, 3, 5, 7, 11]),
]


@pytest.fixture
def empty_Primes():
    from primes import Primes
    new_primes = Primes()
    return new_primes


def test_create_Primes_object(empty_Primes):
    """Test creation of an empty Primes object."""
    assert empty_Primes.prime_list == []

@pytest.mark.parametrize('p, result', TESTS)
def test_first_few_primes(p, result, empty_Primes):
    """Test method first returns results from TESTS."""
    assert empty_Primes.first(p) == result
