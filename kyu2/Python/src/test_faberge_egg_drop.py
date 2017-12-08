"""Tests for https://www.codewars.com/kata/faberge-easter-eggs-crush-test."""

import pytest

TEST_EGGS = [
    (0, 14, 0),
    (2, 0, 0),
    (2, 14, 105),
]

@pytest.mark.parametrize('eggs, tries, result', TEST_EGGS)
def test_height(eggs, tries, result):
    """Test that function height returns correct result."""
    from faberge_egg_drop import height
    assert height(eggs, tries) == result

def test_min_tries_2_eggs():
    """Test that min_tries function returns correct min_tries to cover k floors."""
    from faberge_egg_drop import min_tries
    assert min_tries(100) == 14