from pathlib import Path


def get_input(filename):
    with open(Path(Path(__file__).parent, filename)) as f:
        return f.read().strip().splitlines()


def solve1(inputfile):
    lines = get_input(inputfile)
    score = 0
    for l in lines:
        opp, play = l.split()
        score += score_round(opp, play)
    return score

def score_round(opp, play):
    result =  {'AX': 3, 'AY': 6, 'AZ': 0, 'BX': 0, 'BY': 3, 'BZ': 6, 'CX': 6, 'CY': 0, 'CZ': 3}[opp + play]
    choice = {'X': 1, 'Y': 2, 'Z': 3}[play]
    return result + choice


def solve2(inputfile):
    lines = get_input(inputfile)
    score = 0
    for l in lines:
        opp, res = l.split()
        def get_player_symbol(opp,res):
            SYMBOLS = ['A', 'B', 'C']
            index = SYMBOLS.index(opp)
            offset = {'X': 2, 'Y': 0, 'Z': 1}[res]
            player_index = (index + offset) % 3
            return SYMBOLS[player_index]
        player = get_player_symbol(opp, res)
        round_score =  {'X': 0, 'Y': 3, 'Z': 6}[res] + {'A': 1, 'B': 2, 'C': 3}[player]
        score += round_score
    return score



if __name__ == '__main__':
    print(solve1('sample.txt'))
    print(solve1('puzzle.txt'))
    print(solve2('sample.txt'))
    print(solve2('puzzle.txt'))
