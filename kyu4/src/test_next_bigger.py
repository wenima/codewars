"""Tests for codewars kata https://www.codewars.com/kata/next-bigger-number-with-the-same-digits."""

import pytest


TEST_INPUT = [
    (9, -1),
    (111, -1),
    (531, -1),
]


@pytest.mark.parametrize('n, result', TEST_PS)
def test_next_bigger(n, result):
    """Test next_bigger returns correct next bigger number."""
    from next_bigger import next_bigger
    assert next_bigger(n) == result
