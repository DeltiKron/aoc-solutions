from functools import lru_cache
from itertools import chain, combinations_with_replacement, permutations
from pprint import pprint
import re
from helpers import read_input
from tqdm import tqdm

sample = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

puzzle = read_input(2024, 7)


def parse_line(line):
    sol, rest = line.split(":")
    return int(sol), *map(int, rest.split())


def parse_input(puzzle):
    for line in puzzle.split("\n"):
        solution, *numbers = parse_line(line)
        yield solution, numbers


cache = dict()

operations = {"+": lambda x, y: x + y, "*": lambda x, y: x * y, "|": lambda x, y: int(str(x) + str(y))}


def reduce_func(numbers, operators):
    if (numbers, operators) not in cache:
        if len(numbers) == 2:
            cache[(numbers, operators)] = operations[operators[0]](*numbers)
        else:
            cache[(numbers, operators)] = operations[operators[-1]](
                numbers[-1], reduce_func(numbers[:-1], operators[:-1])
            )
    return cache[(numbers, operators)]


assert reduce_func(tuple(range(5)), tuple(["+"] * 4)) == sum(range(5))
assert reduce_func((81, 40, 27), ("+", "*")) == 3267
assert reduce_func((11, 6, 16, 20), ("+", "*", "+")) == 292


@lru_cache
def get_combinations(operators, r):
    res = set()
    for r in chain.from_iterable((permutations(sample) for sample in combinations_with_replacement(operators, r))):
        res.add(tuple(r))
    return tuple(res)


pprint(list(get_combinations("+*", 3)))


def check_line(sol, inputs, operators=("*", "+")):
    print(len(inputs))
    print(sol, inputs)
    operator_combos = get_combinations(operators, len(inputs) - 1)
    print(len(operator_combos))
    solutions = (sol == reduce_func(tuple(inputs), tuple(op_combo)) for op_combo in operator_combos)
    result = sol if any(solutions) else 0
    return result


def solve1(puzzle):
    result = 0
    for sol, inputs in tqdm(parse_input(puzzle)):
        result += check_line(sol, inputs)
    return result


def solve2(puzzle):
    result = 0
    for sol, inputs in tqdm(parse_input(puzzle)):
        result += check_line(sol, inputs, ("*", "+", "|"))
    return result


assert check_line(156, [15, 6], ("*", "+", "|")) == 156
assert reduce_func((6, 8, 6, 15), ("*", "|", "*")) == 7290
assert check_line(7290, [6, 8, 6, 15], ("*", "+", "|")) == 156

# print(solve1(sample))
# print(solve1(puzzle))
print(solve2(sample))
