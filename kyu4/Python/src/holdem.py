"""Solution for https://www.codewars.com/kata/texas-holdem-poker/python."""

from collections import Counter, defaultdict

CARDS = list("23456789TJQKA")


class Board(object):

    def __init__(self, board):
        self.board = ''.join(c for c in board)
        self.values = sorted(map(lambda x: self.CARDS.index(x[0]), board.split()), reverse=True)


class PokerHand(object):

    def __init__(self, hand):
        self.values = sorted(map(lambda x: CARDS.index(x[0]), hand), reverse=True)
        self.groups = []
        for i in sorted(list(set(Counter(self.values).values())), reverse=True):
            self.groups += sorted([x for x in Counter(self.values).items() if x[1] == i], key=lambda x: x[0], reverse=True)

        self.val_cnt = defaultdict(int)

        for card in self.values:
            self.val_cnt[card] += 1

    @property
    def _score(self):
        points = 0.0
        for i in range(0, len(self.groups)):
            points += self.groups[i][1] ** 2

        if self._is_straight():
            points += 7
        return points

    @property
    def _is_straight(self):
        """Return True if combination of board and hole cards make a straight."""
        hand = [k for k in self.val_cnt.keys()]
        for x in range(2):
            hand = sorted(hand[x:], reverse=True)
            if sum(hand) == 18: return True
            if len(hand) < 5: return False
            if len([i for i in range(4) if hand[i] - 1 == hand[i + 1]]) == 4: return True
        return False
