"""Tests for what is my equity kata using the codewars testing framework."""
from random import shuffle
from collections import Counter
from itertools import combinations
from math import ceil
from call_or_fold import new_deck, draw_cards, get_equity

# nut flush draw + backdoor straight draw vs set
test.assert_equals(get_equity(['JS', '9S', 'KH'], ['AS', '3S'], ['KS', 'KD']), 25.45)

# nut flush draw + overcard draw vs underpair
test.assert_equals(get_equity(['JS', '9S', 'KH', '2H'], ['AS', '3S'], ['6H', '6D']), 27.27)

# open-ended straight draw + backdoor flush draw vs overpair
test.assert_equals(get_equity(['2D', '8D', '9S'], ['JD', 'TH'], ['AS', 'AH']), 36.97)

# nut flush draw + inside straight draw + overcard vs pair
test.assert_equals(get_equity(['5S', '4S', 'KH', '9D'], ['AS', '3S'], ['KS', 'QD']), 31.82)

# nut flush draw + inside straight draw + overcard vs pair
test.assert_equals(get_equity(['5S', '4S', 'KH'], ['AS', '3S'], ['KS', 'QD']), 52.63)

# drawing dead
test.assert_equals(get_equity(['AS', 'AH', 'KH'], ['KD', 'QC'], ['AD', 'KC']), 0)

# getting coolered pre-flop
test.expect(15.36 < get_equity([], ['KH', 'KD'], ['AS', 'AD']) < 19.36, "all-in preflop equity is more than 2% off")

# various different common scenarios
test.assert_equals(get_equity(['JS', '9S', 'KH'], ['AS', '3S'], ['QH', 'QD']), 44.75) #nut flush draw + backdoor straight + overcard vs pair
test.assert_equals(get_equity(['JS', '9S', 'KH'], ['AS', '3S'], ['6H', '6D']), 48.38) #nut flush draw + backdoor straight draw + overcard vs underpair
test.assert_equals(get_equity(['JS', '9S', 'KH'], ['AS', '3S'], ['KS', 'JH']), 32.73) #nut flush draw vs top two pair with one of our outs dead (K of Spades)
test.assert_equals(get_equity(['8H', '2D', '9S'], ['7D', 'JH'], ['AS', 'AH']), 20.30) #inside straight draw (gutshot) vs overpair
test.assert_equals(get_equity(['8H', '6D', '9D'], ['TD', 'QH'], ['AS', 'AH']), 36.36) #double inside straight draw (double gutter) + backdoor flush draw vs overpair



def equity(board, hero, villain):
    """Return a float as the equity for hero."""
    from call_or_fold import calc_equity
    if not board:
        eq = calc_equity(board, hero, villain, mode='monte-carlo', trials=3000)
    else:
        eq = calc_equity(board, hero, villain, mode='exhaustive')
    return round(eq, 2)
    

# random tests for turn equity
for _ in range(5):
    deck = new_deck()
    hero = draw_cards(2, deck)
    villain = draw_cards(2, deck, dead=hero)
    board = draw_cards(4, deck, dead=hero+villain)
    test.assert_equals(get_equity(board, hero, villain), equity(board, hero, villain))
    
# random tests for flop equity

for _ in range(2):
    deck = new_deck()
    hero = draw_cards(2, deck)
    villain = draw_cards(2, deck, dead=hero)
    board = draw_cards(3, deck, dead=hero+villain)
    test.assert_equals(get_equity(board, hero, villain), equity(board, hero, villain))