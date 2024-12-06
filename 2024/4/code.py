from itertools import chain
import re
from helpers import read_input
from helpers import Grid

sample = Grid.from_text(
    """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""",
    cast_func=str,
)

puzzle = Grid.from_text(read_input(2024, 4), cast_func=str)


def find_xmas(string):
    re1 = re.compile("XMAS", re.IGNORECASE)
    re2 = re.compile("SAMX", re.IGNORECASE)
    res = re1.findall(string) + re2.findall(string)
    if res:
        print(res)
        print(len(res))
    return len(res)


def find_mas(string, indexes):
    re1 = re.compile("MAS", re.IGNORECASE)
    re2 = re.compile("SAM", re.IGNORECASE)
    res = chain(re1.finditer(string), re2.finditer(string))
    return [indexes[m.start() + 1] for m in res]


def solve1(puzzle: Grid):
    print(list(puzzle.rows))
    print(list(["".join(i) for i in puzzle.cols]))
    print(list(["".join(i) for i in puzzle.diagonals_lb]))
    print(list(["".join(i) for i in puzzle.diagonals_lt]))

    checks = ["".join(i) for i in chain(puzzle.diagonals_lb, puzzle.diagonals_lt, puzzle.rows, puzzle.cols)]
    return sum(find_xmas(i) for i in checks)


def solve2(puzzle: Grid):
    mas_lb = chain(*[find_mas("".join([puzzle.at(*j) for j in i]), i) for i in puzzle.diagonal_indexes_lt])
    mas_lt = chain(*[find_mas("".join([puzzle.at(*j) for j in i]), i) for i in puzzle.diagonal_indexes_lb])
    matches = set(mas_lb).intersection(set(mas_lt))
    return len(matches)


print(solve1(sample))
print(solve1(puzzle))
print(solve2(sample))
print(solve2(puzzle))
