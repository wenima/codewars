"""Solution for https://www.codewars.com/kata/faberge-easter-eggs-crush-test."""

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
