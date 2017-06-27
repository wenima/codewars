"""Solution for codewars kata https://www.codewars.com/kata/1-s-0-s-and-wildcards/train/python."""

from collections import defaultdict


def possibilities(s):
    """Retun a list which contains all possibilites for a given string including
    ? as wildcards, where ? is replaced with 1 and 0."""
    d = defaultdict(list)
    last = 0
    for idx, c in enumerate(s):
        if c == '?':
            if d:
                for ss in d[last]:
                    d[idx].append(ss + s[last + 1:idx] + '0')
                    d[idx].append(ss + s[last + 1:idx] + '1')
            else:
                d[idx].append(s[:idx] + '0')
                d[idx].append(s[:idx] + '1')
            last = idx
    return d[len(s) - 1]
