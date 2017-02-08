"""Tests for kata grab csv columns."""

import pytest


TESTS = [
    ["1,2\n3,4\n5,6", [5, 6, 7], ""],
    ["1,2,3\n4,5,6", [0, 1], "1,2\n4,5"],
    ["a,b,c,d,e\n1,2,3,4,5\nf,g,h,i,j", [1, 3, 5, 7], "b,d\n2,4\ng,i"],
    ["1\n2\n3\n4\n5", [0, 1], "1\n2\n3\n4\n5"],
    ["1\n2\n3\n4\n5", [1], ""],
]


@pytest.mark.parametrize('csv, indeces, result', TESTS)
def test_csv_columns(csv, indeces, result):
    """Test that given csv, list of indeces return expected result."""
    from csv_columns import csv_columns
    assert csv_columns(csv, indeces) == result
