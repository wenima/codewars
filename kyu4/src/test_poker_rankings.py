"""Tests for codewars kata https://www.codewars.com/kata/ranking-poker-hands/."""

import pytest


TEST_INPUT = [
    ("2H 3H 4H 5H 6H", "KS AS TS QS JS", 'Loss'),
    ("2H 3H 4H 5H 6H", "AS AD AC AH JD", 'Win'),
    ("AS AH 2H AD AC", "JS JD JC JH 3D", 'Win'),
    ("AS AH 3H AD AC", "AS AH 2H AD AC", 'Win'),
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
    ("AH AC 5H 5C QS", "AH AC 5H 5C KS", 'Loss'),
    ("AH AC 5H 5C QS", "KH KC 5H 5C QS", 'Win'),
    ("7C 7S KH 2H 7H", "3C 3S AH 2H 3H", 'Win'),
    ("3C 3S AH 2H 3H", "7C 7S KH 2H 7H", 'Loss'),
    ("6H 5H 4H 3H 2H", "5H 4H 3H 2H AH", "Win"),
    ("5H 4H 3H 2H AH", "5H 4H 3H 2H AH", "Tie"),
    ("5H 4H 3H 2H AH", "6H 5H 4H 3H 2H", "Loss"),
    ("AS 3S 4S 8S 2S", "2H 3H 5H 6H 7H", "Win"),
    ("2S 3H 6H 7S 9C", "7H 3C TH 6H 9S", "Loss")
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
    ("2H 3H 4H 5H 6H", 9),
]

@pytest.mark.parametrize('hand, result', TEST_STRAIGHT)
def test_hand_is_straight(hand, result):
    """Test that hand has a made hand value of straight."""
    from poker_rankings import PokerHand
    heros_hand = PokerHand(hand)
    assert heros_hand._is_straight == result

@pytest.mark.parametrize('hand, result', TEST_FLUSH)
def test_hand_is_flush(hand, result):
    """Test that hand has a made hand value of flush."""
    from poker_rankings import PokerHand
    heros_hand = PokerHand(hand)
    assert heros_hand._is_flush == result

def test_hand_is_straightflush():
    """Test that hand has a made hand value of straight flush."""
    from poker_rankings import PokerHand
    heroes_hand = PokerHand("5H 4H 3H 2H AH")
    assert heroes_hand._is_flush == True
    assert heroes_hand._is_straight == True
    assert heroes_hand._hand_value == 9

def test_tie_when_both_hands_are_straightflush():
    """Test that if both hands are 5 high straight flushes, result is Tie."""
    from poker_rankings import PokerHand
    heroes_hand = PokerHand("5H 4H 3H 2H AH")
    villains_hand = PokerHand("5H 4H 3H 2H AH")
    heroes_hand.compare_with(villains_hand) == 'Tie'

@pytest.mark.parametrize('hand, result', TEST_VALUES)
def test_hand_values(hand, result):
    """Test that hand has a made hand value of flush."""
    from poker_rankings import PokerHand
    from collections import defaultdict
    heroes_hand = PokerHand(hand)
    assert heroes_hand._hand_value == result

def test_hand_has_correct_high_card():
    from poker_rankings import PokerHand
    heroes_hand = PokerHand("8H 9H QS JS KH")
    from collections import defaultdict
    assert heroes_hand.hand.pop(0) == 13
    assert heroes_hand.hand.pop(0) == 12

@pytest.mark.parametrize('hand, other, result', TEST_INPUT)
def test_compare_hero_to_villain(hand, other, result):
    from poker_rankings import PokerHand
    from collections import defaultdict
    hero, villain = PokerHand(hand), PokerHand(other)
    print(hero._total_value)
    print(villain._total_value)
    assert hero.compare_with(villain) == result
