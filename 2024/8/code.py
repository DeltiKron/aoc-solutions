from collections import Counter
from itertools import combinations
import math
from helpers import read_input
from helpers import Grid

sample = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

puzzle = read_input(2024, 8)

def parse_input(puzzle):
    return Grid.from_text(puzzle, cast_func=str)
    

def solve1(puzzle):
    grid = parse_input(puzzle)
    
    def search_func(p, g:Grid):
        val = g.at(*p)
        if val != '.':
            return True, val
        return False, False

    points = list(grid.find_where(search_func))

    counts = Counter([p[0] for p in points])

    antinodes = set()
    antinodes_2 = set()

    for v, c in counts.items():
        if c <2 :
            continue
        positions = {p[1] for p in points if p[0] == v}
        for p1,p2 in combinations(positions,r=2):
            antinodes_i = get_antinodes(p1,p2)
            for a in antinodes_i: 
                if grid.is_in_bounds(*a):
                    antinodes.add(a)
            antinodes_2 = antinodes_2.union(set(get_antinodes2(p1,p2, grid)))
    return len(antinodes),len(antinodes_2)


def get_antinodes(p1,p2,*_):
    d = p1[0]-p2[0], p1[1]-p2[1]
    a1 = p1[0]+d[0],p1[1]+d[1]
    a2 = p2[0]-d[0],p2[1]-d[1]
    return a1, a2

def get_antinodes2(p1,p2,grid:Grid):
    d = p1[0]-p2[0], p1[1]-p2[1]
    gcd = math.gcd(*d)
    d_norm = d[0]/gcd, d[1]/gcd
    
    # p2 -> inft
    # p1 -< -ifty

    a = set()

    for mult, start in zip([-1,1],[p1,p2]):
        p = start
        while grid.is_in_bounds(*p):
            a.add(p)
            p = d_norm[0]*mult+p[0], d_norm[1]*mult+p[1]
    return a

print(solve1(sample))
print(solve1(puzzle))
