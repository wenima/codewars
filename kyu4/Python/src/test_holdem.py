"""Tests for codewars kata https://www.codewars.com/kata/texas-holdem-poker/python."""

import pytest

BOARDS = [
(['2', '3', '5', '6', '7'], True),
(['9','8','K','A','4'], False)
]

TEST_STRAIGHT = [
    (['2','2','3','3','4'],['5','6'], True),
    (['9','8','3','3','4'],['5','6'], False),
    (['9','8','K','Q','4'],['7','6'], False),
    (['2','2','3','3','A'],['5','4'], True),
    (['2','6','3','7','A'],['5','4'], True),
]

@pytest.mark.parametrize('board, hole_cards, result', TEST_STRAIGHT)
def test_hand_is_straight(board, hole_cards, result):
    """Test that combination of board and hole_cards has a made hand value of straight."""
    from holdem import PokerHand
    hand = ''.join(board + hole_cards)
    heros_hand = PokerHand(hand)
    assert heros_hand._is_straight == result
