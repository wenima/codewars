from itertools import cycle, accumulate

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ ?!@#&()|<>.:=-+*/0123456789'

def get_indeces(lines):
    indeces = []
    for w in lines:
        indeces.append([ALPHABET.index(c) for c in w])
    return indeces


def get_flaps(rotors, lines):
    flaps = []
    for r in rotors:
        flaps.append(accumulate(r))
    return flaps
    

def get_idx_flap(index, flap):
    for t in zip(index, flap):
        yield t


def flap_display(lines, rotors):
    indeces = get_indeces(lines)
    flaps = get_flaps(rotors, lines)
    out = []
    for i in range(len(lines)):
        out_line = []
        for t in get_idx_flap(indeces[i], flaps[i]):
            for idx, c in enumerate(cycle(ALPHABET)):
                if idx == sum(t):
                    out_line.append(c)
                    break
        out.append(out_line)
    return [''.join(l) for l in out]
