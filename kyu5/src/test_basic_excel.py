"""Tests for codewars kata https://www.codewars.com/kata/56055244356dc5c45c00001e."""

import pytest


#try to use tuples for input var
COUNTIF_INPUT = [
    ([1, 3, 5, 7, 9], 3, 1),
    (["John","Steve","John"], "John"), 2),
]

SUMIF_INPUT = [
    ([2, 4, 6, -1, 3, 1.5],">0", 16.5),
]

AVERAGEIF_INPUT = [
    ([99, 95.5, 0, 83],"<>0", 92.5),
]


@pytest.mark.parametrize('elements, comparator, result', TEST_INPUT)
def test_countif(elements, comparator, result):
    """Test function returns number of occurences of comparator in elements."""
    from basic_excel import countif
    assert countif(elements, comparator) == result

@pytest.mark.parametrize('elements, comparator, result', TEST_INPUT)
def test_sumif(elements, comparator, result):
    """Test function returns sum of elements based on comparator."""
    from basic_excel import sumif
    assert sumif(elements, comparator) == result

@pytest.mark.parametrize('elements, comparator, result', TEST_INPUT)
def test_countif(elements, comparator, result):
    """Test function returns average of elements based on comparator."""
    from basic_excel import averageif
    assert averageif(elements, comparator) == result
