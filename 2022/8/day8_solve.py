from functools import reduce
from itertools import product
from helpers import Grid, read_input


puzzle = read_input(2022, 8)
sample = """
30373
25512
65332
33549
35390"""

# print(puzzle)


def solve1(text):
    g = Grid.from_text(text)

    # g.print()

    visible = set()

    ranges_x = [
        range(g.len_x),
        range(g.len_x - 1, -1, -1),
    ]
    ranges_y = [
        range(g.len_y),
        range(g.len_y - 1, -1, -1),
    ]

    for x in ranges_x[0]:
        for ry in ranges_y:
            max_height = -1
            for y in ry:
                h = int(g.at(x, y))
                if h > max_height:
                    max_height = h
                    visible.add((x, y))

    for y in ranges_y[0]:
        for rx in ranges_x:
            max_height = -1
            for x in rx:
                h = int(g.at(x, y))
                if h > max_height:
                    max_height = h
                    visible.add((x, y))

    print(len(visible))


def solve2(text):
    g = Grid.from_text(text)
    xy_max = ()
    score_max = 0
    for xy in product(range(g.len_x), range(g.len_y)):
        score = scenic_score(*xy, g)
        if score > score_max:
            xy_max = xy
            score_max = score
    print(score_max, xy_max)


def scenic_score(x, y, g: Grid):
    if x == 0 or y == 0:
        return 0
    left = [(xi, y) for xi in range(x - 1, -1, -1)]
    right = [(xi, y) for xi in range(x + 1, g.len_x)]
    up = [(x, yi) for yi in range(y - 1, -1, -1)]
    down = [(x, yi) for yi in range(y + 1, g.len_y)]

    assert len(left) + len(right) == g.len_x - 1
    assert len(up) + len(down) == g.len_y - 1

    h0 = int(g.at(x, y))
    # print(x,y, h0)
    scores = list(
        map(
            lambda a: get_visible2(g, a, h0),
            [
                up,
                right,
                down,
                left,
            ],
        )
    )
    final_score = reduce(lambda a, b: a * b, scores, 1)
    # print((x,y),h0, "scores",scores, final_score)
    return final_score


def get_visible2(g, indexes, h0):
    n = 0
    for xy in indexes:
        n += 1
        if g.at(*xy) >= h0:
            return n
    return n


solve1(sample)
solve1(puzzle)
solve2(sample)
solve2(puzzle)
