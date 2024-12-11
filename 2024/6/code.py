from dataclasses import dataclass
from helpers import read_input
from helpers import Grid
from helpers import GridDirection
from helpers.helpers import GridOutOfBoundsError

sample = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

puzzle = read_input(2024, 6)


@dataclass
class Guard:
    x: int
    y: int
    direction: GridDirection

    def turn_left(self):
        self.direction = self.direction.turn_left()

    def turn_right(self):
        self.direction = self.direction.turn_right()

    def next_pos(self):
        return self.x + self.direction.value[0], self.y + self.direction.value[1]

    def move(self, grid):
        n_turns = 0
        while grid.at(*self.next_pos()) == "#":
            self.turn_right()
            n_turns += 1
            if n_turns > 4:
                raise StopIteration("Stuck in loop")
        self.x, self.y = self.next_pos()

    @property
    def sprite(self):
        return {
            GridDirection.UP: "^",
            GridDirection.DOWN: "v",
            GridDirection.LEFT: "<",
            GridDirection.RIGHT: ">",
        }[self.direction]


def parse_input(input):
    area = Grid.from_text(input, cast_func=lambda x: x if x in "^#" else None)
    # area.print()
    start = list(area.find("^"))[0]
    guard = Guard(*start, GridDirection.UP)
    return area, guard


def run_setup(grid: Grid, guard: Guard):
    while True:
        try:
            yield (guard.x, guard.y), guard.direction
            guard.move(grid)
        except GridOutOfBoundsError:
            break


def solve1(puzzle):
    grid, guard = parse_input(puzzle)
    positions = {p for p, _ in run_setup(grid, guard)}

    # for y in range(grid.len_x):
    #     line = ""
    #     for x in range(grid.len_y):
    #         line += "X" if (x, y) in positions else grid.at(x, y) or "."
    #     print("", " ".join(line))
    return len(positions)


def solve2(puzzle):
    grid, guard = parse_input(puzzle)

    start = guard.x, guard.y

    to_try = list(grid.indices)
    to_try.remove(start)

    known_loops = set()

    from tqdm import tqdm

    for x, y in tqdm(to_try):
        if grid.at(x, y) == "#" or (x, y) == start:
            continue
        known_states = set()
        grid_i = Grid.from_other(grid)
        grid_i.set(x, y, "#")

        guard_i = Guard(*start, GridDirection.UP)

        while True:
            state = (guard_i.x, guard_i.y), guard_i.direction
            if state in known_states:
                # grid_i.print()
                # print()
                known_loops.add((x, y))
                break
            try:
                known_states.add(state)
                guard_i.move(grid_i)
                grid_i.set(guard_i.x, guard_i.y, guard_i.sprite)
            except GridOutOfBoundsError:
                break
    print(known_loops)
    return len(known_loops)


# print(solve1(sample))
# print(solve1(puzzle))
print(solve2(sample))
print(solve2(puzzle))
