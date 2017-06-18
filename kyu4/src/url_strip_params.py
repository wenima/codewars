"""Module to solve the code-kata https://www.codewars.com/kata/51646de80fd67f442c000013."""

from urlparse import urlparse, parse_qs
from urllib import urlencode

def strip_url_params(url, strip=None):
    if not strip: strip = []

    parse = urlparse(url)
    query = parse_qs(parse.query)

    query = {k: v[0] for k, v in query.iteritems() if k not in strip}
    query = urllib.urlencode(query)
    new = parse._replace(query=query)

    return new.geturl()
