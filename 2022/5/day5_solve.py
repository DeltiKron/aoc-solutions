import re

sample = """    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""


def parse_setup(lines):
    stacks = {int(line): [] for line in map(str.strip, lines.pop(-1).split())}
    for line in lines:
        print(line)
        for k in stacks.keys():
            v = str.strip(line[1 + (k - 1) * 4])
            if v != "":
                stacks[k].append(v)
    return stacks


def print_setup(setup):
    print()
    for k in sorted(setup.keys()):
        print(k, "".join([f"[{v}]" for v in setup[k][::-1]]))


pattern = re.compile("move\s+(\d+)\s+from\s+(\d+)\s+to\s+(\d+)")


def parse_move(move_line):
    return pattern.search(move_line).groups()


def parse_input(puzzle_str):
    lines = list(puzzle_str.split("\n"))
    # print(lines)
    split = lines.index("")
    setup = parse_setup(lines[:split])
    moves = lines[split + 1 :]
    return setup, moves


def make_move(setup, move_string):
    n, source, target = map(int, parse_move(move_string))
    for _ in range(n):
        setup[target] = [setup[source].pop(0)] + setup[target]


def make_move_2(setup, move_string):
    n, source, target = map(int, parse_move(move_string))
    setup[target] = setup[source][:n] + setup[target]
    setup[source] = setup[source][n:]


def solve(puzzle_string):
    setup, moves = parse_input(puzzle_string)
    for m in moves:
        make_move(setup, m)
    return "".join(setup[k][0] for k in sorted(setup.keys()))


def solve2(puzzle_string):
    setup, moves = parse_input(puzzle_string)
    for m in moves:
        make_move_2(setup, m)
    return "".join(setup[k][0] for k in sorted(setup.keys()))


puzzle = """        [F] [Q]         [Q]
[B]     [Q] [V] [D]     [S]
[S] [P] [T] [R] [M]     [D]
[J] [V] [W] [M] [F]     [J]     [J]
[Z] [G] [S] [W] [N] [D] [R]     [T]
[V] [M] [B] [G] [S] [C] [T] [V] [S]
[D] [S] [L] [J] [L] [G] [G] [F] [R]
[G] [Z] [C] [H] [C] [R] [H] [P] [D]
 1   2   3   4   5   6   7   8   9

move 3 from 5 to 2
move 3 from 8 to 4
move 7 from 7 to 3
move 14 from 3 to 9
move 8 from 4 to 1
move 1 from 7 to 5
move 2 from 6 to 4
move 4 from 5 to 7
move 1 from 3 to 6
move 3 from 4 to 3
move 1 from 4 to 1
move 5 from 1 to 9
move 1 from 4 to 6
move 4 from 7 to 4
move 15 from 9 to 2
move 7 from 1 to 6
move 3 from 3 to 5
move 1 from 4 to 9
move 2 from 5 to 3
move 2 from 4 to 9
move 4 from 1 to 6
move 1 from 3 to 1
move 1 from 3 to 2
move 4 from 6 to 3
move 24 from 2 to 8
move 4 from 9 to 8
move 1 from 1 to 3
move 2 from 5 to 4
move 1 from 2 to 4
move 19 from 8 to 1
move 5 from 3 to 9
move 8 from 1 to 3
move 3 from 4 to 1
move 6 from 9 to 5
move 2 from 3 to 4
move 1 from 8 to 5
move 2 from 4 to 6
move 11 from 6 to 1
move 8 from 8 to 7
move 1 from 6 to 5
move 13 from 1 to 3
move 1 from 1 to 7
move 2 from 7 to 8
move 5 from 7 to 1
move 2 from 8 to 4
move 3 from 5 to 3
move 11 from 3 to 1
move 2 from 5 to 3
move 2 from 5 to 3
move 2 from 7 to 1
move 7 from 3 to 1
move 1 from 4 to 5
move 1 from 6 to 4
move 3 from 4 to 7
move 3 from 7 to 1
move 6 from 3 to 5
move 1 from 5 to 9
move 4 from 5 to 4
move 2 from 3 to 4
move 8 from 9 to 2
move 5 from 4 to 6
move 1 from 6 to 5
move 1 from 4 to 9
move 39 from 1 to 7
move 7 from 2 to 6
move 1 from 9 to 3
move 1 from 2 to 7
move 1 from 3 to 1
move 5 from 7 to 3
move 4 from 5 to 1
move 19 from 7 to 9
move 1 from 9 to 8
move 1 from 9 to 7
move 5 from 9 to 3
move 6 from 6 to 7
move 1 from 8 to 3
move 4 from 1 to 4
move 23 from 7 to 6
move 1 from 1 to 6
move 21 from 6 to 2
move 3 from 4 to 8
move 7 from 6 to 1
move 1 from 4 to 9
move 1 from 6 to 7
move 6 from 1 to 2
move 1 from 7 to 4
move 15 from 2 to 8
move 5 from 3 to 8
move 22 from 8 to 7
move 1 from 8 to 1
move 5 from 3 to 4
move 1 from 3 to 2
move 1 from 1 to 2
move 3 from 4 to 8
move 3 from 8 to 9
move 11 from 2 to 1
move 2 from 1 to 4
move 15 from 9 to 5
move 22 from 7 to 3
move 2 from 4 to 9
move 3 from 4 to 2
move 8 from 1 to 8
move 6 from 8 to 6
move 1 from 6 to 2
move 3 from 6 to 9
move 3 from 2 to 7
move 4 from 2 to 9
move 2 from 7 to 5
move 1 from 1 to 7
move 2 from 8 to 2
move 2 from 7 to 5
move 9 from 5 to 3
move 8 from 5 to 2
move 1 from 6 to 4
move 1 from 6 to 9
move 1 from 2 to 9
move 2 from 5 to 1
move 7 from 2 to 3
move 1 from 4 to 3
move 1 from 2 to 4
move 5 from 3 to 4
move 6 from 9 to 3
move 1 from 2 to 6
move 6 from 9 to 6
move 2 from 1 to 8
move 3 from 6 to 3
move 2 from 8 to 6
move 6 from 4 to 1
move 14 from 3 to 9
move 1 from 6 to 4
move 3 from 3 to 9
move 1 from 4 to 5
move 10 from 9 to 6
move 6 from 6 to 7
move 2 from 1 to 8
move 1 from 8 to 6
move 16 from 3 to 2
move 1 from 8 to 1
move 1 from 7 to 1
move 7 from 3 to 4
move 1 from 6 to 5
move 4 from 2 to 3
move 5 from 4 to 9
move 2 from 4 to 5
move 4 from 7 to 4
move 5 from 9 to 6
move 2 from 5 to 4
move 11 from 6 to 7
move 1 from 6 to 8
move 5 from 1 to 5
move 2 from 6 to 4
move 7 from 7 to 3
move 1 from 8 to 6
move 2 from 7 to 3
move 1 from 1 to 3
move 3 from 2 to 8
move 9 from 2 to 5
move 1 from 6 to 1
move 1 from 4 to 8
move 7 from 4 to 7
move 8 from 5 to 6
move 1 from 7 to 2
move 1 from 7 to 4
move 3 from 7 to 8
move 1 from 2 to 3
move 1 from 1 to 2
move 1 from 1 to 7
move 3 from 7 to 6
move 11 from 6 to 2
move 4 from 8 to 7
move 2 from 8 to 7
move 15 from 3 to 2
move 7 from 9 to 4
move 3 from 3 to 2
move 4 from 4 to 7
move 5 from 7 to 3
move 3 from 4 to 6
move 3 from 6 to 9
move 1 from 4 to 2
move 1 from 8 to 1
move 2 from 3 to 7
move 2 from 3 to 7
move 23 from 2 to 5
move 1 from 9 to 1
move 1 from 7 to 9
move 1 from 1 to 8
move 8 from 7 to 1
move 1 from 8 to 4
move 1 from 4 to 2
move 3 from 9 to 8
move 1 from 7 to 9
move 22 from 5 to 9
move 1 from 8 to 5
move 1 from 7 to 4
move 1 from 4 to 5
move 1 from 8 to 3
move 2 from 9 to 3
move 5 from 5 to 2
move 5 from 5 to 4
move 3 from 2 to 7
move 1 from 7 to 3
move 6 from 1 to 7
move 4 from 3 to 1
move 6 from 2 to 8
move 1 from 5 to 6
move 2 from 8 to 1
move 12 from 9 to 4
move 8 from 9 to 4
move 1 from 2 to 9
move 2 from 9 to 8
move 3 from 2 to 8
move 5 from 8 to 6
move 7 from 7 to 1
move 4 from 8 to 9
move 1 from 6 to 1
move 17 from 4 to 7
move 1 from 2 to 4
move 2 from 4 to 1
move 6 from 4 to 6
move 1 from 1 to 4
move 7 from 1 to 5
move 9 from 7 to 9
move 8 from 9 to 8
move 5 from 8 to 3
move 1 from 5 to 6
move 2 from 3 to 6
move 1 from 9 to 1
move 1 from 6 to 1
move 10 from 6 to 1
move 1 from 5 to 1
move 2 from 9 to 1
move 1 from 9 to 7
move 2 from 6 to 8
move 2 from 8 to 2
move 1 from 6 to 8
move 22 from 1 to 9
move 9 from 7 to 5
move 1 from 8 to 1
move 2 from 8 to 3
move 4 from 5 to 9
move 1 from 8 to 3
move 5 from 1 to 9
move 2 from 7 to 3
move 2 from 4 to 7
move 1 from 8 to 5
move 2 from 2 to 4
move 1 from 5 to 8
move 9 from 5 to 8
move 2 from 7 to 5
move 2 from 4 to 5
move 3 from 8 to 4
move 3 from 4 to 3
move 2 from 8 to 6
move 1 from 6 to 4
move 3 from 5 to 9
move 1 from 6 to 3
move 12 from 3 to 5
move 1 from 3 to 1
move 7 from 5 to 4
move 1 from 1 to 3
move 1 from 8 to 1
move 7 from 5 to 1
move 6 from 9 to 6
move 29 from 9 to 5
move 2 from 4 to 6
move 26 from 5 to 2
move 24 from 2 to 7
move 1 from 3 to 2
move 8 from 1 to 7
move 7 from 6 to 9
move 2 from 5 to 3
move 1 from 6 to 4
move 3 from 8 to 5
move 2 from 3 to 8
move 2 from 2 to 8
move 5 from 9 to 2
move 27 from 7 to 2
move 2 from 8 to 3
move 2 from 9 to 5
move 3 from 8 to 5
move 2 from 7 to 4
move 3 from 4 to 7
move 2 from 3 to 2
move 4 from 5 to 1
move 5 from 7 to 2
move 29 from 2 to 8
move 9 from 8 to 3
move 2 from 4 to 8
move 7 from 3 to 2
move 3 from 5 to 4
move 1 from 7 to 5
move 3 from 5 to 6
move 2 from 1 to 8
move 2 from 6 to 8
move 3 from 4 to 2
move 4 from 4 to 2
move 1 from 6 to 8
move 8 from 2 to 4
move 2 from 3 to 5
move 1 from 4 to 1
move 3 from 1 to 2
move 4 from 8 to 2
move 3 from 4 to 9
move 3 from 4 to 1
move 2 from 9 to 5
move 1 from 4 to 6
move 4 from 5 to 1
move 1 from 6 to 8
move 1 from 9 to 3
move 4 from 2 to 3
move 15 from 8 to 2
move 9 from 8 to 1
move 1 from 3 to 9
move 5 from 1 to 9
move 3 from 9 to 7
move 2 from 7 to 6
move 3 from 3 to 2
move 1 from 7 to 8
move 1 from 9 to 6
move 1 from 9 to 8
move 2 from 8 to 2
move 1 from 1 to 2
move 1 from 3 to 7
move 4 from 1 to 7
move 19 from 2 to 5
move 1 from 1 to 4
move 1 from 7 to 4
move 1 from 1 to 5
move 3 from 1 to 4
move 1 from 1 to 8
move 6 from 2 to 4
move 7 from 2 to 1
move 2 from 7 to 9
move 8 from 2 to 8
move 2 from 7 to 3
move 1 from 6 to 4
move 10 from 4 to 6
move 5 from 6 to 7
move 2 from 9 to 8
move 6 from 8 to 9
move 1 from 2 to 3
move 2 from 8 to 3
move 5 from 1 to 8
move 8 from 5 to 2
move 8 from 8 to 7
move 7 from 2 to 8
move 1 from 1 to 2
move 1 from 9 to 7
move 1 from 4 to 2
move 2 from 2 to 6
move 5 from 9 to 3
move 2 from 8 to 6
move 2 from 3 to 9
move 4 from 8 to 6
move 7 from 6 to 1
move 8 from 1 to 5
move 1 from 8 to 7
move 1 from 9 to 6
move 12 from 5 to 3
move 1 from 4 to 8
move 2 from 9 to 5
move 1 from 2 to 3
move 3 from 5 to 1
move 1 from 1 to 5
move 21 from 3 to 8
move 2 from 1 to 5
move 6 from 5 to 7
move 2 from 5 to 6
move 10 from 6 to 9
move 1 from 6 to 8
move 13 from 8 to 2
move 2 from 5 to 4
move 2 from 4 to 3
move 4 from 9 to 1
move 5 from 7 to 8
move 12 from 8 to 1
move 5 from 9 to 6
move 1 from 3 to 7
move 2 from 6 to 5
move 11 from 2 to 1
move 1 from 8 to 4
move 16 from 1 to 9
move 1 from 2 to 6
move 1 from 8 to 5
move 12 from 9 to 3
move 14 from 7 to 2
move 1 from 7 to 9
move 1 from 4 to 2
move 1 from 7 to 5
move 3 from 9 to 5
move 4 from 6 to 9
move 3 from 9 to 4
move 1 from 8 to 4
move 2 from 4 to 5
move 1 from 7 to 1
move 5 from 3 to 5
move 2 from 4 to 2
move 8 from 2 to 7
move 7 from 2 to 4
move 1 from 3 to 7
move 3 from 9 to 7
move 2 from 2 to 9
move 3 from 4 to 5
move 6 from 1 to 8
move 6 from 1 to 5
move 3 from 9 to 2
move 22 from 5 to 9
move 1 from 5 to 6
move 2 from 2 to 3
move 5 from 7 to 6
move 5 from 8 to 9
move 2 from 7 to 2
move 20 from 9 to 4
move 1 from 8 to 3
move 2 from 2 to 5
move 1 from 2 to 5
move 15 from 4 to 8
move 1 from 5 to 7
move 6 from 9 to 1
move 5 from 4 to 8
move 2 from 4 to 8
move 1 from 2 to 1
move 5 from 6 to 5
move 5 from 5 to 7
move 1 from 9 to 8
move 5 from 7 to 2
move 2 from 5 to 1
move 4 from 7 to 5
move 1 from 5 to 9
move 1 from 6 to 8
move 1 from 7 to 2
move 6 from 3 to 4
move 3 from 5 to 7
move 1 from 9 to 2
move 6 from 2 to 3
move 1 from 3 to 4
move 13 from 8 to 9
move 7 from 1 to 5
move 6 from 9 to 2
move 1 from 1 to 4
move 6 from 2 to 3
move 1 from 1 to 4
move 5 from 9 to 7
move 11 from 8 to 4
move 7 from 7 to 3
move 2 from 7 to 8
move 1 from 8 to 2
move 8 from 4 to 1
move 2 from 1 to 6
move 2 from 5 to 8
move 3 from 1 to 9
move 1 from 8 to 2
move 11 from 3 to 2
move 2 from 8 to 9
move 9 from 4 to 7
move 11 from 3 to 8
move 7 from 9 to 6
move 5 from 4 to 6
move 3 from 7 to 3
move 1 from 7 to 1
move 5 from 7 to 6
move 2 from 3 to 5
move 1 from 3 to 4
move 5 from 2 to 5
move 1 from 1 to 7
move 1 from 4 to 8
move 1 from 7 to 6
move 7 from 5 to 7
move 2 from 5 to 7
move 3 from 1 to 7
move 1 from 2 to 3
move 1 from 6 to 4
move 1 from 3 to 4
move 1 from 5 to 3
move 18 from 6 to 4
move 9 from 7 to 1
move 14 from 4 to 6
move 3 from 6 to 4
move 12 from 6 to 7
move 2 from 5 to 3
move 3 from 7 to 4
move 6 from 4 to 7
move 5 from 1 to 7
move 5 from 4 to 5
move 5 from 2 to 1
move 9 from 8 to 4
move 9 from 1 to 3
move 2 from 8 to 2
move 4 from 2 to 4
move 1 from 7 to 6
move 1 from 2 to 3
move 1 from 8 to 9
move 1 from 6 to 9
move 2 from 9 to 3
move 3 from 4 to 1
move 13 from 3 to 5
move 12 from 5 to 1
move 7 from 1 to 8
move 1 from 3 to 6
move 4 from 5 to 4
move 1 from 5 to 2
move 8 from 4 to 9"""


print(solve(sample))
print(solve2(puzzle))
