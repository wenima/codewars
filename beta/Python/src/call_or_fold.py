
def new_deck():
    """Return a 52 deck of cards as a list."""
    rs = [rank + suit for rank in "A23456789TJQK" for suit in "CDHS"]
    return rs

def convert_suits(hand):
    """Return a string with suit symbols in place of character representation for a given hand."""
    return hand.replace('D', '♦').replace('H', '♥').replace('S', '♠').replace('C', '♣').replace(' ', '')
