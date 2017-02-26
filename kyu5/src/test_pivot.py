"""Tests for kata pivot."""

import pytest


TESTS = [
    ([
      ["Item 1", "Man", "2500", "500", "Yellow"],
      ["Item 2", "Woman", "42", "8.4", "Blue"],
      ["Item 3", "Woman", "56", "11.2", "Purple"],
      ["Item 4", "Woman", "11", "2.2", "Yellow"],
      ["Item 5", "Man", "3600", "720", "Red"],
      ["Item 6", "Woman", "32", "6.4", "Red"],
      ["Item 7", "Man", "6700", "1340", "Yellow"],
      ["Item 8", "Woman", "25", "5", "Green"]
    ], 1,
    [['-', 'Man', 12800.0, 2560.0, '-'],['-', 'Woman', 166.0, 33.2, '-']]),
    ([
        ["Item 1", "Black", "123"],
        ["Item 2", "Red", "34"],
        ["Item 3", "Black", "4747"],
        ["Item 4", "Red", "35"]
    ], 0,
    [['Item 1', '-', 123.0], ['Item 2', '-', 34.0], ['Item 3', '-', 4747.0], ['Item 4', '-', 35.0]]),
    ([
        ["Item 1", "Black", "123"],
        ["Item 2", "Red", "34"],
        ["Item 3", "Black", "4747"],
        ["Item 4", "Red", "35"]
    ], 1,
    [['-', 'Black', 4870.0], ['-', 'Red', 69.0]]),
    ([
        ['Item 1', 'Man', '2500', '500', 'Yellow'],
        ['Item 2', 'Woman', '42', '8.4', 'Blue'],
        ['Item 3', 'Woman', '56', '11.2', 'Purple'],
        ['Item 4', 'Woman', '11', '2.2', 'Yellow'],
        ['Item 5', 'Man', '3600', '720', 'Red'],
        ['Item 6', 'Woman', '32', '6.4', 'Red'],
        ['Item 7', 'Man', '6700', '1340', 'Yellow'],
        ['Item 8', 'Woman', '25', '5', 'Green']
    ], 4,
    [['-', '-', 42.0, 8.4, 'Blue'],
    ['-', '-', 25.0, 5.0, 'Green'],
    ['-', '-', 56.0, 11.2, 'Purple'],
    ['-', '-', 3632.0, 726.4, 'Red'],
    ['-', '-', 9211.0, 1842.2, 'Yellow']]),
]


@pytest.mark.parametrize('report, index, result', TESTS)
def test_pivot(report, index, result):
    """Test that given report, test returns a pivot indexed by given index."""
    from pivot import pivot
    assert pivot(report, index) == result
