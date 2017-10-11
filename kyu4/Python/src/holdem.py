"""Solution for https://www.codewars.com/kata/texas-holdem-poker/python."""

from collections import Counter, defaultdict

CARDS = list("23456789TJQKA")

class PokerHand(object):

    def __init__(self, hand):
        self.values = sorted(map(lambda x: CARDS.index(x[0]), hand), reverse=True)

        self.val_cnt = defaultdict(int)
        for card in self.values:
            self.val_cnt[card] += 1

        self.groups = sorted(self.val_cnt.items(), reverse=True)

    @property
    def score(self):
        points = 0.0
        for k, v in self.val_cnt.items():
            points += v ** 2
        if self._is_straight:
            points += 7
        return points

    @property
    def _is_straight(self):
        """Return True if combination of board and hole cards make a straight."""
        cards = [k for k in self.val_cnt.keys()]
        for x in range(3):
            hand = sorted(cards[x:], reverse=True)
            if len(hand) < 5: return False
            if len([i for i in range(4) if hand[i] - 1 == hand[i + 1]]) == 4 or sum(hand) == 18:
                diff = [c for c in self.val_cnt.keys() if c not in hand]
                for c in diff:
                    del self.val_cnt[c]
                    self.groups = sorted(self.val_cnt.items(), reverse=True)
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
