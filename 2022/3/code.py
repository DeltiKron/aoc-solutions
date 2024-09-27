import itertools
from pathlib import Path


def get_input(filename):
    with open(Path(Path(__file__).parent, filename)) as f:
        return f.read().strip().splitlines()


def solve1(inputfile):
    lines = get_input(inputfile)
    score = 0
    for line in lines:
        items = line.strip()
        sep = len(line)
        c1, c2 = items[: sep // 2], items[sep // 2 :]
        misplaced = set(c1).intersection(set(c2))
        # print(misplaced)
        for m in misplaced:
            score += 1 + "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index(m)
    return score


def solve2(inputfile):
    lines = get_input(inputfile)
    score = 0
    groups = itertools.batched(lines, n=3)
    for g in groups:
        sets = (set(gi) for gi in g)
        badge = set.intersection(*sets)
        # print(badge)
        for b in badge:
            score += 1 + "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index(b)
    return score


if __name__ == "__main__":
    print(solve1("sample.txt"))
    print(solve1("puzzle.txt"))
    print(solve2("sample.txt"))
    print(solve2("puzzle.txt"))
