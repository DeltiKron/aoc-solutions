from ctypes import Array
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from pprint import pprint
from typing import Optional


def get_input(filename):
    with open(Path(Path(__file__).parent, filename)) as f:
        return f.read().strip().splitlines()


sample = get_input("sample.txt")
puzzle = get_input("puzzle.txt")


LS = "$ ls"
CD = "$ cd"
DIR = "dir"


def solve1(input_data):
    current_path = Path("/")
    paths = {current_path: (set(), set())}

    for line in input_data:
        if line.startswith(CD):
            current_path = (Path(current_path) / line.split(" ")[-1]).resolve()
            if current_path not in paths:
                paths[current_path] = (set(), set())
        elif line.startswith(LS):
            pass
        elif line.startswith(DIR):
            paths[current_path][0].add(current_path / line.split(" ")[-1])
        else:
            paths[current_path][1].add(tuple(line.split(" ")))
    print(paths)

    @lru_cache
    def get_size(path: Path) -> int:
        dirs, files = paths[path]
        return sum([*map(get_size, dirs)]) + sum([int(size) for size, _ in files])

    good_order = sorted(paths.keys(), key=lambda k: len(str(k)))[::-1]
    sizes = {str(path): get_size(path) for path in good_order}
    res1 = sum([v for v in sizes.values() if v < 100000])
    occupied = sizes["/"]
    total = 70000000
    needed = 30000000 - (total - occupied)
    print("Total space:", 70000000)
    print("Occupied space:", occupied)
    print("Space needed:", needed)
    res2 = list(
        [s for _, s in sorted(sizes.items(), key=lambda x: x[1]) if s >= needed]
    )[0]
    print(res2)
    return res1


assert solve1(sample) == 95437
print(solve1(puzzle))
