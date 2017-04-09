"""Tests for codewars kata https://www.codewars.com/kata/rpg-dice-roller."""

import pytest

TEST_INPUT = [
    ('', False),
    ({}, False),
    ('abc', False),
    ('2d6+3 abc', False),
    ('abc 2d6+3', False),
    ('2d6++4', False),
    ('d6', True),
    ('2d4', True),
    ('d3 + 4', True),
    ('3d7 + 3 -2', True),
    ('10d20', True),
]

TEST_MODIFIERS = [
    ('d3+4', 4),
    ('3d7+3-2', 1),
    ('d6+10-11', -1),
    ('d6', 0),
]

TEST_OUTPUT_SUMMED = [
    ('d6', 0, 7),
    ('2d4', 1, 9),
    ('d3 + 4', 4, 8),
    ('3d7 + 3 - 2', 3, 23),
]


@pytest.mark.parametrize('d, result', TEST_INPUT)
def test_dice_notation_input(d, result):
    """Test that dice notation is correct."""
    from diceroller import validate_input, normalize_input
    assert validate_input(d) == result

@pytest.mark.parametrize('d, result', TEST_MODIFIERS)
def test_get_modifiers(d, result):
    """Test modifiers are correctly returned as an integer."""
    from diceroller import get_modifiers
    assert get_modifiers(d) == result

@pytest.mark.parametrize('d, lower, upper', TEST_OUTPUT_SUMMED)
def test_dice_roll_summed(d, lower, upper):
    """Test that output with summed returns a number within bounds."""
    from diceroller import roll
    assert lower < roll(d) < upper
