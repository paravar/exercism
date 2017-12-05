""""
def slices(series, length):
    if length > len(series) or length == 0:
        raise ValueError
    return [list(map(int, series[i:i+length])) for i in range(0, len(series) -
            length + 1)]


def mult(ls):
    result = 1
    for i in range(len(ls)):
        result *= ls[i]
    return(result)


def largest_product(series, size):
    if size > len(series) or size < 0:
        raise ValueError
    if size == 1 or size == 0 or len(series) == 0:
        return(1)
    slcs = slices(series, size)
    largest = max(list(map(mult, slcs)))
    return(largest)
"""

from functools import reduce
from operator import mul


def largest_product(series, size):
    if size > len(series) or size < 0:
        raise ValueError("Size must be positive and smaller than length of series")
    chunks = (series[i:i+size] for i in range(len(series) - size + 1))
    return max(map(lambda x: reduce(mul, (int(n) for n in x), 1), chunks))
