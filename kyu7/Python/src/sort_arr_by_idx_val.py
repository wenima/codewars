"""Solution for https://www.codewars.com/kata/sort-an-array-by-value-and-index/"""

from operator import itemgetter

def sort_by_value_and_index(arr):
    return [n[0] for n in sorted([(n, (idx + 1) * n) for idx, n in enumerate(arr)], key=itemgetter(1))]

# better way:
def sort_by_value_and_index(arr):
    return [y[1] for y in sorted(enumerate(arr), key=lambda x:(x[0] + 1) * x[1])]

# nice use of itertools
import itertools
def sort_by_value_and_index(nums):
    seq = itertools.count(1)
    return sorted(nums, key=lambda num:num*next(seq))
