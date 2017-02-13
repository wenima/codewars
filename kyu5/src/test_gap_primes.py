"""Tests for kata gap_primes."""

import pytest

TESTS = [
    (2, 5, 7, [5, 7]),
    (2, 5, 5, None),
    (4, 130, 200, [163, 167]),
    (2, 100, 110, [101, 103]),
    (4, 100, 110, [103, 107]),
    (6, 100, 110, None),
    (8, 300, 400, [359, 367]),
    (10, 300, 400, [337, 347]),
]


@pytest.mark.parametrize('g, m, n, result', TESTS)
def test_gap_primes(g, m, n, result):
    """Test that the correct prime pair is returned."""
    from gap_primes import gap
    assert gap(g, m, n) == result
