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
    ('hi(hi)()',True),
]


@pytest.mark.parametrize('s, result', TEST_PS)
def test_validParentheses(s, result):
    """Test valid braces for parantheses."""
    from valid_parentheses import validParentheses
    assert validParentheses(s) == result
