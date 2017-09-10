"""Tests for codewars kata https://www.codewars.com/kata/ranking-poker-hands/."""

import pytest
from random import shuffle

SORTED_POKER_HANDS = [
"KS AS TS QS JS",
"2H 3H 4H 5H 6H",
"AS AD AC AH JD",
"JS JD JC JH 3D",
"2S AH 2H AS AC",
"AS 3S 4S 8S 2S",
"2H 3H 5H 6H 7H",
"2S 3H 4H 5S 6C",
"2D AC 3H 4H 5S",
"AH AC 5H 6H AS",
"2S 2H 4H 5S 4C",
"AH AC 5H 6H 7S",
"AH AC 5H 5C KS",
"AH AC 5H 5C QS",
"AH AC 4H 6H 7S",
"2S AH 4H 5S KC",
"2S 3H 6H 7S 9C",
"AC KH QH AH AS",
"7C 7S KH 2H 7H",
"7C 7S QH 2S 7D",
"7C 7S TH 2S 7D",
"2H 2C 3S 3H 3D",
"3D 2H 3H 2C 2D",
"KH KC 3S 3H 3D",
"2H 2C 3S 3H 3D",
"AC KH QH AH AS",
"7C 7S KH 2H 7H"
]

def test_custom_sort():
    """Test the output of sort matches list."""
    from poker_rankings import PokerHand
    pokerhands = []
    for hand in SORTED_POKER_HANDS:
        pokerhands.append(Pokerhand(hand))
    shuffle(pokerhands)
    pokerhands.sort(reverse=True)
    for i, hand in enumerate(pokerhands)
        assert hand == SORTED_POKER_HANDS[i]
