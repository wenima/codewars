"""Solution for kata https://www.codewars.com/kata/valid-parentheses/python.
Please note that function names sometimes do not follow the suggested convention of
snake_case due to the kata's author not following it."""

def validParentheses(s):
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
