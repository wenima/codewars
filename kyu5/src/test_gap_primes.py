"""Tests for kata gap_primes."""

import pytest

TESTS = [
    (2, 5, 7, (5, 7)),
    (2, 5, 5, None),
    (4, 130, 200, (163, 167)),
]


@pytest.mark.parametrize('g, m, n, result', TESTS)
def test_gap_primes(g, m, n, result):
    """Test that the correct prime pair is returned."""
    from gap_primes import gap
    assert gap(g, m, n) == result
