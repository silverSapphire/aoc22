#!/usr/bin/env python3
from operator import add, sub
import math

NUM_KNOTS = 10

def getData():
    return [x.strip() for x in open('input.txt').readlines()]

def parseData(lines):
    motions = []
    for line in lines:
        motions.append(tuple(line.split()))

    return motions

def getDelta(dir):
    if(dir == 'U'): return (0, 1)
    elif(dir == 'D'): return (0, -1)
    elif(dir == 'L'): return (-1, 0)
    elif(dir == 'R'): return (1, 0)
    elif(dir == None): return (0, 0)

def normalize(x):
    if x > 0: return x - 1
    elif x < 0: return x + 1
    else: return x

def copySign(x):
    if x < 0: return -1
    if x > 0: return 1

def step(dir, head, tail, pos):
    head = list(map(add, head, getDelta(dir)))

    gap = list(map(sub, head, tail))
    if math.sqrt(sum(x*x for x in gap)) > math.sqrt(2):
        if all(gap):
            normalized = list(map(copySign, gap))
        else:
            normalized = list(map(normalize, gap))
        tail = list(map(add, tail, normalized))
        pos.add(tuple(tail))

    return head, tail, pos

def solve1(motions):
    head = [0, 0]
    tail = [0, 0]
    pos = {(0, 0)}

    for dir, num in motions:
        for _ in range(int(num)):
            head, tail, pos = step(dir, head, tail, pos)

    return len(pos)

def solve2(motions):
    knots = [[0, 0] for x in range(NUM_KNOTS)]
    pos = [{(0, 0)} for x in range(NUM_KNOTS)]

    for dir, num in motions:
        for _ in range(int(num)):
            for i in range(NUM_KNOTS - 1):
                knots[i], knots[i+1], pos[i+1] = \
                    step(dir if i == 0 else None, knots[i], knots[i+1], pos[i+1])

    return len(pos[9])

if __name__ == "__main__":
    data = parseData(getData())
    print(''.join(["The solution to Part One is ", str(solve1(data))]))
    print(''.join(["The solution to Part Two is ", str(solve2(data))]))