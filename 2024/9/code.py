from dataclasses import dataclass
from enum import Enum
from typing import Iterable
from helpers import read_input

sample = """2333133121414131402"""

puzzle = read_input(2024, 9)


class BlockType(Enum):
    SPACE='SPACE'
    FILE='FILE'

@dataclass
class Scorer():
    debug_str=''
    i=0
    total=0

    def add(self,v):
        self.total+=self.i*v
        self.i+=1
        self.debug_str+=str(v)
    
    def add_batch(self, values: Iterable[int]):
        for v in values:
            self.add(v)


        

@dataclass
class Defragger:
    next_type = BlockType.FILE
    free_spaces = 0
    next_file_id = 0
    remaining_blocks = []
    checksum = 0
    scorer:Scorer

    def process_next(self, size):
        match self.next_type:
            case BlockType.FILE:
                self.remaining_blocks.append((size, self.next_file_id))
                self.next_file_id +=1
            case BlockType.SPACE:
                self.free_spaces = 0
        self.compact()

    def partial_pull(self):
        score = 0
        while True:
            if len(self.remaining_blocks) == 0 or self.free_spaces==0:
                return score
            size, curr_id = self.remaining_blocks.pop(0)
            take = min(self.free_spaces, size)
            size = size - take
            self.free_spaces -=take
            self.scorer.add_batch([curr_id]*take)
            if size > 0:
                self.remaining_blocks.insert(0, (size, curr_id))

    def compact(self):
        if len(self.remaining_blocks) == 0:
            return
        if self.free_spaces > 0:
            self.partial_pull()
            return         
        size, curr_id = self.remaining_blocks.pop()
        self.scorer.add_batch(size * [curr_id])

def solve1(puzzle):
    scorer = Scorer()
    dfg = Defragger(scorer)
    for block in puzzle:
        dfg.process_next(int(block))
    dfg.compact()
    print(scorer.debug_str)
    return scorer.total



print(solve1(sample))


# ToDo:
# This algorithm fills the next block. Instead, I need to collect all blocks and then start filling the spaces from the back 