"""Tests for codewars kata https://www.codewars.com/kata/valid-braces."""

import pytest


TEST_INPUT = [
    ('(){}[]', True),
    ('(}', False),
    ('[(])', True),
]


def test_valid_braces_parantheses():
    """Test valid braces for just parantheses."""
    from valid_braces import valid_braces
    assert valid_braces('((()))') == True

@pytest.mark.parametrize('s, result', TEST_INPUT)
def test_valid_braces(s, result):
    """Test valid braces returns correct result."""
    from valid_braces import valid_braces
    assert valid_braces(s) == result
