from pathlib import Path


def get_input(filename):
    with open(Path(Path(__file__).parent, filename)) as f:
        return f.read().strip().splitlines()


def parse_input(lines):
    split = lines.index("")
    crates = lines[:split]
    moves = lines[split + 1 :]
    return crates, moves


def parse_crates(lines):
    lines == lines[::-1]
    width = max(map(lambda x: len(x), lines))
    for layer, line in enumerate(lines):
        for i in range(1, min(width - 1, len(line)), 4):
            print(layer, line[i], i)


def solve1(inputfile):
    lines = get_input(inputfile)
    crates, _ = parse_input(lines)
    parse_crates(crates)


if __name__ == "__main__":
    print(solve1("sample.txt"))
    # print(solve2("puzzle.txt"))
