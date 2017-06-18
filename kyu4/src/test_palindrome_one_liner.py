"""Tests for codewars kata http://www.codewars.com/kata/one-line-task-palindrome-string/."""

import pytest


TEST = [
    (10, 'abcd'),
]


@pytest.mark.parametrize('n, s', TEST)
def test_make_palindrome(n, s, result):
    """Test palindrome is returned with length n."""
    from palindrome_one_liner import palindrome
    assert make_palindrome(n, s) == result
