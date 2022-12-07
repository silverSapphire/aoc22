#!/usr/bin/env python3
from collections import deque

def getData():
    return [x.strip() for x in open('input.txt').readlines()]

def parseData(lines):
    splitIdx = lines.index("")
    initial = lines[:splitIdx-1]
    instr = lines[splitIdx+1:]
    numStacks = max([int(x) for x in lines[splitIdx-1].split()])

    # Parse initial state
    stacks = [deque() for i in range(numStacks)]
    for line in initial:
        cleaned = line[1::4]
        for i, y in enumerate(cleaned):
            if y.strip(): stacks[i].appendleft(y)

    # Parse moves
    moves = []
    for i, line in enumerate(instr):
        digits = [int(x) if x.isdigit() else None for x in line.split(" ")]
        digits = [x for x in digits if x is not None]
        moves.append({'num': digits[0], 'start': digits[1] - 1, 'end': digits[2] - 1})

    return stacks, moves

def solve1(stacks, moves):
    for move in moves:
        for num in range(move['num']):
            x = stacks[move['start']].pop()
            stacks[move['end']].append(x)

    return [x[len(x)-1] for x in stacks]

if __name__ == "__main__":
    stacks, moves = parseData(getData())
    print(''.join(["The solution to Part One is ", str(solve1(stacks, moves))]))