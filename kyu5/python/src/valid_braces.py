"""Solution for kata https://www.codewars.com/kata/valid-braces."""

import queue as q


def valid_braces(s):
    para_stack = q.LifoQueue(maxsize=len(s))
    for p in s:
        if p == '(':
            para_stack.put(p)
        else:
            try:
                para_stack.get_nowait()
            except q.Empty:
                return False
    return para_stack.empty()
