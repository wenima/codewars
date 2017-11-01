def convert_suits(hand):
    """Return a string with suit symbols in place of character representation for a given hand."""
    return hand.replace('D', '♦').replace('H', '♥').replace('S', '♠').replace('C', '♣').replace(' ', '')
