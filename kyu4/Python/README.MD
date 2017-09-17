# Python coding challenges:

## kyu4

* Validate Sudoku with size `NxN`
* Valid Braces
* Next Bigger Number
* One Line Task: Palindrome String
* Strip Url Params
* Ranking Poker Hands

## Details for each kata completed

### Validate Sudoku with size `NxN`
* Description of Kata: Given a Sudoku data structure with size NxN, N > 0 and
√N == integer, write a method to validate if it has been filled out correctly.
* Difficulty: kyu4
* Module: sudoku_validator.py
* Tests: test_sudoku_validator.py
* [Link](https://www.codewars.com/kata/validate-sudoku-with-size-nxn)

### Valid Braces
* Description of Kata: Write a function called validBraces that takes a string of
braces, and determines if the order of the braces is valid. validBraces should
return true if the string is valid, and false if it's invalid.
* Difficulty: kyu4
* Module: valid_braces.py
* Tests: test_valid_braces.py
* [Link](https://www.codewars.com/kata/valid-braces)

### Next Bigger Number
* Description of Kata: You have to create a function that takes a positive integer
number and returns the next bigger number formed by the same digits:
* Difficulty: kyu4
* Module: next_bigger.py
* Tests: test_next_bigger.py
* [Link](https://www.codewars.com/kata/next-bigger-number-with-the-same-digits)
* Comments about most interesting solution/best practice:
Some of the solutions are short but are basically brute-forcing it. The below
solution is 2nd highest voted but I like it better than the top voted one due to
readability and speed.
```python
import itertools
def next_bigger(n):
    s = list(str(n))
    for i in range(len(s)-2,-1,-1):
        if s[i] < s[i+1]:
            t = s[i:]
            m = min(filter(lambda x: x>t[0], t))
            t.remove(m)
            t.sort()
            s[i:] = [m] + t
            return int("".join(s))
    return -1
```

### One Line Task: Palindrome String
* Description of Kata: Your task is to generate a palindrome string, using the
specified length n, the specified characters c(all characters in c must be used
at least once), and the code length should less than 55 characters
* Difficulty: kyu4
* Module: palindrome_one_liner.py
* Tests: test_palindrome_one_liner.py
* [Link](https://www.codewars.com/kata/one-line-task-palindrome-string)
* Comments about most interesting solution/best practice: Didn't know about method
center, nice use here.
```python
palindrome=lambda n,s:(s+s[-1-n%2::-1]).center(n,s[0])
```

### Strip Url Params
* Description of Kata: Write a method that
Removes any duplicate query string parameters from the url
Removes any query string parameters specified within the 2nd argument (optional array)
* Difficulty: kyu4
* Module: url_strip_params.py
* Tests: test_palindrome_one_liner.py
* [Link](https://www.codewars.com/kata/strip-url-params)

### Ranking Poker Hands
* Descripton of Kata: Create a poker hand that has a method to compare itself to another poker hand:
    compare_with(self, other_hand)
A poker hand has a constructor that accepts a string containing 5 cards:
    PokerHand(hand)
* Difficulty: kyu4
* Module: poker_rankings.py
* Tests: test_poker_rankings.py
* [Link](https://www.codewars.com/kata/ranking-poker-hands/python)

### Sortable Poker Hands
* Descripton of Kata: Write an algorithm which sorts Texas Hold'em poker hands.
* Difficulty: kyu4
* Module: sortable_poker_hands.py
* Tests: test_sortable_poker_hands.py
* [Link](https://www.codewars.com/kata/sortable-poker-hands/python)
