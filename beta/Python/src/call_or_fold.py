import re
from random import shuffle
from collections import Counter
from itertools import combinations

HANDS_STRENGHT_MAPPING = {
    0: 8, #four of a kind
    1: 9, #straight flush
    2: 5, #straight
    3: 6, #flush
    4: 0, #high card
    5: 1, #pair
    6: 3, #two pair
    7: 9, #straight-flush/royal flush
    8: 4, #three of a kind
    9: 7, #full house
    10: -1 #Invalid
}

LOOKUP = {
    'A' : 14,
    'K' : 13,
    'Q' : 12,
    'J' : 11,
    'T' : 10,
    }

HANDRANKS = [8, 9, 5, 6, 1, 2, 3, 10, 4, 7, 0]

def new_deck(dead=[]):
    """Return a 52 deck of cards as a list."""
    deck = [rank + suit for rank in "A23456789TJQK" for suit in "CDHS"]
    for card in dead:
        pos = deck.index(card)
        del deck[pos]
    return deck

def draw_cards(n, deck, dead=[], random=None):
    """Return n cards from a shuffled deck."""
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

def get_cards(heroes_hand):
    """Return a list with string representation of a given 7 card hand."""
    card_str_no_suits = ''.join([c if ord(c) < 128 else '' for c in heroes_hand])
    cards = [LOOKUP[c] if not c.isnumeric() else int(c) for c in card_str_no_suits]
    return cards

def get_suits(heroes_hand):
    """Return a list with the suits of the hand."""
    pattern = re.compile('♠|♣|♥|♦')
    return list(re.findall(pattern, heroes_hand))

def get_pokerscore(heroes_hand):
    """Return a unique value representing overall hand strength."""
    c = Counter(heroes_hand)
    a = sorted(heroes_hand, key=lambda x: (c[x], x), reverse=True)
    return a[0]<<16|a[1]<<12|a[2]<<8|a[3]<<4|a[4]

def calc_index(heroes_hand):
    """Return the integer index representing the strenght of the hand for a given 5 card hand and suits."""
    cs, ss = zip(*heroes_hand)
    v = 0
    for card in cs:
        o = int(pow(2, card * 4))
        v += o*((v // o & 15) + 1)
    v %= 15
    if v != 5:
        return v - 1
    else:
        s = 1<<cs[0]|1<<cs[1]|1<<cs[2]|1<<cs[3]|1<<cs[4]
    v -= 3 if (s/(s&-s) == 31) or (s == hex(0x403c)) else 1
    return v - (ss[0] == ss[0]|ss[1]|ss[2]|ss[3]|ss[4]) * (-5 if s == hex(0x7c00) else 1)

def rank_hand(heroes_hand):
    """Return a tuple with index representing hand strength and final 5 card hand."""
    cards = get_cards(heroes_hand)
    suits = get_suits(heroes_hand)
    for i, s in enumerate(suits):
        suits[i] = int(pow(2, (ord(s) % 9824)))
    heroes_hand = [(cards[i], suits[i]) for i in range(7)]
    c = combinations(heroes_hand, 5)
    max_rank = 0
    win_index = 10
    for combo in c:
        cs, ss = zip(*combo)
        index = calc_index(combo)
        if HANDRANKS[index] > max_rank:
            max_rank = HANDRANKS[index]
            win_index = index
            wci = cs
            heroes_hand = cs
        elif HANDRANKS[index] == max_rank:
            score_1 = get_pokerscore(cs)
            score_2 = get_pokerscore(wci)
            if score_1 > score_2:
                heroes_hand = cs
                wci = cs
    return (win_index, heroes_hand)

def get_best_hand(hand):
    """Return a list of integers representing the best 5 card combination from a given board and hole_cards."""
    hand = convert_suits(''.join(hand))
    return rank_hand(hand)

def compare_hands(board, hero, villain):
    """Return a string as the outcome of hero after comparing to villains hand to be one of 3: Win, Loss, Tie."""
    if len(board) < 5:
        dead = board + hero + villain
        for card in draw_cards(5 - len(board), new_deck(dead)):
            board.append(card)
    hero_index, heroes_hand = get_best_hand(board + hero)
    villain_index, villains_hand = get_best_hand(board + villain)
    if HANDS_STRENGHT_MAPPING[hero_index] > HANDS_STRENGHT_MAPPING[villain_index]:
        return 'Hero'
    elif HANDS_STRENGHT_MAPPING[hero_index] < HANDS_STRENGHT_MAPPING[villain_index]:
        return 'Villain'
    else:
        hero_score = get_pokerscore(heroes_hand)
        villain_score = get_pokerscore(villains_hand)
        if hero_score > villain_score:
            return 'Hero'
        elif hero_score < villain_score:
            return 'Villain'
        else:
            return 'Tie'

def calc_equity(deck, board, hero, villain, mode='monte-carlo', trials=1):
    """Return a float as the equity for hero."""
    if mode == 'exhaustive':
        combos = combinations(deck, 2)
    else:
       dead = board + hero + villain
       combos = [tuple(draw_cards(5 - len(board), new_deck(dead=dead))) for _ in range(trials)]
       print(combos)
    runs = []
    for combo in combos:
        runs.append(compare_hands(board + list(combo), hero, villain))
    c = Counter(runs)
    print(c)
    return round(((c['Hero'] + (c['Tie'] // 2)) / sum(c.values())) * 100, 2)
    


    
        


