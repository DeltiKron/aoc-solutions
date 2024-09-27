from pathlib import Path


def get_input(filename):
    with open(Path(Path(__file__).parent, filename)) as f:
        return f.read().strip().splitlines()


def main(infile):
    lines = get_input(infile)
    current_sum = 0
    max_sum = 0
    for line in lines:
        if line != "":
            current_sum += int(line)
        else:
            max_sum = max(max_sum, current_sum)
            current_sum = 0

    return max_sum


def main2(infile):
    lines = get_input(infile)
    current_sum = 0
    max_sum = []
    for line in lines:
        if line != "":
            current_sum += int(line)
        else:
            max_sum.append(current_sum)
            if len(max_sum) > 3:
                print(max_sum)
                max_sum = sorted(max_sum)[1:]
                print(max_sum)

            current_sum = 0
    max_sum.append(current_sum)
    if len(max_sum) > 3:
        print(max_sum)
        max_sum = sorted(max_sum)[1:]
        print(max_sum)

    return sum(max_sum)


if __name__ == "__main__":
    print(main("sample.txt"))
    print(main("puzzle.txt"))
    print(main2("sample.txt"))
    print(main2("puzzle.txt"))
