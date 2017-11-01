import pytest

INPUT = [
    ('KS AS TS QS JS', 'K♠A♠T♠Q♠J♠'),
    ('2D AH 4H 5S KC', '2♦A♥4♥5♠K♣'),
]

@pytest.mark.parametrize('hand, result', INPUT)
def test_convert_suits(hand, result):
    """Test that convert_suits returns a string with actual suits in place of characters representing the suit."""
    from call_or_fold import convert_suits
    assert convert_suits(hand) == result

def test_new_deck():
    """Test that a new deck with 52 cards is returned and all suits are correct."""
    from call_or_fold import new_deck
    deck = new_deck()
    for suit in ['C', 'H', 'S', 'D']:
        assert len([c for c in deck if c[1] == suit]) == 13

def test_draw_cards():
    """Test that dead cards are handled correctly when drawing cards from a shuffled deck."""
    from call_or_fold import draw_cards, new_deck
    deck = new_deck()
    dead = ['AS', 'AH']
    drawn = draw_cards(50, deck, dead=dead)
    assert 'AS' not in drawn
    assert len(drawn) == 50
    assert not deck
    