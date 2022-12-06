#!/usr/bin/env python3
import numpy as np

def getData():
    return [x.strip() for x in open('input.txt').readlines()]

def parseData1(lines):
    lines = [x.split(",") for x in lines]
    lines = [x.split("-") for y in lines for x in y]
    return [x.tolist() for x in np.array_split(lines, len(lines) / 2)]

def solve1(data):
    isSubset = []
    for l in data:
        first = {x for x in list(range(int(l[0][0]), int(l[0][1]) + 1))}
        second = {x for x in list(range(int(l[1][0]), int(l[1][1]) + 1))}
        isSubset.append(first.issubset((second)) or second.issubset((first)))

    return sum(isSubset)

if __name__ == "__main__":
    print(''.join(["The solution to Part One is ", str(solve1(parseData1(getData())))]))