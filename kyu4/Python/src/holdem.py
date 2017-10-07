"""Solution for https://www.codewars.com/kata/texas-holdem-poker/python."""

from collections import Counter

CARDS = list("23456789TJQKA")


class PokerHand(object):

    def __init__(self, hand):
        self.values = sorted(map(lambda x: self.CARDS.index(x[0]), hand.split(' ')), reverse=True)
        self.groups = []
        for i in sorted(list(set(Counter(self.values).values())), reverse=True):
            self.groups += sorted([x for x in Counter(self.values).items() if x[1] == i], key=lambda x: x[0], reverse=True)

        self.points = 0.0
        for i in range(0, len(self.groups)):
            self.points += self.groups[i][1] ** 2

        if PokerHand.is_straight(self.values):
            self.points += 7

    @staticmethod
    def is_straight(values):
        return len([x for x in range(0, 4) if values[x] - 1 == values[x + 1]]) == 4
