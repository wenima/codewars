"""Solution for https://www.codewars.com/kata/texas-holdem-poker/python."""

from collections import Counter, defaultdict
from operator import itemgetter

CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

class PokerHand(object):

    def __init__(self, hand):
        self.values = sorted([CARDS.index(c) for c in hand], reverse=True)

        self.val_cnt = defaultdict(int)
        for card in self.values:
            self.val_cnt[card] += 1

        self.groups = sorted(self.val_cnt.items(), key=itemgetter(1, 0), reverse=True)

    @property
    def score(self):
        points = 0.0
        if self._is_straight:
            points += 7
        cards = 0
        for k, v in self.groups:
            if cards + v > 5: continue
            cards += v
            points += v ** 2
            if cards == 5: return points

    @property
    def _is_straight(self):
        """Return True if combination of board and hole cards make a straight."""
        cards = [k for k in self.val_cnt.keys()]
        for x in range(3):
            hand = sorted(cards[x:], reverse=True)
            if len(hand) < 5: return False
            straight = [hand[i] for i in range(4) if hand[i] - 1 == hand[i + 1]]
            if len(straight) == 4:
                last_card = hand.index(straight[-1]) + 1
                straight.append(hand[last_card])
                self.values = straight
                self.val_cnt = defaultdict(int)
                for card in self.values:
                    self.val_cnt[card] += 1
                    self.groups = sorted(self.val_cnt.items(), key=itemgetter(1, 0), reverse=True)
                return True
        return False

    def compare_with(self, villain):
        """Return the winner given 2 pokerhand objects or return tie."""
        if villain.score > self.score:
            return 'B'
        elif villain.score < self.score:
            return 'A'
        else:
            for i in range(0, len(self.groups)):
                if villain.groups[i][0] > self.groups[i][0]:
                    return 'B'
                elif villain.groups[i][0] < self.groups[i][0]:
                    return 'A'
            return 'AB'

def texasHoldem(board, hole_cards_hero, hole_cards_villain):
    """Return the winning hand given board cards and 2 player's hands."""
    hero = PokerHand(board + hole_cards_hero)
    villain = PokerHand(board + hole_cards_villain)
    return hero.compare_with(villain)
