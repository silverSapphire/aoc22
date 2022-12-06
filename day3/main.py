#!/usr/bin/env python3
import numpy as np

def getData():
    return [x.strip() for x in open('input.txt').readlines()]

def parseData1(lines):
    normalize = lambda x: ord(x) - ord('a') + 1 if ord(x) >= ord('a') else ord(x) - ord('A') + 27
    return [[{normalize(y) for y in x[:len(x)//2]}, 
              {normalize(z) for z in x[len(x)//2:]}] for x in lines]

def parseData2(lines):
    normalize = lambda x: ord(x) - ord('a') + 1 if ord(x) >= ord('a') else ord(x) - ord('A') + 27
    normalized = [{normalize(x) for x in y} for y in lines]
    return [x.tolist() for x in np.array_split(normalized, len(normalized) / 3)]

def solve1(data):
    intersection = [x & y for (x, y) in data]
    return sum([sum(x) for x in intersection])

def solve2(data):
    intersection = [x & y & z for (x, y, z) in data]
    return sum([sum(x) for x in intersection])

if __name__ == "__main__":
    print(''.join(["The solution to Part One is ", str(solve1(parseData1(getData())))]))
    print(''.join(["The solution to Part Two is ", str(solve2(parseData2(getData())))]))