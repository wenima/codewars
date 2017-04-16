"""Solution for kata https://www.codewars.com/kata/valid-braces."""

import queue as q


def valid_braces(s):
    """Return True if given string consisting of a mix of parens, brackets and
    braces is valid."""
    parens = q.LifoQueue(maxsize=len(s))
    braces = q.LifoQueue(maxsize=len(s))
    brackets = q.LifoQueue(maxsize=len(s))
    last_updated = q.LifoQueue(maxsize=len(s))
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
