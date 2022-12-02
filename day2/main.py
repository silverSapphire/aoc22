#!/usr/bin/env python3
import itertools as it

def getData():
    return parseData(getLines())

def getLines():
    return open('input.txt').readlines()

def translate(x):
    m = {"C": 3, "Y": 3, "B": 2, "A": 1, "X": 0, "Z": 6}
    return m[x]

def symbolPts(i, j):
    wins = {1: 2, 2: 3, 3: 1}
    loses = {1: 3, 2: 1, 3: 2}
    if j is 3:
        return i
    if j is 6:
        return wins[i]
    else:
        return loses[i]

def parseData(lines):
    return map(translate, [i for j in [x.split() for x in lines] for i in j])

def solve1(plays):
    score = 0
    for i, j in zip(plays[0::2], plays[1::2]):
        score = score + j + symbolPts(i, j)
    return score

if __name__ == "__main__":
    data = getData()
    print(''.join(["The solution to Part One is ", str(solve1(data))]))