"""Tests for codewars kata https://www.codewars.com/kata/rpg-dice-roller."""

import pytest

TEST_INPUT = [
    ('', False)
    ({}, False),
    ('abc', False),
    ('2d6+3 abc', False),
    ('abc 2d6+3', False),
    ('2d6++4', False),
    ('d6', True),
    ('2d4', True),
    ('d3 + 4', True),
    ('3d7 + 3 -2', True),
]


@pytest.mark.parametrize('d, result', TESTS)
def test_dice_notation_input(d, result):
    """Test that dice notation is correct."""
    from diceroller import validate_input
    assert validate_input(d) == result
