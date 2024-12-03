from dataclasses import dataclass, field
from functools import reduce
from itertools import product
from pprint import pprint
from typing import Dict, List
from helpers.helpers import Grid, read_input


puzzle = read_input(2022, 10)
sample = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""


@dataclass
class Monkey:
    number: str = field(init=True)
    items: List[int] = field(init=False)
    true_target: str = field(init=False)
    false_target: str = field(init=False)
    operation_desc: str = field(init=False)
    test_desc: str = field(init=False)
    n_inspections = 0
    debug_on = False

    def debug(self, *args):
        if self.debug_on:
            print(*args)

    def reduce_worry(self, item):
        return item // 3

    def process_item(self, monkeys):
        item = self.items.pop(0)
        self.debug("Monkey ", self.number, " inspects an item with a worry level of", item)
        item = self.operation(item)
        self.debug("Worry level increases to", item)
        self.debug("Monkey bored: Worry by 3 to", item := self.reduce_worry(item))
        target = self.true_target if self.test(item) else self.false_target
        self.debug(
            "Test ", self.test_desc, " is ", self.test(item), " item with level ", item, " is thrown to ", target
        )
        self.n_inspections += 1
        self.pass_item(monkeys, target, item)

    def pass_item(self, monkeys, target, item):
        monkeys[target].items.append(item)

    def take_turn(self, monkeys):
        while len(self.items):
            self.process_item(monkeys)

    def __init__(self, number: str):
        self.number = number


def setup_puzzle(puzzle_text, constructor=Monkey):
    monkeys = dict()
    number = None
    for line in map(str.strip, puzzle_text.split("\n")):
        if line.startswith("Monkey"):
            number = line.split()[-1][:-1]
            monkeys[number] = constructor(number)
        elif line.startswith("Starting items"):
            monkeys[number].items = list(
                map(int, filter(lambda x: len(x.strip()) > 0, line.split(":")[-1].split(", ")))
            )
        elif line.startswith("Operation"):
            monkeys[number].operation_desc = line.split(":")[-1]
            monkeys[number].operation = parse_operation(monkeys[number].operation_desc)
        elif line.startswith("Test"):
            monkeys[number].test_desc = line.split(":")[-1]
            monkeys[number].test = parse_test(line.split(":")[-1])
        elif line.startswith("If true"):
            monkeys[number].true_target = line.split()[-1]
        elif line.startswith("If false"):
            monkeys[number].false_target = line.split()[-1]
    return monkeys


def parse_operation(text: str):
    return lambda old: eval(text.split("=")[-1])


def parse_test(text: str):
    return lambda x: x % int(text.split()[-1]) == 0


def solve1(puzzle):
    monkeys = setup_puzzle(puzzle)
    order = sorted(list(monkeys.keys()))

    def debug_print(monkeys, round):
        print("*" * 8, round, "*" * 8)
        for o in order:
            print(o, monkeys[o].items)

    def round(round_i):
        for n in order:
            monkeys[n].take_turn(monkeys)
        # debug_print(monkeys, round_i)
        # exit()

    for i in range(20):
        round(i + 1)
    counters = list([m.n_inspections for m in monkeys.values()])
    print(counters)
    return reduce(lambda a, b: a * b, sorted(counters)[-2:], 1)


def solve2(puzzle):
    class Monkey2(Monkey):
        def reduce_worry(self, item):
            return item

        def pass_item(self, *args):
            super(Monkey2, self).pass_item(*args[:-1], args[-1] % self.megamod)

    monkeys = setup_puzzle(puzzle, Monkey2)

    megamod = reduce(lambda a, b: a * b, [int(m.test_desc.split()[-1]) for m in monkeys.values()])
    for m in monkeys.values():
        m.megamod = megamod

    order = sorted(list(monkeys.keys()))

    def debug_print(monkeys, round):
        if round in [1, 20, 1000]:
            print(8 * "*", round, 8 * "*")
            for mi in sorted(list(monkeys.keys())):
                print("Monkey", mi, "inspected items", monkeys[mi].n_inspections, "times")

    def round(round_i):
        for n in order:
            monkeys[n].take_turn(monkeys)
        debug_print(monkeys, round_i)
        # exit()

    for i in range(10000):
        round(i + 1)
    counters = list([m.n_inspections for m in monkeys.values()])
    print(counters)
    return reduce(lambda a, b: a * b, sorted(counters)[-2:], 1)


print(solve1(sample))
print(solve1(read_input(2022, "11")))
# print(solve1(puzzle))
print(solve2(sample))
print(solve2(read_input(2022, "11")))
