"""Tests for codewars kata http://www.codewars.com/kata/one-line-task-palindrome-string/."""

import pytest


TEST = [
    (10, 'abcd', 'abcdaadcba'),
]


@pytest.mark.parametrize('n, s, result', TEST)
def test_make_palindrome(n, s, result):
    """Test palindrome is returned with length n."""
    from palindrome_one_liner import palindrome
    assert palindrome(n, s) == result
