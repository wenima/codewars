"""Module to solve the code-kata https://www.codewars.com/kata/56055244356dc5c45c00001e.
Per the description of the kata, we assume that if a string is given and it starts
with anything but an alphanumeric character, it is an operator.

Since the use of eval is not recommended for unknown input and apparently it's
really hard to safeguard against malicious code using eval, we implement a
dispatch/commann pattern.
"""

import re
#commented out using fast_real from fastnumbers due to lib not available on codewars
# from fastnumbers import fast_real
import operator as op


def is_smaller(a, b):
  return True if a < b else None

def is_greater(a, b):
  return True if a > b else None

def is_equal_or_smaller(a, b):
    return True if a <= b else None

def is_equal_or_greater(a, b):
    return True if a >= b else None

def is_not_equal(a, b):
    return True if a != b else None

def compare(command, a, b):
    return(dispatch[command](a, b))

dispatch = {
  '<': is_smaller,
  '>': is_greater,
  '<=': is_equal_or_smaller,
  '>=': is_equal_or_greater,
  '<>': is_not_equal,
}


def parse_input(criteria):
    """Return operator, comparator if operator exists in input."""
    try:
        if criteria[:1].isalnum():
            return '', criteria
        else:
            #since we can't use fastnumbers, we need to capture anyting after the decimal point
            m = re.match(r'([^\d\w]*)?(\d*\.?(\d*))$', criteria)
            operator, comparator, decimal = m.groups()
            comparator = float(comparator) if decimal else int(comparator)
            return operator, comparator
    except:
        return '', criteria
        

def out_arr(values, criteria, operator, comparator):
    if len(operator) > 0:
        return [value for value in values if compare(operator, value, comparator)]
    else:
        return [value for value in values if value == criteria]


def count_if(values, criteria):
    """Return number of occurences of criteria in list of values."""
    operator, comparator = parse_input(criteria)
    return len(out_arr(values, criteria, operator, comparator))


def sum_if(values, criteria):
    """Return sum of values based on criteria."""
    operator, comparator = parse_input(criteria)
    return sum(out_arr(values, criteria, operator, comparator))


def average_if(values,criteria):
    """Return average of values based on criteria."""
    operator, comparator = parse_input(criteria)
    out = out_arr(values, criteria, operator, comparator)
    return op.truediv(sum(out), len(out))
