"""Solution for https://www.codewars.com/kata/faberge-easter-eggs-crush-test."""

from math import sqrt, ceil

def height(eggs, tries, prev_floor=0):
    """Return the number of max floors a building can have given a number of tries and a number of eggs."""
    if not tries or not eggs: return 0
    count_drops = 0
    interval = egg1 = tries
    while not count_drops > tries:
        count_drops += 1
        interval -= 1
        egg1 += interval
    return egg1 + 1

def min_tries(floors):
    """
    Return the minimum tries it would take to find the breaking point given a number of floors and 2 eggs.

    The idea is to keep the number of drops constanst, wether the first egg drops on the first or last drop, i.e. we
    need to balance the worst case scenario by lowering the number of drops egg2 has to take.
    Therefore, we need to start dropping egg1 on floor x and go up x-1 for the next drop, then x-2 and so on
    We arrive at the formula: x + (x - 1) + (x -2) + ... == floors


    We can shorten this formula to:
    (min_tries * (min_tries + 1) / 2) == floors) where min_tries is x
    we need to solve for min_tries by transforming the above formula into a polynomial function
    min_tries ** 2 + min_tries -2 * floors == 0
    we can solve this by applying the quadratic formula:
    """
    return ceil((-1 + sqrt(1 + 8 * floors)) / 2)
