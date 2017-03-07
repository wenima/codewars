"""Tests for kata regex password validator."""

import pytest

TESTS = [
    ('fjd3IR9', True),
    ('ghdfj32', False),
    ('DSJKHD23', False),
    ('dsF43', False),
    ('4fdg5Fj3', True),
    ('DHSJdhjsU', False),
    ('fjd3IR9.;', False),
    ('fjd3  IR9', False),
    ('djI38D55', True),
    ('a2.d412', False),
    ('JHD5FJ53', False),
    ('!fdjn345', False),
    ('jfkdfj3j', False),
    ('123', False) ,
    ('abc', False),
    ('123abcABC', True),
    ('ABC123abc', True),
    ('Password123', True),
    ('0qw 8EkloP', False),
]


@pytest.mark.parametrize('s, result', TESTS)
def test_validate_pwd(s, result):
    """Test that supplied string satisfies the password requirements."""
    from regex_pwd_validator import validate_pwd
    assert validate_pwd(s) == result
