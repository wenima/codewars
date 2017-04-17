"""Tests for codewars kata https://www.codewars.com/kata/next-bigger-number-with-the-same-digits."""

import pytest


TEST_BIGGEST = [
    (9, -1),
    (111, -1),
    (531, -1),
    (123, 0),
]


# @pytest.mark.parametrize('n, result', TEST_PS)
# def test_next_bigger(n, result):
#     """Test next_bigger returns correct next bigger number."""
#     from next_bigger import next_bigger
#     assert next_bigger(n) == result

@pytest.mark.parametrize('n, result', TEST_BIGGEST)
def test_is_biggest(n, result):
    """Test is_biggest returns -1 ."""
    from next_bigger import is_biggest
    assert is_biggest(n) == result
