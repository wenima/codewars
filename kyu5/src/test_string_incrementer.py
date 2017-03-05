"""Tests for kata last_digit."""

import pytest

TESTS = [
    ('foo', 'foo1'),
    ('foobar23', 'foobar24'),
    ('foo0042', 'foo0043'),
    ('foo9', 'foo10'),
    ('foo099', 'foo100'),
]


@pytest.mark.parametrize('s, result', TESTS)
def test_string_increment(s, result):
    """Test that if a string ends with a number, the number is correctly
    incremented."""
    from string_incrementer import string_increment
    assert string_increment(s) == result
