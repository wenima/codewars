"""Tests for codewars kata https://www.codewars.com/kata/56055244356dc5c45c00001e."""

import pytest


#try to use tuples for input var
COUNTIF_INPUT = [
    ([1, 3, 5, 7, 9], 3, 1),
    (["John","Steve","John"], "John", 2),
    ([1, 3, 5, 3],'>=3', 3),
    ([1.5, 3, 5, 3, 0, -1, -5],'<=1.5', 4),
    ([1, 3, 5, 3.5],'>3', 2),
    ([1, 3, 5, 3, 0, -1, -5],'<1', 3),
    ([1, 3, 5, 3, 0, -1, -5],'<>1', 6)
]

SUMIF_INPUT = [
    ([2, 4, 6, -1, 3, 1.5],">0", 16.5),
    ([1, 3, 5, 3], 3, 6),
    ([1, 3, 5, 3],'>=3', 11),
    ([1.5, 3, 5, 3, 0, -1, -5],'<=1.5', -4.5),
    ([1, 3, 5, 3.5],'>3', 8.5),
    ([1, 3, 5, 3, 0, -1, -5],'<1', -6),
    ([1, 3, 5, 3, 0, -1, -5],'<>1', 5),
]

AVERAGEIF_INPUT = [
    ([99, 95.5, 0, 83],"<>0", 92.5),
    ([1, 3, 5, 3], 3, 3),
    ([1, 3, 5, 3],'>=3', 11/3.0),
    ([1.5, 3, 5, 3, 0, -1, -5],'<=1.5', -1.125),
    ([1, 3, 5, 3.5],'>3', 4.25),
    ([1, 3, 5, 3, 0, -1, -5],'<1', -2),
    ([1, 3, 5, 3, 0, -1, -5],'<>1', 5/6.0),
]


@pytest.mark.parametrize('values, criteria, result', COUNTIF_INPUT)
def test_countif(values, criteria, result):
    """Test function returns number of occurences of comparator in elements."""
    from basic_excel import countif
    assert countif(values, criteria) == result

@pytest.mark.parametrize('values, criteria, result', SUMIF_INPUT)
def test_sumif(values, criteria, result):
    """Test function returns sum of elements based on criteria."""
    from basic_excel import sumif
    assert sumif(values, criteria) == result

@pytest.mark.parametrize('values, criteria, result', AVERAGEIF_INPUT)
def test_countif(values, criteria, result):
    """Test function returns average of elements based on comparator."""
    from basic_excel import averageif
    assert averageif(values, criteria) == result
