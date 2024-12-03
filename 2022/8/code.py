from io import StringIO
from itertools import combinations, product
from pathlib import Path
from pprint import pprint
import numpy as np


def get_input(filename):
    with open(Path(Path(__file__).parent, filename)) as f:
        return f.read()


sample = get_input("sample.txt")
puzzle = get_input("puzzle.txt")


def parse_input(input_str):
    return np.genfromtxt(StringIO(input_str), delimiter=1)


def solve1(input_str):
    f = parse_input(input_str)
    x, y = f.shape
    center = f[1 : x - 1, 1 : y - 1]
    center_indices = np.indices(center.shape) + np.array([1, 1]).reshape((2, 1, 1))
    mask = np.zeros(center.shape, dtype=bool)
    for direction, axis in product([-1, 1], [0, 1]):
        ind = center_indices.copy()
        ind[axis] += direction
        # ind = indices
        shifted = f[*(ind)]
        greater = center > shifted

        rolled = np.rollaxis(greater, -axis)
        mask_i = np.zeros(rolled.shape, dtype=bool)
        print(axis, direction)
        # print(center)
        print(shifted)
        # print(rolled)
        print(greater.astype(int))
        if direction == 1:
            rolled = np.flip(rolled, axis)
        if direction != 1:
            rolled = np.flip(rolled, ~axis)
        print(rolled.astype(int))
        for i in range(rolled.shape[0]):
            mask_i[i] = np.all(rolled[: (i + 1)], axis=0)
        mask_i = np.rollaxis(mask_i, axis)
        print(mask_i)
        mask = np.logical_or(mask, mask_i)

    print(f)
    print(mask.astype(int))
    # print(center)
    outside = f.shape[0] * f.shape[1] - (center.shape[0] * center.shape[1])
    print(mask.sum(), outside, mask.sum() + outside)


sample2 = """11111
12221
12321
12221
11111"""
sample3 = """11111
12221
23132
12221
11111"""
# solve1(sample)
solve1(sample3)
# solve1(puzzle)
