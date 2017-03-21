"""Tests for codewars kata https://www.codewars.com/kata/convert-string-to-camel-case/python."""

import pytest


TEST_INPUT = [
    # ('',''),
    ('the_stealth_warrior', 'theStealthWarrior'),
    ('The-Stealth-Warrior', 'TheStealthWarrior'),
]


@pytest.mark.parametrize('s, result', TEST_INPUT)
def test_to_camel_case(s, result):
    """Test to_camel_case converts correctly."""
    from camelcase import to_camel_case
    assert to_camel_case(s) == result
