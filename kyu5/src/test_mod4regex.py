"""Tests for codewars kata https://www.codewars.com/kata/mod4-regex."""

import pytest


TEST_INPUT = [
    ('[+05620]', True),
    ('[+05621]', False),
    ('[-55622]', False),
    ('[005623]', False),
    ('[005624]', True),
    ('[-05628]', True),
    ('the beginning [0] ... [invalid] numb[3]rs ... the end', True),
    ("No, [2014] isn't a multiple of 4...", False),
    ('...may be [+002016] will be.', True),
    ('[555636]', True),
    ('[005600]', True),
    ('the beginning [-0] the end', True),
    ('~[4]', True),
    ('[+05640]', True),
    ('[32]', True),
    ('[~24]', False),
]


@pytest.mark.parametrize('s, result', TEST_INPUT)
def test_mod4regex(s, result):
    """Test mod4-regex returns mod4 correctly."""
    from mod4regex import mod4
    assert mod4(s) == result
