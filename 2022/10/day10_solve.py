from functools import reduce
from itertools import product
from helpers import Grid, read_input


puzzle = read_input(10)
sample = read_input("10_sample")


class Computer:


    def __init__(self, callback):
        self.to_add = dict()
        self.X = 1
        self.cycle = 1
        self.callback = callback

    def _next_cycle(self):
        self.callback(self, self.cycle)
        self.cycle += 1
        # print(self.cycle)
        changes = self.to_add.get(self.cycle) or [0]
        self.X += sum(changes)
        
    def addx(self, change):
        # print('running addx',change)
        target_cycle = self.cycle + 2
        if target_cycle not in self.to_add:
            self.to_add[target_cycle] = []
        self.to_add[target_cycle].append(change)

        # Takes two cycles to execute
        self.noop()
        self.noop()

    def noop(self):
        # print("running noop")
        self._next_cycle()

    def execute_command(self, command: str):
        if command.startswith("addx"):
            self.addx(int(command.split()[-1]))
        else:
            self.noop()


def solve1(text):
    sum_importance = 0

    def cycle_callback(c: Computer, cycle):
        # print("callback")
        if cycle > 220:
            pass
        if (cycle - 20) % 40 == 0:
            nonlocal sum_importance
            sum_importance += c.cycle * c.X
            # print(sum_importance)

    c = Computer(cycle_callback)
    for line in text.split("\n"):
        # print(line)
        c.execute_command(line)
    return sum_importance

def solve2(text):
    line = ''
    
    def cycle_callback(c: Computer, cycle):
        pos_sprite = c.X
        pos_pixel = (cycle-1) % 40
        nonlocal line
        line += '#' if abs(pos_sprite - pos_pixel) <= 1 else ' '
        if len(line) == 40:
            print(line)
            line = ''
            
    c = Computer(cycle_callback)
    for command in text.split("\n"):
        # print(line)
        c.execute_command(command)
    # return sum_importance



# print(solve1(sample))
# print(solve1(puzzle))
# print(solve1(puzzle))
print(solve2(sample))
print(solve2(puzzle))
