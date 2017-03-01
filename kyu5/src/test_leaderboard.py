"""Tests for kata leaderboard."""

import pytest


TESTS = [
    (3, 'SteffenVogel_79', 'CSV - SLayer', 39407),
    (25, 'jacobb', 'UVM', 16878),
    (102, 'ubaw', '', 7002),
]


@pytest.mark.parametrize('pos, name, clan, honor', TESTS)
def test_solution(pos, name, clan, honor):
# def test_solution():
    """Test that given report, test returns a pivot indexed by given index."""
    from leaderboard import solution
    leaderboard = solution()
    assert len(leaderboard.position) == 500
    # user = leaderboard.position[3]
    # user.name == 'SteffenVogel_79'
    # user.clan == 'CSV - SLayer'
    # user.honor == 39407
    user = leaderboard.position[pos]
    assert user.name == name
    assert user.clan == clan
    assert user.honor == honor
