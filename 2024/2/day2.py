from io import StringIO
from helpers import read_input
from numpy import array, diff, genfromtxt, logical_or
import numpy as np

sample = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


def solve1(text):
    result = 0
    for line in text.splitlines():
        a = genfromtxt(StringIO(line), dtype=int)
        result += is_safe(a)
    return result


def is_safe(values):
    a = array(values)
    d = diff(a)
    print(d)
    print(descending := np.all((-3 <= d) & (d < 0)))
    print(ascending := np.all((0 < d) & (d <= 3)))
    res = logical_or(ascending, descending)
    return res


def solve2(text):
    result = 0
    for line in text.splitlines():
        a = genfromtxt(StringIO(line), dtype=int)
        if is_safe(a):
            result += 1
            continue
        for i in range(len(a)):
            line_i = list(a)
            del line_i[i]
            if is_safe(line_i):
                result += 1
                break
    return result


puzzle = read_input("2024/input_2.txt")
print(solve1(sample))
print(solve1(puzzle))
print(solve2(puzzle))
