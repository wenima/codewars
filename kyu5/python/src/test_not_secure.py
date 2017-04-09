"""Tests for codewars kata https://www.codewars.com/kata/not-very-secure/train/python."""

import pytest


TEST_INPUT = [
    ('hello world_', False),
    ('PassW0rd', True),
    ('', False),
    ('      ', False),
]


@pytest.mark.parametrize('s, result', TEST_INPUT)
def test_alphanumeric(s, result):
    """Test alphanumeric returns True if input is alphanumeric else False."""
    from not_secure import alphanumeric
    assert alphanumeric(s) == result

@pytest.mark.parametrize('s, result', TEST_INPUT)
def test_alphanumeric_py(s, result):
    """Test alphanumeric returns True if input is alphanumeric else False."""
    from not_secure import alphanumeric_py
    assert alphanumeric_py(s) == result
