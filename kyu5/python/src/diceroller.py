"""Module to solve the code-kata https://www.codewars.com/kata/rpg-dice-roller.
"""

import re
from random import randint
from collections import OrderedDict


def normalize_input(s):
    try:
        s = s.replace(' ', '')
    except AttributeError:
        return False
    pattern = r'^[0-9]*d[1-9]+(?:[+-]?\d)*$'
    m = re.match(pattern, s)
    return m.group() if m else False


def validate_input(s):
    """Return True if input follows the dice notation or False."""
    try:
        m = normalize_input(s)
    except AttributeError:
        return False
    return True if m else False

def get_modifiers(s):
    """Return a list of modifiers of the given dice notation."""
    pattern = r'[+-]+[1-9][0-9]*'
    return sum([int(match) for match in re.findall(pattern, s)])


def roll(s, verbose=False):
    """Roll Dice defined in input string and apply modifieres if present.

    Keyword arguments:
    output -- takes either 'summed' or 'verbose' (default: 'summed')
    'summed' will sum up the roll plus modifieres and return an integers
    'verbose' returns an object with a list containing all rolls and the sum of
    all modifiers. If no modifiers are given, returns zero
    """
    throw = OrderedDict()
    d = normalize_input(s)
    if validate_input(s):
        m = re.search(r'^([0-9])*d([1-9][0-9]*)', d)
        if m.group(1) == None:
            no_of_dies = 1
        else:
            no_of_dies = m.group(1)
        die = m.group(2)
        throw['dice'] = [randint(1, int(die)) for i in range(int(no_of_dies))]
        throw['modifier'] = get_modifiers(d)
        if verbose:
            return dict(throw)
        else:
            return sum(throw['dice']) + throw['modifier']
    else:
        return False
