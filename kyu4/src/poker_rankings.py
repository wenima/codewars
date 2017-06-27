"""Solution for https://www.codewars.com/kata/ranking-poker-hands/train/python."""

RESULT = ["Loss", "Tie", "Win"]

class PokerHand(object):
    """Create an object representing a Poker Hand based on an input of a 5 char
    string which represents the best 5 card combination from the player's hand
    and board cards.

    Methods:
        compare_with(self, villain): takes in Hero's Hand (self) and Villain's
        Hand (villain) and compares both hands according to rules of Texas Hold'em.
        Returns one of 3 strings (Win, Loss, Tie) based on wether Hero's hand
        is better than villain's hand.
        """

    def __init__(self, hand):
        """Initialize a poker hand based on a 10 character string input representing
        5 cards.
        """
        pass

    def compare_with(self, other):
        """Return one of 3 outcomes from result const."""
        pass
