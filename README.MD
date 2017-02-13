#Summary

the repository *codewars* includes all of my completed code-katas from the
[CodeWars Python challenges] (http://wwww.codewars.com) with a difficulty of
kyu5 or higher. [History of the term kyu(https://en.wikipedia.org/wiki/Ky%C5%AB)]

# Python coding challenges:

## kyu5

* What's a perfect power anyway?
* Grab CSV Columns
*


## Details for each kata completed

* Name: Perfect Power
* Descripton of Kata: Your task is to check wheter a given integer is a perfect
power. If it is a perfect power, return a pair ```m``` and ```k``` with m^k = n
as a proof. Otherwise return None.
* Difficulty: kyu5
* Module: perfect_power.py
* Tests: test_perfect_power.py
* Link: https://www.codewars.com/kata/whats-a-perfect-power-anyway/python
* Comments about most interesting solution/best practice:
```python

```

* Name: Grab CSV Columns
* Descripton of Kata: Write a function called csvColumns that takes a CSV
(format shown below) and an array of indices, which represents the columns of
the CSV, and return a CSV with only the columns specified in the indices array.
* Difficulty: kyu5
* Module: csv_columns.py
* Tests: test_csv_columns.py
* Link: https://www.codewars.com/kata/grab-csv-columns/python
* Comments about most interesting solution/best practice:
the use of lambda here is quite elegant. I like the idea of joining the lines
together with newline character rather than building a string like in my solution.
```python
def csv_columns(csv, indices):
    sorted_indices = sorted(set(indices))
    extract = lambda line: [line[idx] for idx in sorted_indices if idx < len(line)]
    csv_parsed = [line.split(',') for line in csv.split('\n')]
    return '\n'.join(','.join(line) for line in map(extract, csv_parsed) if line)
```

* Name: Last digit of a large number
* Descripton of Kata: Define a function that takes in two numbers a and b and
returns the last decimal digit of ```a^b```. Note that a and b may be very large!
The inputs to your function will always be non-negative integers.
* Difficulty: kyu5
* Module: last_digit.py
* Tests: test_last_digit.py
* Link: https://www.codewars.com/kata/last-digit-of-a-large-number/python
* Comments about most interesting solution/best practice:
there is the option to use all the batteries included and simply call ```pow()```
with a third argument but it was raised as an issue in the kata and was proposed
to be banned. From the other solutions, I liked this one but don't know how it
measures against my solution.
```python
def last_digit(n1, n2):
    return (n1 % 10) ** min(n2 % 4 or 4, n2) % 10
```

* Name: Primes in numbers
* Descripton of Kata: Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :
 ```
 (p1**n1)(p2**n2)...(pk**nk)
 ```
with the p(i) in increasing order and n(i) empty if n(i) is 1.
* Difficulty: kyu5
* Module: primes_in_numbers.py
* Tests: test_primes_in_numbers.py
* Link: https://www.codewars.com/kata/primes-in-numbers
* Comments about most interesting solution/best practice:
```python

```

* Name: Gap in Primes
* Descripton of Kata: A prime gap of length n is a run of n-1 consecutive
composite numbers between two successive primes
(see: http://mathworld.wolfram.com/PrimeGaps.html).

We will write a function gap with parameters:

g(integer >= 2) which indicates the gap we are looking for

m (integer > 2) which gives the start of the search (m inclusive)

n (integer >= m) which gives the end of the search (n inclusive)

In the example above
```
gap(2, 3, 50)
```
 will return [3, 5] or (3, 5) or {3, 5} which is the first pair between 3 and 50 with a 2-gap.
* Difficulty: kyu5
* Module: gap_primes.py
* Tests: test_gap_primes.py
* Link: https://www.codewars.com/kata/gap-in-primes
* Comments about most interesting solution/best practice:
```python

```
