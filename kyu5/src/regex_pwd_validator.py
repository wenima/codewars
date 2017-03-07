"""Module to solve the code-kata https://www.codewars.com/kata/regex-password-validation/python"""

import re


def validate_pwd(password):
    """Validates a given password to check for the following rules:
    * At least six characters long
    * contains a lowercase letter
    * contains an uppercase letter
    * contains a number
    True is returned if the given password satisfies this criteria
    """

    pattern = r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)^[A-Za-z0-9]{6,}$'

    m = re.search(pattern, password)

    return True if m else False
