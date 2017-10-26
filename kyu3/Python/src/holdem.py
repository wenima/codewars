"""Tests for codewars kata https://www.codewars.com/kata/texas-holdem-hands/."""

import re
from collections import Counter

LOOKUP = {
    'A' : '14',
    'K' : '13',
    'Q' : '12',
    'J' : '11',
    }

def get_cards(hand):
    """Return a list with string representation of a given 7 card hand."""
    card_str_no_suits = ''.join([c if ord(c) < 128 else '' for c in hand])
    cards = [LOOKUP[c] if not c.isnumeric() else c for c in card_str_no_suits]
    return cards

def get_suits(hand):
    """Return a list with the suits of the hand."""
    pattern = re.compile('♠|♣|♥|♦')
    return list(re.findall(pattern, hand))

def get_pokerscore(hand):
    """Return a unique value representing overall hand strength."""
    c = Counter(hand)
    a = sorted(hand, key=lambda x: (c[x], x), reverse=True)
    return a[0]<<16|a[1]<<12|a[2]<<8|a[3]<<4|a[4]
