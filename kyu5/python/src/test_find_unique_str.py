"""Tests for codewars kata https://www.codewars.com/kata/find-the-unique-string."""

import pytest


TEST = [
    ([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ], 'BbBb'),
    ([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ], 'foo'),
]


@pytest.mark.parametrize('arr, result', TEST)
def test_find_uniq(arr, result):
    """Test that function returns unique element."""
    from find_unique_str import find_uniq
    assert find_uniq(arr) == result
