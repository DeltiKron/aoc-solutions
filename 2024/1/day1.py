from collections import Counter

from helpers import read_input


puzzle = read_input(2024, 1)

sample = """3   4
4   3
2   5
1   3
3   9
3   3"""


def parse_input(text):
    a, b = [], []
    for line in text.split("\n"):
        if len(line.strip()) < 1:
            continue
        ai, bi = map(lambda x: int(x.strip()), line.split())
        a.append(ai)
        b.append(bi)
    return a, b


def solve1(text):
    print("solving 1")
    a, b = parse_input(text)
    a = sorted(a)
    b = sorted(b)

    res = []
    for ai, bi in zip(a, b):
        res.append(abs(ai - bi))
    return sum(res)


def solve2(text):
    a, b = parse_input(text)
    c = Counter(b)
    # print(c)
    return sum(map(lambda x: c.get(x, 0) * x, a))


print(solve1(sample))
print(solve1(puzzle))
print(solve2(sample))
print(solve2(puzzle))
