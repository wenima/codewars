"""Tests for codewars kata https://www.codewars.com/kata/car-park-escape/."""

import pytest


TEST_INPUT = [
    ([
    [1, 0, 0, 0, 2],
    [0, 0, 0, 0, 0]], ["L4", "D1", "R4"]),
    ([
    [2, 0, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0]], ["R3", "D2", "R1"]),
    ([
    [0, 2, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0]], ["R3", "D3"]),
    ([
    [1, 0, 0, 0, 2],
    [0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]], ["L4", "D1", "R4", "D1", "L4", "D1", "R4"]),
    ([
    [0, 0, 0, 0, 2]], []),
]


@pytest.mark.parametrize('carpark, escape', TEST_INPUT)
def test_alphanumeric(carpark, escape):
    """Test that for a given carpark, the function returns a valid escape route."""
    from carpark import escape
    assert escape(carpark) == escape
