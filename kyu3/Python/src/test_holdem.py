"""Tests for codewars kata https://www.codewars.com/kata/texas-holdem-hands/."""

import pytest

def test_get_cards():
    """Test that get_cards returns a list of strings representing the numerical value of each card."""
    from holdem import get_cards
    assert get_cards('A♦A♣5♥5♣K♥Q♥K♦) == ['14', '14', '5', '5', '13' ,'12', '13']

def test_get_suits():
    """Test that get_suits returns a list of strings representing the suits."""
    from holdem import get_suits
    assert get_suits('A♦A♣5♥5♣K♥Q♥K♦) == ['♦', '♣', '♥', '♣', '♥', '♥', '♦']

def test_get_combinations():
    """Test that get_combinations returns the correct length."""
    from holdem import get_combinations
    c = get_combinations(5, 7)
    assert len(c) == 21

def test_get_pokerscore():
    """Test that getPokerScore returns correct integer score for given hand."""
    from holdem import get_pokerscore
    assert get_pokerscore([14,14,5,5,12]) == 976220
