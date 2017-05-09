"""Tests for codewars kata https://www.codewars.com/kata/valid-parentheses/python."""

import pytest


TEST_PS = [
    (')))(((', False),
    ('((()))(', False),
    ('((()))', True),
    ('()()()()()()', True),
    ('())))(((()', False),
    ('()()())()()()', False),
    ('(()(()(', False),
    ('(((((())))', False),
    ('())(((((', False),
    ('hi(hiasdfsfasfal2342342ogojia.?!!$%^sdjgosagj)()',True),
]


@pytest.mark.parametrize('s, result', TEST_PS)
def test_valid_parentheses(s, result):
    """Test valid braces for parantheses."""
    from valid_parentheses import valid_parentheses
    assert valid_parentheses(s) == result
