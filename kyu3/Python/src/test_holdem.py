"""Tests for codewars kata https://www.codewars.com/kata/texas-holdem-hands/."""

import pytest

HAND_STRENGTH_INDEX = [
    ([(14, 8), (5, 32), (5, 8), (13, 32), (13, 64)], 6),
    ([(11, 32), (5, 32), (10, 32), (12, 32), (3, 32)], 3),
    ([(14, 64), (14, 8), (14, 32), (14, 1), (13, 32)], 0),
]

HAND_RANK = [
    ('A♦A♣5♥5♣K♥Q♥K♦', 6),
    ('A♦A♣A♥A♠5♣K♥Q♥', 0),
    ('A♠K♦J♥5♥10♥Q♥3♥', 3),
]

def test_get_cards():
    """Test that get_cards returns a list of strings representing the numerical value of each card."""
    from holdem import get_cards
    assert get_cards('A♦A♣5♥5♣K♥Q♥K♦') == [14, 14, 5, 5, 13 , 12, 13]

def test_get_suits():
    """Test that get_suits returns a list of strings representing the suits."""
    from holdem import get_suits
    assert get_suits('A♦A♣5♥5♣K♥Q♥K♦') == ['♦', '♣', '♥', '♣', '♥', '♥', '♦']

def test_get_pokerscore():
    """Test that getPokerScore returns correct integer score for given hand."""
    from holdem import get_pokerscore
    assert get_pokerscore([14,14,5,5,12]) == 976220

@pytest.mark.parametrize('hand, result', HAND_STRENGTH_INDEX)
def test_calc_index(hand, result):
    """Test that calc_index returns the correct index for a given hand and suits."""
    from holdem import calc_index
    assert calc_index(hand) == result

# @pytest.mark.parametrize('hand, result', HAND_RANK)
# def test_rank_hand(hand, result):
#     """Test that rank_hand returns the correct index from a list of hand strenght for a given hand."""
#     from holdem import rank_hand
#     assert rank_hand(hand)[0] == result


    
