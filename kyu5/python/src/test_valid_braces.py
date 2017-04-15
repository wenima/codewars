"""Tests for codewars kata https://www.codewars.com/kata/valid-braces."""

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
    ('())(((((', False)
]

TEST_INPUT = [
    ('(){}[]', True),
    ('(}', False),
    ('[(])', False),
    ('([{}])', True)
]

@pytest.mark.parametrize('s, result', TEST_PS)
def test_valid_braces_parantheses(s, result):
    """Test valid braces for just parantheses."""
    from valid_braces import valid_braces
    assert valid_braces(s) == result

@pytest.mark.parametrize('s, result', TEST_INPUT)
def test_valid_braces(s, result):
    """Test valid braces returns correct result."""
    from valid_braces import valid_braces
    assert valid_braces(s) == result
