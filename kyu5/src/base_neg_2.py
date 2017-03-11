"""Module to solve the code-kata https://www.codewars.com/kata/base-2/train/python."""


def to_nega_binary(n):
    """Return a string representation of the negabinary value of given n."""
	res = []
	while n != 0:
		remainder = abs(n) % 2
		res.append(str(remainder))
		if n < 0 and remainder:
			n -= 1
		n = int(n / -2)
	return (''.join(reversed(res)))
