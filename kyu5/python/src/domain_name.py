"""Module to solve the code-kata
https://www.codewars.com/kata/extract-the-domain-name-from-a-url-1/train/python.
This is just a proof of concept/prototype. The correct solution covering all
domain names as well as private domains is alot more complicated. It would
involve getting the current viable top-level domains and parse the url looking
up valid domains under the TLD.

For example http://ag.utah.gov/ won't be found with the approach taken below.
"""

import re


def domain_name(url):
    """Return the domain name of the url."""
    pattern = r'^(?:http(?:s?)://)?(?:www\.)?(.*?)\.(?:[a-z.-])'
    m = re.match(pattern, url)
    return m.group(1) if m else None
