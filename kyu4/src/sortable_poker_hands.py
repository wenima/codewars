"""Solution for https://www.codewars.com/kata/ranking-poker-hands/train/python."""

from operator import itemgetter
from collections import defaultdict
import functools

SUITS = {
    'S': ('Spades', 1),
    'H': ('Hearts', 1),
    'D': ('Diamonds', 1),
    'C': ('Clubs', 1)
}

RANKS = {
    'A': ('Ace', 14),
    '2': ('Two', 2),
    '3': ('Three', 3),
    '4': ('Four', 4),
    '5': ('Five', 5),
    '6': ('Six', 6),
    '7': ('Seven', 7),
    '8': ('Eight', 8),
    '9': ('Nine', 9),
    'T': ('Ten', 10),
    'J': ('Jack', 11),
    'Q': ('Queen', 12),
    'K': ('King', 13)
}

MADE_HANDS = {
    'straight flush': 9,
    '4 of a kind': 8,
    'full house': 7,
    'flush': 6,
    'straight': 5,
    'set': 4,
    'two pair': 3,
    'one pair': 1,
    'high card': 0
}

@functools.total_ordering
class PokerHand(object):
    """Create an object representing a Poker Hand based on an input of a
    string which represents the best 5 card combination from the player's hand
    and board cards.

    Attributes:
        high_card_vals: a list of card values sorted highest to lowest

        vals: a list of card's values

        suits: a list of card's suits

        hand: a sorted list of tuples representing face value and card value ordered
        by highest card in descending order

        val_cnt: a dict containing each card and the number of times it appears in the hand

        has_two_pair: True if hand is a 2 pair hand, else False

        hand_value: the hand value according to MADE_HANDS

        total_value: a tuple of int representing the value of the hand and a tuple of high cards

    Methods:
        compare_with(self, villain): takes in Hero's Hand (self) and Villain's
            Hand (villain) and compares both hands according to rules of Texas Hold'em.
            Returns one of 3 strings (Win, Loss, Tie) based on wether Hero's hand
            is better than villain's hand.
    Helper Methods:
        _is_straight(self): returns True if hand is a straight
        _is_flush(self): returns True if hand is a flush
        _has_two_pair(self): returns True if hand is a 2 pair hand
        """

    def __repr__(self):  return repr(self.passed_hand)

    def __lt__(self, other):
        return self._total_value < other._total_value

    def __eq__(self, other):
        return self.passed_hand == other

    def __init__(self, hand):
        """Initialize a poker hand based on a 10 character string input representing
        5 cards.
        """
        self.passed_hand = hand
        hand = hand.replace(' ', '')
        self.high_card_vals = []
        self.vals = [c for c in hand if c in RANKS.keys()]
        self.suits = [c for c in hand if c in SUITS.keys()]
        self.hand = sorted([(c, RANKS[c][1]) for c in self.vals], key=itemgetter(1), reverse=True)
        self.val_cnt = defaultdict(int)
        self.high_card_vals = sorted([RANKS[c][1] for c in self.vals], reverse=True)

        for card in self.vals:
            self.val_cnt[card] += 1

    @property
    def _is_five_high_straight(self):
        if sum([c[1] for c in self.hand]) == 28:
            return True

    @property
    def _is_straight(self):
        """Return True if hand is a straight."""
        if self._is_five_high_straight: return True
        previous_card = sorted(self.hand, key=itemgetter(1))[0][1] - 1
        for card in sorted(self.hand, key=itemgetter(1)):
            if previous_card + 1 != card[1]: return False
            previous_card = card[1]
        return True

    @property
    def _is_flush(self):
        """Return True if hand is a flush."""
        return True if len(set(self.suits)) == 1 else False

    @property
    def _has_two_pair(self):
        """Return value for 2pair if hand has made hand value of 2pair, else return 0."""
        sorted_d = sorted(self.val_cnt.items(), key=lambda x: x[1], reverse=True)
        return True if sorted_d[0][1] == 2 and sorted_d[1][1] == 2 else False

    @property
    def _hand_value(self):
        """Return a value based on hand strength."""
        hand_value = 0
        if self._has_two_pair: return 3
        if self._is_straight:
            if self._is_flush:
                return 9
            else:
                return 5
        if self._is_flush:
            return 6
        if len(set(self.val_cnt.values())) == 1: return hand_value
        sorted_d = sorted(self.val_cnt.items(), key=lambda x: x[1], reverse=True)
        while True:
            try:
                pair_plus = sorted_d.pop(0)[1]
            except IndexError:
                break
            if pair_plus == 4:
                return 8
            elif pair_plus == 3:
                hand_value = 4
            elif pair_plus == 2:
                if hand_value == 4:
                    return 7
                else:
                    return 1
        return hand_value

    @property
    def _total_value(self):
        """Return a tuple containing of an int representing hand value and a tuple
        of sorted high card values."""
        if self._is_five_high_straight:
            del self.high_card_vals[0]
            self.high_card_vals.append(1)
        return (self._hand_value, tuple(self.high_card_vals))
