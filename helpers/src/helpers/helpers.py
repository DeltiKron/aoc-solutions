from copy import deepcopy
from dataclasses import dataclass, field

from enum import Enum
from pathlib import Path
import re
from typing import Callable, List, Tuple


class GridOutOfBoundsError(IndexError):
    pass


def read_input(year, day_number: int):
    path = Path.cwd() / str(year)
    pattern = re.compile(f".*\D{day_number}\D.*(?:(?!\.py|\.ipynb))$")
    files = list(filter(lambda x: pattern.match(x.name), path.rglob("*input*.txt")))
    if len(files) < 1:
        raise IOError(f"No input found for Day {day_number}")
    with open(files[0]) as infile:
        data = infile.read().strip("\n")
    assert len(data) > 0, f"Empty data for Day {day_number}"
    return data


@dataclass
class Grid:
    data: List[List[str]] = field(default_factory=lambda: [[]], init=False, repr=False)
    x: int = field(init=False, default=0)
    y: int = field(init=False, default=0)

    @classmethod
    def from_text(cls, grid_text, cast_func=int):
        g = cls()
        g.cast_func = cast_func
        g.data = list(filter(lambda x: len(x) > 0, grid_text.split("\n")))
        g.x = g.len_x
        g.y = g.len_x
        return g

    @classmethod
    def from_other(cls, other):
        return deepcopy(other)

    @property
    def len_y(self):
        return len(self.data)

    @property
    def len_x(self):
        return len(self.data[0])

    def at(self, x, y):
        self._validate_coords(x, y)
        return self.cast_func(self.data[y][x])

    def is_in_bounds(self, x,y):
        try:
            self._validate_coords(x,y)
            return True
        except GridOutOfBoundsError:
            return False

    def _validate_coords(self, x, y):
        oob_message = "Out of bound in {}"
        try:
            assert x < self.len_x, oob_message.format("x")
            assert y < self.len_y, oob_message.format("y")
            assert 0 <= x, oob_message.format("x")
            assert 0 <= y, oob_message.format("x")
        except AssertionError as e:
            raise GridOutOfBoundsError(e)

    def col(self, x):
        self._validate_coords(x, 0)
        return [row[x] for row in self.data]

    def row(self, y):
        self._validate_coords(0, y)
        return self.data[y]

    @property
    def rows(self):
        return (row for row in self.data)

    @property
    def indices(self):
        for x in range(self.len_x):
            for y in range(self.len_y):
                yield x, y

    @property
    def cols(self):
        for i in range(self.len_x):
            yield self.col(i)

    @property
    def diagonal_indexes_lb(self):
        start_indexes = [(0, i) for i in range(self.len_y - 1, 0, -1)]
        start_indexes += [(i, 0) for i in range(self.len_x)]
        for x, y in start_indexes:
            yield [(x + i, y + i) for i in range(min(self.len_x - x, self.len_y - y))]

    @property
    def diagonals_lb(self):
        for idxs in self.diagonal_indexes_lb:
            yield [self.at(x, y) for x, y in idxs]

    @property
    def diagonal_indexes_lt(self):
        start_indexes = [(0, i) for i in range(self.len_y - 1)]
        start_indexes += [(i, self.len_y - 1) for i in range(self.len_x)]
        for x, y in start_indexes:
            res = []
            for i in range(min(self.len_x - x, y + 1)):
                res.append((x + i, y - i))
            yield res

    @property
    def diagonals_lt(self):
        for idxs in self.diagonal_indexes_lt:
            yield [self.at(x, y) for x, y in idxs]

    def print(self):
        for r in self.rows:
            print(" " + " ".join(r))

    def find(self, target):
        for x, y in self.indices:
            if self.at(x, y) == target:
                yield x, y

    def set(self, x, y, value):
        self._validate_coords(x, y)
        line = list(item for item in self.data[y])
        line[x] = value
        self.data[y] = "".join(line)
    
    def find_where(self, check_node:Callable[[Tuple[int, int], 'Grid'],Tuple[bool, str]]):
        for coord in self.indices:
            match, res = check_node(coord,self)
            if match:
                yield res, coord



class GridDirection(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    def turn_left(self):
        return {
            self.UP: self.LEFT,
            self.LEFT: self.DOWN,
            self.DOWN: self.RIGHT,
            self.RIGHT: self.UP,
        }[self]

    def turn_right(self):
        return {
            self.LEFT: self.UP,
            self.DOWN: self.LEFT,
            self.RIGHT: self.DOWN,
            self.UP: self.RIGHT,
        }[self]
