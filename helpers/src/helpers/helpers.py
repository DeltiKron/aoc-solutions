from dataclasses import dataclass, field

from pathlib import Path
import re
from typing import List


def read_input(year, day_number: int):
    path = Path.cwd() / str(year)
    pattern = re.compile(f".*\D{day_number}\D.*(?:(?!\.py|\.ipynb))$")
    files = list(filter(lambda x: pattern.match(x.name), path.rglob(f"*input*.txt")))
    if len(files) < 1:
        raise Exception(f"No input found for Day {day_number}")
    with open(files[0]) as infile:
        raw = infile.readlines()
        return "".join(filter(lambda x: len(x.strip()) > 0, raw))


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

    @property
    def len_y(self):
        return len(self.data)

    @property
    def len_x(self):
        return len(self.data[0])

    def at(self, x, y):
        self._validate_coords(x, y)
        return self.cast_func(self.data[y][x])

    def _validate_coords(self, x, y):
        assert x < self.len_x, "Out of bound in x"
        assert y < self.len_y, "Out of bound in y"
        assert 0 <= x, "Out of bound in x"
        assert 0 <= y, "Out of bound in x"

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
    def cols(self):
        for i in range(self.len_x):
            yield self.col(i)

    def print(self):
        for r in self.rows:
            print(" " + " ".join(r))
