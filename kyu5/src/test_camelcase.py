"""Tests for codewars kata https://www.codewars.com/kata/convert-string-to-camel-case/python."""

import pytest


TEST_INPUT = [
    ('the_stealth_warrior', 'theStealthWarrior'),
    ('The-Stealth-Warrior', 'TheStealthWarrior'),
]


@pytest.mark.parametrize('in, out', TEST_INPUT)
def to_camel_case(in, out):
    """Test to_camel_case converts correctly."""
    from camelcase import to_camel_case
    assert to_camel_case(in) == out
