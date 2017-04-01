# Summary

the repository *codewars* includes all of my completed code-katas from the
[CodeWars Python challenges](http://wwww.codewars.com) with a difficulty of
kyu5 or higher. [History of the term kyu](https://en.wikipedia.org/wiki/Ky%C5%AB)

# Python coding challenges:

## kyu5

* Base -2
* RPG dice roller
* Extract the domain name from a URL
* not-very-secure
* Excel's COUNTIF, SUMIF and AVERAGEIF functions
* Mod 4 Regex
* Convert string to camel case
* Calculate Fibonacci return count of digit occurrences

##kyu4

* Validate Sudoku with size `NxN`

## Details for each kata completed

### Base -2
* Descripton of Kata: In this Kata you must convert integers numbers from and to
a negative-base binary system.
* Difficulty: kyu5
* Module: base_neg_2.py
* Tests: test_base_neg_2.py
* Link: https://www.codewars.com/kata/base-2/train/python
* Comments about most interesting solution/best practice:
I spent quite a bit reading up on this topic and came across a shortcut to convert
from decimal to negabinary by using the Librik, Szudzik & Schroeppel algorithm
which is mentioned [here] (https://en.wikipedia.org/wiki/Negative_base). A more
detailed explanation happend in this SO thread:
http://stackoverflow.com/questions/37637781/calculating-the-negabinary-representation-of-a-given-number-without-loops
Solution using Librik, Szudzik & Schroeppel algo:
```python
def int_to_negabinary(i):
    return str(bin((i + mask) ^ mask))[2:]

def negabinary_to_int(s):
    return (mask ^ int(s,2)) - mask
```
Most upvoted solution using bit-shifting:
```python
def int_to_negabinary(i):
    ds = []
    while i != 0:
        ds.append(i & 1)
        i = -(i >> 1)
    return ''.join(str(d) for d in reversed(ds)) if ds else '0'

def negabinary_to_int(s):
    i = 0
    for c in s:
        i = -(i << 1) + int(c)
    return i
```

### RPG dice roller
* Descripton of Kata: Your task in this kata is to write a "dice roller" that
interprets a subset of [dice notation] (https://en.wikipedia.org/wiki/Dice_notation)
Your function must support two types of output depending on the second argument;
verbose and summed.
* Difficulty: kyu5
* Module: diceroller.py
* Tests: test_diceroller.py
* Link: https://www.codewars.com/kata/rpg-dice-roller
* Comments about most interesting solution/best practice:
I like the use of unpacking the match.groups() into the 3 variables.
Not sure ```isinstance``` is a preferred solution though as it violates the
principle of asking for forgiveness rather than permission philosophy.
```python
import re
import random

def roll(desc, verbose=False):
    if isinstance(desc, str):
        desc_cleared = re.sub(r'\s', '', desc)
        match = re.match(r'^(\d*)d(\d+)((?:[+-]\d+)*)$', desc_cleared)
        if match:
            (dices, sides, modifiers) = match.groups()
            dices, sides = [int(x) if x else 1 for x in [dices, sides]]
            modifier = eval(modifiers) if modifiers else 0
            rolls = [random.randint(1, sides) for _ in range(dices)]
            return {'dice': rolls, 'modifier': modifier} if verbose else sum(rolls) + modifier
    return False
```

### Extract the domain name from a URL
* Descripton of Kata: Write a function that when given a URL as a string, parses
out just the domain name and returns it as a string. For example:
```
domain_name("http://github.com/carbonfive/raygun") == "github"
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
```
* Difficulty: kyu5
* Module: domain_name.py
* Tests: test_domain_name.py
* Link: https://www.codewars.com/kata/extract-the-domain-name-from-a-url-1/train/python
* Comments about most interesting solution/best practice:
Below solution is not the most up-voted one for this kata but in my view the one
which solves the problem description the best.
```python
import re
def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')
```

### Not very secure
* Descripton of Kata: In this example you have to validate if a user input
string is alphanumeric. The given string is not nil, so you don't have to check
that.

The string has the following conditions to be alphanumeric:
```
- At least one character ("" is not valid)
- Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
- No whitespaces/underscore
```
* Difficulty: kyu5
* Module: not_secure.py
* Tests: test_not_secure.py
* Link: https://www.codewars.com/kata/not-very-secure/train/python
* Comments about most interesting solution/best practice:
```python
import re
def alphanumeric(string):
    return bool(re.match(r'^[A-Za-z0-9]+$', string))
```

### Excel's COUNTIF, SUMIF and AVERAGEIF functions
* Descripton of Kata: Microsoft Excel provides a number of useful functions for
counting, summing, and averaging values if they meet a certain criteria. Your
task is to write three functions that work similarly to Excel's COUNTIF, SUMIF
and AVERAGEIF functions.

Each function will take the same two arguments:

- A list object containing ```values``` to be counted, summed, or averaged.
- A ```criteria``` in either an integer, float, or string
* Integer or float indicates equality
* Strings can indicate >, >=, <, <= or <> (use the Excel-style "Not equal to"
operator) to a number (ex. ">=3"). In the ```count_if``` function, a string without
an operator indicates equality to this string.

The tests will all include properly formatted inputs. The test cases all avoid
rounding issues associated with floats.

* Difficulty: kyu5
* Module: basic_excel.py
* Tests: test_basic_excel.py
* Link: https://www.codewars.com/kata/56055244356dc5c45c00001e
* Comments about most interesting solution/best practice:
Not many solutions which didn't use eval or simply checked for the parameters
given in the test. I feel this should be solved programmatically. I like the
creativity of the below solutions but don't agree with checking for type.
```python
def parse(values, criteria):
    if type(criteria) in [int, float] or (type(criteria) is str and criteria[0] not in "<>"):
        return [item for item in values if item == criteria]

    rel = criteria.translate(None, "0123456789.")
    limit = float(criteria.translate(None, "<>="))

    if   rel == "<>":
        return [item for item in values if item <> limit]
    elif rel == "<=":
        return [item for item in values if item <= limit]
    elif rel == ">=":
        return [item for item in values if item >= limit]
    elif rel == "<":
        return [item for item in values if item < limit]
    elif rel == ">":
        return [item for item in values if item > limit]


def count_if(values, criteria):
    return len(parse(values, criteria))

def sum_if(values, criteria):
    return sum(parse(values, criteria))

def average_if(values, criteria):
    return sum(parse(values, criteria)) * 1.0 / len(parse(values, criteria))
```

### Mod4 Regex
* Descripton of Kata: You are to write a Regular Expression that matches any
string with at least one number divisible by 4 (with no remainder). In most
languages, you could do this easily by using ```number % 4 == 0```. How would
you do it with Regex?
* Difficulty: kyu5
* Module: mod4regex.py
* Tests: test_mod4regex.py
* Link: https://www.codewars.com/kata/mod4-regex
* Comments about most interesting solution/best practice:
Not the highest voted but best solution nonetheless
```python
import re

class Mod:
    mod4 = re.compile(r'.*\[[+-]?\d*((\b|[02468])[048]|[13579][26])\]')
```

### Convert string to camel case
* Descripton of Kata: Complete the method/function so that it converts dash/underscore
delimited words into camel casing. The first word within the output should be
capitalized only if the original word was capitalized.
* Difficulty: kyu5
* Module: camelcase.py
* Tests: test_camelcase.py
* Link: https://www.codewars.com/kata/convert-string-to-camel-case/python
* Comments about most interesting solution/best practice:
```python
```

### Calculate Fibonacci return count of digit occurrences
* Descripton of Kata: Your task is to efficiently calculate the nth element in
the Fibonacci sequence and then count the occurrence of each digit in the number
returning a list of integer pairs sorted in descending order.
* Difficulty: kyu5
* Module: fib_digit_occurence.py
* Tests: test_fib_digit_occurence.py
* Link: https://www.codewars.com/kata/calculate-fibonacci-return-count-of-digit-occurrences
* Comments about most interesting solution/best practice:
```python
from collections import Counter


def fib_digits(n):
    a,b = 0,1
    for i in range(n-1):
        a,b = b, a+b
    counts = Counter(str(b))
    return sorted(((count, int(digit)) for digit, count in counts.items()), reverse=True)
```

### Validate Sudoku with size `NxN`
* Descripton of Kata: Given a Sudoku data structure with size NxN, N > 0 and
√N == integer, write a method to validate if it has been filled out correctly.
* Difficulty: kyu4
* Module: sudoku_validator.py
* Tests: test_sudoku_validator.py
* Link: https://www.codewars.com/kata/validate-sudoku-with-size-nxn
* Comments about most interesting solution/best practice:
```python
```

### Primes with Even Digits
* Descripton of Kata: Find the closest prime number under a certain integer n
that has the maximum possible amount of even digits.
* Difficulty: kyu4
* Module: even_digit_primes.py
* Tests: test_even_digit_primes.py
* Link: https://www.codewars.com/kata/primes-with-even-digits
* Comments about most interesting solution/best practice:
```python
```
