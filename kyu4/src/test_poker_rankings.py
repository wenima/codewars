"""Tests for codewars kata https://www.codewars.com/kata/ranking-poker-hands/."""

import pytest


TEST_INPUT = [
    ("2H 3H 4H 5H 6H", "KS AS TS QS JS", 'Loss'),
    ("2H 3H 4H 5H 6H", "AS AD AC AH JD", 'Win'),
    ("AS AH 2H AD AC", "JS JD JC JH 3D", 'Win'),
    ("2S AH 2H AS AC", "JS JD JC JH AD", 'Loss'),
    ("2S AH 2H AS AC", "2H 3H 5H 6H 7H", 'Win'),
    ("AS 3S 4S 8S 2S", "2H 3H 5H 6H 7H", 'Win'),
    ("2H 3H 5H 6H 7H", "2S 3H 4H 5S 6C", 'Win'),
    ("2S 3H 4H 5S 6C", "3D 4C 5H 6H 2S", 'Tie'),
    ("2S 3H 4H 5S 6C", "AH AC 5H 6H AS", 'Win'),
    ("2S 2H 4H 5S 4C", "AH AC 5H 6H AS", 'Loss'),
    ("2S 2H 4H 5S 4C", "AH AC 5H 6H 7S", 'Win'),
    ("6S AD 7H 4S AS", "AH AC 5H 6H 7S", 'Loss'),
    ("2S AH 4H 5S KC", "AH AC 5H 6H 7S", 'Loss'),
    ("2S 3H 6H 7S 9C", "7H 3C TH 6H 9S", 'Loss'),
    ("4S 5H 6H TS AC", "3S 5H 6H TS AC", 'Win'),
    ("2S AH 4H 5S 6C", "AD 4C 5H 6H 2C", 'Tie'),
]

TEST_STRAIGHT = [
    ("2H 3H 4H 5H 6H", True),
    ("AS AH 2H AD AC", False),
    ("2H 3H 5H 6H 7H", False),
    ("KS AS TS QS JS", True),
    ("8H 9H QS JS TH", True),
]

TEST_FLUSH = [
    ("2H 3H 4H 5H 6H", True),
    ("AS AH 2H AD AC", False),
    ("2H 3H 5H 6H 7H", True),
    ("KS AS TS QS JS", True),
    ("8H 9H QS JS TH", False),
    ("AS 3S 4S 8S 2S", True),
]

TEST_VALUES = [
    ("2H 2S 4H 5H 6H", 1),
    ("AS AH 2H 2D KC", 3),
    ("AS AH AC 2D KC", 4),
    ("AH AC 6S 6H AS", 7),
    ("8H 9H QS JS KH", 0),
]


@pytest.mark.parametrize('hand, result', TEST_STRAIGHT)
def test_hand_is_straight(hand, result):
    """Test that hand has a made hand value of straight."""
    from poker_rankings import PokerHand
    heros_hand = PokerHand(hand)
    assert heros_hand._is_straight() == result

@pytest.mark.parametrize('hand, result', TEST_FLUSH)
def test_hand_is_flush(hand, result):
    """Test that hand has a made hand value of flush."""
    from poker_rankings import PokerHand
    heros_hand = PokerHand(hand)
    assert heros_hand._is_flush() == result

@pytest.mark.parametrize('hand, result', TEST_VALUES)
def test_hand_values(hand, result):
    """Test that hand has a made hand value of flush."""
    from poker_rankings import PokerHand
    from collections import defaultdict
    heroes_hand = PokerHand(hand)
    heroes_hand.get_card_values()
    heroes_hand.get_made_hand_value()
    assert heroes_hand.hand_value == result

def test_hand_has_correct_high_card():
    from poker_rankings import PokerHand
    heroes_hand = PokerHand("8H 9H QS JS KH")
    from collections import defaultdict
    heroes_hand.get_high_cards()
    assert heroes_hand.high_card.pop(0) == "K"
    assert heroes_hand.high_card.pop(0) == "Q"

@pytest.mark.parametrize('hand, result', TEST_INPUT)
def test_compare_hero_to_villain(hand, result):
    from poker_rankings import PokerHand
    from collections import defaultdict
    hero, villain = PokerHand(hand), PokerHand(other)
    hero.get_card_values()
    villain.get_card_values()
    hero.get_made_hand_value()
    villain.get_made_hand_value()
    assert hero.compare_with(villain) == result
