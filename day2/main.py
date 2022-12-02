#!/usr/bin/env python3
import itertools as it

def getData():
    return parseData(getLines())

def getLines():
    return open('input.txt').readlines()

def translate(x):
    if x is "C" or x is "Z":
        return 3
    if x is "B" or x is "Y":
        return 2
    if x is "A" or x is "X":
        return 1

def outcomePts(i, j):
    losses = [[1, 3], [2, 1], [3, 2]]
    if i is j:
        return 3
    if [i, j] in losses:
        return 0
    else:
        return 6

def parseData(lines):
    return map(translate, [i for j in [x.split() for x in lines] for i in j])

def solve1(plays):
    score = 0
    for i, j in zip(plays[0::2], plays[1::2]):
        score = score + j + outcomePts(i, j)
    return score

#def solve2(data):
#    return sum(sorted([sum(i) for i in data], reverse=True)[:3])
        
if __name__ == "__main__":
    data = getData()
    print(''.join(["The solution to Part One is ", str(solve1(data))]))
#    print(''.join(["The solution to Part Two is ", str(solve2(data))]))