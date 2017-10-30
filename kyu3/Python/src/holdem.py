"""Tests for codewars kata https://www.codewars.com/kata/texas-holdem-hands/."""

import re
from collections import Counter
from itertools import combinations
from operator import itemgetter

HANDS = [
    "four-of-a-kind", "straight-flush", "straight", "flush", "nothing",
    "pair", "two pair", "straight-flush", "three-of-a-kind", "full house", "-Invalid-"
    ]

LOOKUP = {
    'A' : 14,
    'K' : 13,
    'Q' : 12,
    'J' : 11,
    'T' : 10,
    }

HANDRANKS = [8, 9, 5, 6, 1, 2, 3, 10, 4, 7, 0]

CARDSLOOKUP = {
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: '10',
    11: 'J',
    12: 'Q',
    13: 'K',
    14: 'A'
}

def get_cards(heroes_hand):
    """Return a list with string representation of a given 7 card hand."""
    heroes_hand = re.sub(r"10", "T", heroes_hand)
    card_str_no_suits = ''.join([c if ord(c) < 128 else '' for c in heroes_hand])
    cards = [LOOKUP[c] if not c.isnumeric() else int(c) for c in card_str_no_suits]
    return cards

def get_suits(heroes_hand):
    """Return a list with the suits of the hand."""
    pattern = re.compile('♠|♣|♥|♦')
    return list(re.findall(pattern, heroes_hand))

def get_pokerscore(heroes_hand):
    """Return a unique value representing overall hand strength."""
    c = Counter(heroes_hand)
    a = sorted(heroes_hand, key=lambda x: (c[x], x), reverse=True)
    return a[0]<<16|a[1]<<12|a[2]<<8|a[3]<<4|a[4]

def rank_hand(heroes_hand):
    """Return a tuple with index representing hand strength and final 5 card hand."""
    cards = get_cards(heroes_hand)
    suits = get_suits(heroes_hand)
    for i, s in enumerate(suits):
        suits[i] = int(pow(2, (ord(s) % 9824)))
    heroes_hand = [(cards[i], suits[i]) for i in range(7)]
    c = combinations(heroes_hand, 5)
    max_rank = 0
    win_index = 10
    for combo in c:
        index = calc_index(combo)
        if HANDRANKS[index] > max_rank:
            cs, ss = zip(*combo)
            max_rank = HANDRANKS[index]
            win_index = index
            wci = cs
            heroes_hand = cs
        elif HANDRANKS[index] == max_rank:
            cs, ss = zip(*combo)
            score_1 = get_pokerscore(cs)
            score_2 = get_pokerscore(wci)
            if (score_1 > score_2):
                heroes_hand = cs
                wci = cs
    return (win_index, heroes_hand)

def calc_index(heroes_hand):
    """Return the integer index representing the strenght of the hand for a given 5 card hand and suits."""
    cs, ss = zip(*heroes_hand)
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

def get_ordered_hand(index, heroes_hand, pairs, filtered):
    """Return a list of high cards for a given hand."""
    if index in [1, 2, 3, 4, 7]: return heroes_hand[:5] # straights&flushes
    elif index == 8: return pairs + filtered[:2] # three-of-a kind
    elif index == 5: return pairs + filtered[:3] # pairs
    elif index == 6 or index == 0: return pairs + filtered[:1] # 2pair & four-of-a-kind
    # full-house - we need to get a weighted sorted to display the set first and then the pair
    elif index == 9:
        fh = Counter(heroes_hand)
        return [x[0] for x in sorted(fh.items(), key=itemgetter(1), reverse=True)]


def hand(hole_cards, board):
    """Return a dict with keys: 'type' and 'ranks' describing the type of hand and high cards."""
    heroes_hand = ''.join(hole_cards + board)
    index, final_hand = rank_hand(heroes_hand)
    c = Counter(final_hand)
    pairs = [k for k, v in dict(c).items() if v > 1]
    filtered = [n for n in final_hand if n not in pairs]
    sorted_hand = sorted(final_hand, reverse=True)
    pairs.sort(reverse=True)
    filtered.sort(reverse=True)
    ordered_hand = get_ordered_hand(index, sorted_hand, pairs, filtered)
    out = {'type': HANDS[index], 'ranks': [CARDSLOOKUP[card] for card in ordered_hand]}
    return out
