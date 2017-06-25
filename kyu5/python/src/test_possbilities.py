"""Tests for codewars kata https://www.codewars.com/kata/1-s-0-s-and-wildcards/train/python."""

import pytest


TEST_INPUT = [
    ('101?', ['1010', '1011']),
    ('10??', ['1000', '1001', '1010', '1011']),
    ('1?1?', ['1010', '1011', '1110', '1111']),
]


@pytest.mark.parametrize('s, result', TEST_INPUT)
def test_possibilities(s, result):
    """Test that for a given string including ? as wildcards, all posibilities
    are returned where ? is replaced with 1 and 0."""
    from possibilities import possibilities
    assert possibilities(s) == result
