"""Tests for codewars kata https://www.codewars.com/kata/ranking-poker-hands/."""

import pytest
from random import shuffle

SORTED_POKER_HANDS = [
"KS AS TS QS JS",
"KS AS TS QS JS",
"2H 3H 4H 5H 6H",
"AS AD AC AH JD",
"JS JD JC JH 3D",
"2S AH 2H AS AC",
"KH KC 3S 3H 3D",
"2H 2C 3S 3H 3D",
"3D 2H 3H 2C 2D",
"AS 3S 4S 8S 2S",
"2H 3H 5H 6H 7H",
"2S 3H 4H 5S 6C",
"2D AC 3H 4H 5S",
"AC KH QH AH AS",
"AH AC 5H 6H AS",
"7C 7S KH 2H 7H",
"7C 7S QH 2S 7D",
"7C 7S TH 2S 7D",
"AH AC 5H 5C KS",
"AH AC 5H 5C QS",
"AH AC 4H 5S 4C",
"2S 2H 4H 5S 4C",
"AH AC 5H 6H 7S",
"AH AC 4H 6H 7S",
"2S AH 4H 5S KC",
"2S 3H 6H 7S 9C",
]

def test_custom_sort_5high_straight():
    """Test that 5 high straights are compared correctly."""
    from sortable_poker_hands import PokerHand
    pokerhands = []
    pokerhands.append(PokerHand("2D AC 3H 4H 5S"))
    pokerhands.append(PokerHand("2S 3H 4H 5S 6C"))
    pokerhands.sort(reverse=True)
    assert pokerhands[0].passed_hand == "2S 3H 4H 5S 6C"

def test_repr():
    """Test that repr of PokerHand class returns a string."""
    from sortable_poker_hands import PokerHand
    hand = PokerHand("2D AC 3H 4H 5S")
    assert hand == '2D AC 3H 4H 5S'

def test_custom_sort():
    """Test the output of sort matches list."""
    from sortable_poker_hands import PokerHand
    pokerhands = []
    for hand in SORTED_POKER_HANDS:
        pokerhands.append(PokerHand(hand))
    shuffle(pokerhands)
    pokerhands.sort(reverse=True)
    for i, hand in enumerate(pokerhands):
        assert hand == SORTED_POKER_HANDS[i]
