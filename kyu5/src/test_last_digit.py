"""Tests for kata last_digit."""

import pytest

TESTS = [
    (4, 0, 1),
    (4, 1, 4),
    (4, 2, 6),
    (9, 7, 9),
    (9, 2**3, 1),
    (10, 10**10, 0),
    (2**200, 2**300, 6),
]


@pytest.mark.parametrize('a, b, result', TESTS)
def test_last_digit(a, b, result):
    """Test that given positive integers a and b, the correct last_digit
    is returned."""
    from last_digit import last_digit
    assert last_digit(a, b) == result
