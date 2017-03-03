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
def gap(g, m, n):
    prev = 2
    for x in range(m|1, n + 1, 2):
        if all(x%d for d in range(3, int(x**.5) + 1, 2)):
            if x - prev == g: return [prev, x]
            prev = x
```

* Name: Biggest Sum
* Descripton of Kata: You have to find maximum sum of numbers from top left
corner of a matrix to bottom right corner. You can only go down or right.

Matrix will be square M x M, 4 ≤ M ≤ 60
Matrix will have only positive integers N.
10 ≤ N ≤ 200
```
matrix = [[20, 20, 10, 10],
          [10, 20, 10, 10],
          [10, 20, 20, 20],
          [10, 10, 10, 20]]
```

* Difficulty: kyu5
* Module: find_sum.py
* Tests: test_find_sum.py
* Link: https://www.codewars.com/kata/biggest-sum/python
* Comments about most interesting solution/best practice:
Very nice solution to solve the issue. My approach of solving this via a graph
also provides the path taken.
```python
def find_sum(m):
    p = [0] * (len(m) + 1)
    for l in m:
        for i, v in enumerate(l, 1):
            p[i] = v + max(p[i-1], p[i])
    return p[-1]
```

* Name: Rudimentary Pivot Table
* Descripton of Kata: Create a Rudimentary Pivot Table function that takes in a
two dimensional array and returns an aggregated two dimensional array based on
the values of a certain column.

Example Input:
```
# A report showing shopping items and their related metrics
report = [
      ["Item 1", "Man", "2500", "500", "Yellow"],
      ["Item 2", "Woman", "42", "8.4", "Blue"],
      ["Item 3", "Woman", "56", "11.2", "Purple"],
      ["Item 4", "Woman", "11", "2.2", "Yellow"],
      ["Item 5", "Man", "3600", "720", "Red"],
      ["Item 6", "Woman", "32", "6.4", "Red"],
      ["Item 7", "Man", "6700", "1340", "Yellow"],
      ["Item 8", "Woman", "25", "5", "Green"]
]
```
* Difficulty: kyu5
* Module: pivot.py
* Tests: test_pivot.py
* Link: https://www.codewars.com/kata/rudimentary-pivot-table
* Comments about most interesting solution/best practice:
I like the use of itertools' groupby and using itemgetter for sorting. I don't
like the bare except and variable naming.
```python
from operator import itemgetter
from itertools import groupby

def agg(l):
    try: return sum(map(float,l))
    except: return '-'

def pivot(a,ip):
    return [[k if i==ip else agg(c) for i,c in enumerate(zip(*g))] for k,g in groupby(sorted(a,key=itemgetter(ip)),key=itemgetter(ip))]
```


* Name: Scraping: Codewars Top 500 Users
* Descripton of Kata: You should get and parse the html of the codewars
leaderboard page.

Return a 'Leaderboard' object with a position property.
```
Leaderboard#position should contain 500 'User' objects.
Leaderboard#position[i] should return the ith ranked User(1 based index).
```

Each User should have the following properties:
```
User#name    # => the user's username, not their real name
User#clan    # => the user's clan, empty string if empty clan field
User#honor   # => the user's honor points as an integer
```
Ex:
```
an_alien = leaderboard.position[3]   # => #<User:0x3124da0 @name="myjinxin2015", @clan="China Changyuan", @honor=21446>
 an_alien.name                        # => "myjinxin2015"
 an_alien.clan                        # => "China Changyuan"
 an_alien.honor                       # => 21446
 ```

* Difficulty: kyu5
* Module: scrape.py
* Tests: test_scrape.py
* Link: https://www.codewars.com/kata/scraping-codewars-top-500-users
* Comments about most interesting solution/best practice:
```python
import sys
from bs4 import BeautifulSoup
if sys.version_info[0] > 2:
    import urllib.request
else:
    import urllib2


class Leaderboard:

    def __init__(self, position):
        self.position = position


class User:

    def __init__(self, username, clan, honor):
        self.name = username
        self.clan = clan
        self.honor = honor


def get_html(url):
    if sys.version_info[0] > 2:
        with urllib.request.urlopen(url) as response:
            return response.read()
    return urllib2.urlopen(url).read()



def get_table(html):
    return BeautifulSoup(html).find('table')


def solution():
    table = get_table(get_html('https://www.codewars.com/users/leaderboard'))
    positions = {}
    i = 1
    for row in table.find_all("tr")[1:]:
        clan, honor = row.find_all('td')[-2:]
        user_name = row.attrs['data-username']
        positions[i] = User(str(user_name), clan.text, int(honor.text))
        i += 1
    return Leaderboard(positions)
```
