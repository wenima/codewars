from random import shuffle

def new_deck():
    """Return a 52 deck of cards as a list."""
    rs = [rank + suit for rank in "A23456789TJQK" for suit in "CDHS"]
    return rs

def draw_cards(n, deck, dead=[], random=None):
    """Return n cards from a shuffled deck."""
    for card in dead:
        pos = deck.index(card)
        del deck[pos]
    if random:
        random.shuffle(deck)
    else:
        shuffle(deck)
    return [deck.pop() for _ in range(n)]

def convert_suits(hand):
    """Return a string with suit symbols in place of character representation for a given hand."""
    return hand.replace('D', '♦').replace('H', '♥').replace('S', '♠').replace('C', '♣').replace(' ', '')

def complete_board(deck, board, hero, villain):
    """Return a 5 card board given a an existing board and hole cards from 2 players."""
    if len(board) == 5: return board #board already has been dealt a river, no more cards to deal
    dead = board + hero + villain #dead cards which cannot be in the deck
    for card in draw_cards(5 - len(board), deck, dead):
        board.append(card)
    return board
        


