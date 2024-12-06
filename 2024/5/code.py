from itertools import chain
import re
from helpers import read_input

sample = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

puzzle = read_input(2024, 5)


def validate_update(update, ruleset):
    for i, page in enumerate(update):
        if page not in ruleset:
            continue
        rules = ruleset[page]
        if set(rules).intersection(set(update[:i])):
            return 0
    # print(update, update[(len(update) // 2)])
    return update[(len(update) // 2)]


def reorder_pages(update, ruleset):
    result = []
    for page in update:
        rules = ruleset.get(page, set())
        for j in range(len(result), 0, -1):
            pages_before = result[:j]
            pages_after = result[j:]
            individual_rules_after = list(chain(ruleset.get(p, set()) for p in pages_after)) or [set()]
            rules_after = set.union(*individual_rules_after)

            if rules.intersection(set(pages_before)):
                continue
            if page in rules_after:
                raise ValueError("Invalid page order")
            result.insert(j, page)
            break
        else:
            result.insert(0, page)
    return result[len(result) // 2]


def parse_puzzle(puzzle):
    rule_list, updates = puzzle.split("\n\n")
    rules = re.findall(r"(\d+)\|(\d+)", rule_list)
    rules = [(int(i), int(j)) for i, j in rules]
    # print(rules)
    update_sets = [list(map(lambda x: int(x.strip()), i.split(","))) for i in updates.split("\n")]

    ruleset = dict()
    for i, j in rules:
        if i in ruleset:
            ruleset[i].add(j)
        else:
            ruleset[i] = set([j])
    return ruleset, update_sets


def solve1(puzzle):
    ruleset, update_sets = parse_puzzle(puzzle)
    return sum(validate_update(i, ruleset) for i in update_sets)


def solve2(puzzle):
    ruleset, update_sets = parse_puzzle(puzzle)

    def process_update(update, ruleset):
        if validate_update(update, ruleset) != 0:
            return 0

        return reorder_pages(update, ruleset)

    middle_pages = [process_update(i, ruleset) for i in update_sets]
    return sum(middle_pages)


print(solve1(sample))
print(solve1(puzzle))
print(solve2(sample))
print(solve2(puzzle))
