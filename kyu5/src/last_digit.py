from itertools import count

def get_sequence(a, b):
    for n in (a**x % 10 for x in count(1)):
        yield n

def last_digit(a, b):
    if b == 0:
        return 1
    if a**1 % 10 == 0:
        return 0
    seq = []
    while True:
        for n in get_sequence(a, b):
            if n == a**1 % 10 and seq:
                break
            else:
                seq.append(n)
        break
    if len(seq) < 2 and seq:
        return seq[0]
    return seq[len(seq) - 1] if b % len(seq) == 0 else seq[b % len(seq) - 1]
