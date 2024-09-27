from pathlib import Path


def get_input(filename):
    with open(Path(Path(__file__).parent, filename)) as f:
        return f.read().strip().splitlines()


def main(infile):
    lines = get_input(infile)
    currentSum = 0
    maxSum = 0
    for l in lines:
        if l != "":
            currentSum += int(l)
        else:
            maxSum = max(maxSum, currentSum)
            currentSum = 0

    return maxSum


def main2(infile):
    lines = get_input(infile)
    currentSum = 0
    maxSum = []
    for l in lines:
        if l != "":
            currentSum += int(l)
        else:
            maxSum.append(currentSum)
            if len(maxSum) > 3:
                print(maxSum)
                maxSum = sorted(maxSum)[1:]
                print(maxSum)

            currentSum = 0
    maxSum.append(currentSum)
    if len(maxSum) > 3:
        print(maxSum)
        maxSum = sorted(maxSum)[1:]
        print(maxSum)

    return sum(maxSum)


if __name__ == "__main__":
    print(main("sample.txt"))
    print(main("puzzle.txt"))
    print(main2("sample.txt"))
    print(main2("puzzle.txt"))
