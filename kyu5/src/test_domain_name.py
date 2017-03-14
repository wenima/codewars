"""Tests for codewars kata https://www.codewars.com/kata/extract-the-domain-name-from-a-url-1/train/python."""

import pytest


TEST_INPUT = [
    ('http://github.com/carbonfive/raygun', 'github'),
    ('http://www.zombie-bites.com', 'zombie-bites'),
    ('https://www.cnet.com', 'cnet'),
]


@pytest.mark.parametrize('url, result', TEST_INPUT)
def test_domain_name(url, result):
    """Test domain name is returned correctly from given url."""
    from domain_name import domain_name
    assert domain_name(url) == result
