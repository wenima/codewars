"""Solution for kata https://www.codewars.com/kata/valid-braces."""

import queue as q


def valid_braces(s):
    """Return True if given string consisting of a mix of parens, brackets and
    braces is valid."""
    queuesize = len(s)
    if queuesize < 1:
        return False
    parens = q.LifoQueue(queuesize)
    braces = q.LifoQueue(queuesize)
    brackets = q.LifoQueue(queuesize)
    last_updated = q.LifoQueue(queuesize)
    for p in s:
#         Tracer()()
        if p == '(':
            parens.put(p)
            last_updated.put(parens)
        elif p == '{':
            braces.put(p)
            last_updated.put(braces)
        elif p == '[':
            brackets.put(p)
            last_updated.put(brackets)
        else:
            try:
                if p == ')' and last_updated.get_nowait() == parens:
                    parens.get_nowait()
                elif p == '}' and last_updated.get_nowait() == braces:
                    braces.get_nowait()
                elif p == ']' and last_updated.get_nowait() == brackets:
                    brackets.get_nowait()
                else:
                    return False
            except q.Empty:
                return False
    if parens.empty() and braces.empty() and brackets.empty():
        return True
    return False
