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

def test_hand_has_4_of_a_kind():
    """Test that hand has made hand value of 4 of a kind."""
    from poker_rankings import PokerHand
    heroes_hand = PokerHand('AS AH 2H AD AC')
    heroes_hand.get_card_values()
    assert sorted(heroes_hand.val_cnt.items(), key=lambda x: x[1], reverse=True).pop(0)[1] == 4


def test_hand_has_set():
    """Test that hand has made hand value of a set."""
    from poker_rankings import PokerHand
    from collections import defaultdict
    heroes_hand = PokerHand("AH AC 5H 6H AS")
    heroes_hand.get_card_values()
    assert sorted(heroes_hand.val_cnt.items(), key=lambda x: x[1], reverse=True).pop(0)[1] == 3

def test_hand_has_2pair():
    """Test that hand has made hand value of 2 pair."""
    from poker_rankings import PokerHand
    from collections import defaultdict
    heroes_hand = PokerHand("AH AC 5H 5C 2S")
    assert heroes_hand._has_2pair() == 3
