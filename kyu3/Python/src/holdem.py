"""Tests for codewars kata https://www.codewars.com/kata/texas-holdem-hands/."""

import re
from collections import Counter
from itertools import combinations

LOOKUP = {
    'A' : 14,
    'K' : 13,
    'Q' : 12,
    'J' : 11,
    }

HANDRANKS = [8, 9, 5, 6, 1, 2, 3, 10, 4, 7, 0]

def get_cards(hand):
    """Return a list with string representation of a given 7 card hand."""
    card_str_no_suits = ''.join([c if ord(c) < 128 else '' for c in hand])
    cards = [LOOKUP[c] if not c.isnumeric() else int(c) for c in card_str_no_suits]
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

def rank_hand(hand):
    """Return a tuple with index representing hand strength and final 5 card hand."""
    cards = get_cards(hand)
    suits = get_suits(hand)
    for i, s in enumerate(suits):
        suits[i] = int(pow(2, (ord(s) % 9824)))
    hand = [(cards[i], suits[i]) for i in range(7)]
    print(hand)
    c = combinations(hand, 5)
    max_rank = 0
    win_index = 10
    for combo in c:
        index = calc_index(combo)
        if HANDRANKS[index] > max_rank:
            cs, ss = zip(*combo)
            max_rank = HANDRANKS[index]
            win_index = index
            wci = combo
            hand = cs
        # elif HANDRANKS[index] == max_rank:
        #     cs, ss = zip(*combo)
        #     score_1 = get_pokerscore(cs)
        #     score_2 = get_pokerscore()
    return (win_index, hand)

def calc_index(hand):
    """Return the integer index representing the strenght of the hand for a given 5 card hand and suits."""
    cs, ss = zip(*hand)
    v = 0
    for card in cs:
        o = int(pow(2, card * 4))
        v += o*((v // o & 15) + 1)
    v %= 15
    if v != 5:
        return v - 1
    else:
        s = 1<<cs[0]|1<<cs[1]|1<<cs[2]|1<<cs[3]|1<<cs[4]
    v -= 3 if (s/(s&-s) == 31) or (s == hex(0x403c)) else 1
    return v - (ss[0] == ss[0]|ss[1]|ss[2]|ss[3]|ss[4]) * (-5 if s == hex(0x7c00) else 1)

    


