"""Tests for codewars kata https://www.codewars.com/kata/next-bigger-number-with-the-same-digits."""

import pytest


TEST_BIGGEST = [
    (9, True),
    (111, True),
    (531, True),
    (123, False),
    (9998, True),
    (54321, True),
]

TEST_INPUT = [
    (999, -1),
    (12, 21),
    (513, 531),
    (2017, 2071),
    (12345, 12354),
    (54312, 54321),
    (414, 441),
    (144, 414),
    (1234567890, 1234567908),
]


@pytest.mark.parametrize('n, result', TEST_INPUT)
def test_next_bigger(n, result):
    """Test next_bigger returns correct next bigger number."""
    from next_bigger import next_bigger
    assert next_bigger(n) == result

@pytest.mark.parametrize('n, result', TEST_BIGGEST)
def test_is_biggest(n, result):
    """Test is_biggest returns -1 ."""
    from next_bigger import is_biggest
    assert is_biggest(n) == result
