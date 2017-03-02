"""Tests for kata leaderboard."""

import pytest


TESTS = [
    (3, 'SteffenVogel_79', 'CSV - SLayer', 39488),
    (25, 'jacobb', 'UVM', 16890),
    (102, 'ubaw', '', 7003),
]


@pytest.mark.parametrize('pos, name, clan, honor', TESTS)
def test_solution(pos, name, clan, honor):
    """Test that given report, test returns a pivot indexed by given index."""
    from leaderboard import solution
    leaderboard = solution()
    assert len(leaderboard.position) == 500
    user = leaderboard.position[pos]
    assert user.name == name
    assert user.clan == clan
    assert user.honor == honor
