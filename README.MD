#Summary

the repository *codewars* includes all of my completed code-katas from the
[CodeWars Python challenges] (http://wwww.codewars.com) with a difficulty of
kyu5 or higher. [History of the term kyu(https://en.wikipedia.org/wiki/Ky%C5%AB)]

# Python coding challenges:

## kyu5

* Base -2
* RPG dice roller
* Extract the domain name from a URL

## Details for each kata completed

* Name: Base -2
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
Highest using solution using bit-shifting:
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

* Name: RPG dice roller
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

* Name: Extract the domain name from a URL
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

* Name: Not very secure
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
```
