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


@pytest.mark.parametrize('p, result', TESTS)
def test_first_few_primes(p, result, empty_Primes):
    """Test method first returns results from TESTS."""
    assert empty_Primes.first(p) == result

def test_primes_slice():
    """Test method first returns correct slice."""
    from primes import Primes
    Primes = Primes()
    assert Primes.first(20)[-5:] == [53, 59, 61, 67, 71]

def test_prime_100th_element():
    """Test method first returns correct element."""
    from primes import Primes
    Primes = Primes()
    assert Primes.first(100)[99] == 541

def test_prime_80thth_element():
    """Test method first returns correct element."""
    from primes import Primes
    Primes = Primes()
    assert Primes.first(80)[79] == 409
