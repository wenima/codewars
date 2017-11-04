from random import Random
from collections import Counter
import pytest

BOARD_RUNOUTS = [
    (['JS', '9S', 'KH'], ['AS', '3S'], ['KS', 'KD'], 5),
    ([], ['AS', '3S'], ['KS', 'KD'], 5),
]

DETERMINISTIC_DRAWS = [
    ['TH', '7C'],
    ['3H', '6S'],
    ['6D', '6C'],
    ['8H', 'JC'],
    ['2C', '6D'],
    ['2H', 'QS'],
    ['8C', 'QS']
]

FINAL_HAND = [
    (['JS', '9S', 'KH'], DETERMINISTIC_DRAWS[0], ['AS', '3S'], (4, [14, 13, 11, 10, 9])),
    (['JS', '9S', 'KH'], DETERMINISTIC_DRAWS[1], ['AS', '3S'], (3, [14, 11, 9, 6, 3])),
    (['JS', '9S', 'KH'], DETERMINISTIC_DRAWS[2], ['AS', '3S'], (5, [14, 13, 11, 6, 6])),
    (['JS', '9S', 'KH'], DETERMINISTIC_DRAWS[3], ['AS', '3S'], (5, [14, 13, 11, 11, 9])),
    (['JS', '9S', 'KH'], DETERMINISTIC_DRAWS[4], ['AS', '3S'], (4, [14, 13, 11, 9, 6])),
    (['JS', '9S', 'KH'], DETERMINISTIC_DRAWS[5], ['AS', '3S'], (3, [14, 12, 11, 9, 3])),
    (['JS', '9S', 'KH'], DETERMINISTIC_DRAWS[6], ['AS', '3S'], (3, [14, 12, 11, 9, 3])),
    (['JS', '9S', 'KH'], ['AH', 'AD'], ['AS', '3S'], (8, [14, 14, 14, 13, 11])),
]

HERO_VS_VILLAIN = [
    (DETERMINISTIC_DRAWS[0], ['AS', '3S'], 'Villain'),
    (DETERMINISTIC_DRAWS[1], ['AS', '3S'], 'Hero'),
    (DETERMINISTIC_DRAWS[2], ['AS', '3S'], 'Villain'),
    (DETERMINISTIC_DRAWS[3], ['AS', '3S'], 'Villain'),
    (DETERMINISTIC_DRAWS[4], ['AS', '3S'], 'Villain'),
    (DETERMINISTIC_DRAWS[5], ['AS', '3S'], 'Hero'),
    (DETERMINISTIC_DRAWS[6], ['AS', '3S'], 'Hero'),
    (['AH', 'AD'], ['AS', '3S'], 'Villain'),
]

EQUITY_CALCS_EXHAUSTIVE = [
    (['JS', '9S', 'KH'], ['AS', '3S'], ['KS', 'KD'], 'exhaustive', 25.45), #nut flush draw vs set
    (['2D', '8D', '9S'], ['JS', 'TH'], ['AS', 'AH'], 'exhaustive', 34.24), #open-ended straight draw vs overpair
    (['JS', '9S', 'KH'], ['AS', '3S'], ['AH', 'AD'], 'exhaustive', 36.82), #nut flush draw vs overpair
    (['JS', '9S', 'KH'], ['AS', '3S'], ['QH', 'QD'], 'exhaustive', 44.75), #nut flush draw vs pair
    (['JS', '9S', 'KH'], ['AS', '3S'], ['6H', '6D'], 'exhaustive', 48.38), #nut flush draw vs underpair
    (['JS', '9S', 'KH'], ['AS', '3S'], ['KD', 'JH'], 'exhaustive', 32.83), #nut flush draw vs top two pair
    (['JS', '9S', 'KH'], ['AS', '3S'], ['KS', 'JH'], 'exhaustive', 32.73), #nut flush draw vs top two pair with one of our outs dead (K of Spades)
    (['2D', '8D', '9S'], ['JD', 'TD'], ['AS', 'AH'], 'exhaustive', 56.26), #open-ended straight draw + flush draw vs overpair
    (['2D', '8D', '9S'], ['JD', 'TH'], ['AS', 'AH'], 'exhaustive', 36.97), #open-ended straight draw + backdoor flush draw vs overpair
    (['8H', '2D', '9S'], ['7D', 'JH'], ['AS', 'AH'], 'exhaustive', 20.30), #inside straight draw (gutshot) vs overpair
    (['8H', '6D', '9D'], ['TD', 'QH'], ['AS', 'AH'], 'exhaustive', 36.36), #double inside straight draw (double gutter) + backdoor flush draw vs overpair
]

# EQUITY_CALCS_MC = [
#     (['JS', '9S', 'KH'], ['AS', '3S'], ['KS', 'KD'], 'monte-carlo', 3000, 25),
#     ([], ['AS', '3S'], ['KS', 'KD'], 'monte-carlo', 3000, 33),
#     ([], ['KH', 'KD'], ['AS', 'AD'], 'monte-carlo', 3000, 18),
#     ([], ['AH', 'KD'], ['QH', 'QD'], 'monte-carlo', 3000, 44),
# ]

INPUT = [
    ('KS AS TS QS JS', 'K♠A♠T♠Q♠J♠'),
    ('2D AH 4H 5S KC', '2♦A♥4♥5♠K♣'),
]

@pytest.fixture
def deck():
    from call_or_fold import new_deck
    deck = new_deck()
    return deck

@pytest.mark.parametrize('hand, result', INPUT)
def test_convert_suits(hand, result):
    """Test that convert_suits returns a string with actual suits in place of characters representing the suit."""
    from call_or_fold import convert_suits
    assert convert_suits(hand) == result

def test_new_deck(deck):
    """Test that a new deck with 52 cards is returned and all suits are correct."""
    for suit in ['C', 'H', 'S', 'D']:
        assert len([c for c in deck if c[1] == suit]) == 13

def test_new_deck_with_dead_cards():
    """Test that a deck is returned minus dead cards."""
    from call_or_fold import new_deck
    dead = ['AS', 'AH']
    deck = new_deck(dead)
    assert 'AS' not in deck
    assert len(deck) == 50

def test_draw_cards(deck):
    """Test that dead cards are handled correctly when drawing cards from a shuffled deck."""
    from call_or_fold import draw_cards
    drawn = draw_cards(52, deck)
    assert len(drawn) == 52
    assert not deck

def test_draw_cards_deterministic():
    """Test that same cards are drawn passing in a seed."""
    from call_or_fold import draw_cards, new_deck
    random = Random(333)
    dead = ['JS', '9S', 'KH', 'AS', '3S']
    out = []
    for _ in range(7):
        deck = new_deck(dead)
        out.append(draw_cards(2, deck, random=random))
    for idx, draw in enumerate(out):
        assert draw == DETERMINISTIC_DRAWS[idx]

@pytest.mark.parametrize('board, hero, villain, result', BOARD_RUNOUTS)
def test_complete_board(deck, board, hero, villain, result):
    """Test that complete_board returns a board of 5 unique cards."""
    from call_or_fold import complete_board
    board = complete_board(deck, board, hero, villain)
    assert len(board) == result

@pytest.mark.parametrize('board, runout, hole_cards, result', FINAL_HAND)
def test_get_best_hand(board, runout, hole_cards, result):
    """Test that given a board, a runout and hole_cards, the best 5 card combination is returned."""
    from call_or_fold import get_best_hand
    index, best_hand = get_best_hand(board + runout + hole_cards)
    assert Counter(best_hand) == Counter(result[1])
    assert index == result[0]

@pytest.mark.parametrize('runout, hero, result', HERO_VS_VILLAIN)
def test_compare_hands(runout, hero, result):
    """Test that given 2 hands, the winner is correctly returned."""
    from call_or_fold import compare_hands
    board = ['JS', '9S', 'KH'] + runout
    villain = ['KS', 'KD']
    assert compare_hands(board, hero, villain) == result

@pytest.mark.parametrize('board, hero, villain, mode, result', EQUITY_CALCS_EXHAUSTIVE)
def test_calc_equity_exhaustive(board, hero, villain, mode, result):
    """Test that simulations of runouts given board, hero and villain match expected result."""
    from call_or_fold import calc_equity, new_deck
    dead = hero + villain + board
    deck = new_deck(dead=dead)
    assert calc_equity(deck, board, hero, villain, mode=mode) == result

# @pytest.mark.parametrize('board, hero, villain, mode, trials, result', EQUITY_CALCS_MC)
# def test_calc_equity_monte_carlo(board, hero, villain, mode, trials, result):
#     """Test that simulations of runouts given board, hero and villain match expected result."""
#     from call_or_fold import calc_equity, new_deck
#     dead = hero + villain + board
#     deck = new_deck(dead=dead)
#     eq = calc_equity(deck, board, hero, villain, mode=mode, trials=trials)
#     assert eq == pytest.approx(result, abs=3)



