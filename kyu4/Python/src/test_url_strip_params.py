"""Tests for codewars kata https://www.codewars.com/kata/51646de80fd67f442c000013."""

import pytest

url1 = 'www.codewars.com?a=1&b=2'
url2 = 'www.codewars.com?a=1&b=2&a=1&b=3'
url3 = 'www.codewars.com?a=1'
url4 = 'www.codewars.com'

TEST = [
    (url1, [], url1),
    (url2, [], url1),
    (url2, ['b'], url3),
    (url4, ['b'], url4),
]


@pytest.mark.parametrize('u, p, result', TEST)
def test_strip_url(u, p, result):
    """Test that function returns correct url."""
    from url_strip_params import strip_url_params
    assert strip_url_params(u, p) == result
