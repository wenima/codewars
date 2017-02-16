"""Tests for kata find_sum."""

import pytest

TESTS = [
        ([[20, 20, 10, 10],
          [10, 20, 10, 10],
          [10, 20, 20, 20],
          [10, 10, 10, 20]], 140),
        ([[10, 10, 10, 10],
          [10, 10, 10, 10],
          [10, 10, 10, 10],
          [10, 10, 10, 20]], 80),
]

@pytest.mark.parametrize('m, result', TESTS)
def test_find_sum(m, result):
    """Test that the largest sum is returned for the input matrix."""
    from find_sum import find_sum
    assert find_sum(m) == result
