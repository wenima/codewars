"""Solution for kata https://www.codewars.com/kata/valid-parentheses/python."""

def valid_parentheses(s):
    """Return a boolean if given string has valid parentheses."""
    stack = []
    for c in s:
        if c not in ['(', ')']:
            continue
        if c == '(':
            stack.append(c)
        else:
            try:
                stack.pop()
            except IndexError:
                return False
    return len(stack) == 0
