import re

from helpers import read_input

sample = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"


pattern = re.compile(r"mul\((\d+),(\d+)\)")
puzzle = read_input(2024, 3)


def mul(a, b):
    return a * b


def solve1(puzzle):
    result = 0
    for a, b in pattern.findall(puzzle):
        result += mul(int(a), int(b))
    return result


def solve2(puzzle):
    dos = [0] + [m.start() for m in re.finditer("do()", puzzle)]
    donts = [m.start() for m in re.finditer("don't()", puzzle)]
    result = 0

    for m in pattern.finditer(puzzle):
        im = m.start()
        last_do = max(map(lambda x: x if x < im else -1, dos))
        last_dont = max(map(lambda x: x if x < im else -1, donts))
        if last_do > last_dont:
            result += mul(*map(int, m.groups()))
    return result


print(solve1(sample))
print(solve1(puzzle))

sample2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
print(solve2(sample2))
print(solve2(puzzle))
