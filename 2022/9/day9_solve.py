from functools import reduce
from itertools import product
from helpers import Grid, read_input


puzzle = read_input(2022, 9).split("\n")
sample = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".split("\n")


sample2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""".split("\n")
# print(puzzle)


def move_tail(tail, head):
    tx, ty = tail
    hx, hy = head
    dx, dy = hx - tx, hy - ty

    if any([abs(dx) > 2, abs(dy) > 2]):
        raise Exception(f"Unexpected head movement tail:{tail}, head:{head}, delta:{(dx,dy)}")
    if abs(dx) == 2 and abs(dy) < 2:
        tx = dx / abs(dx) + tx
        ty = ty if dy == 0 else ty + dy / abs(dy)
    if abs(dy) == 2 and abs(dx) < 2:
        ty = dy / abs(dy) + ty
        tx = tx if dx == 0 else tx + dx / abs(dx)
    if abs(dx) == 2 and abs(dy) == 2:
        ty = dy / abs(dy) + ty
        tx = dx / abs(dx) + tx
    return (int(tx), int(ty))


def solve1(puzzle):
    directions = dict(U=(0, 1), D=(0, -1), L=(-1, 0), R=(1, 0))
    start = (0, 0)
    head = start
    tail = start

    visited_by_tail = set()

    def get_next(start, direction, steps=1):
        dx, dy = directions.get(direction)
        sx, sy = start
        return sx + dx, sy + dy

    for line in puzzle:
        if line == "":
            continue
        direction, steps = line.strip().split()
        # print(head, tail)
        for _ in range(int(steps)):
            head = get_next(head, direction)
            tail = move_tail(tail, head)
            visited_by_tail.add(tail)
            # print(head, tail)
    return len(visited_by_tail)


def solve2(puzzle):
    directions = dict(U=(0, 1), D=(0, -1), L=(-1, 0), R=(1, 0))
    start = (0, 0)

    rope = [start] * 10

    visited_by_tail = set()

    def get_next(start, direction, steps=1):
        dx, dy = directions.get(direction)
        sx, sy = start
        return sx + dx, sy + dy

    for line in puzzle:
        if line == "":
            continue
        direction, steps = line.strip().split()
        # print(head, tail)
        for _ in range(int(steps)):
            rope[0] = get_next(rope[0], direction)
            for i in range(1, len(rope)):
                rope[i] = move_tail(rope[i], rope[i - 1])
            visited_by_tail.add(rope[-1])
    return len(visited_by_tail)


# print(solve1(sample))
# print(puzzle)
# print(solve1(puzzle))
print(solve2(sample2))
print(solve2(puzzle))
