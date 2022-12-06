#!/usr/bin/env python3
import itertools as it

def getData():
    return parseData([x.strip() for x in open('input.txt').readlines()])

def parseData(lines):
    normalize = lambda x: ord(x) - ord('a') + 1 if ord(x) >= ord('a') else ord(x) - ord('A') + 1 + 26
    return [[{normalize(y) for y in x[:len(x)//2]}, 
              {normalize(z) for z in x[len(x)//2:]}] for x in lines]

def solve1(data):
    intersection = [x & y for (x, y) in data]
    return sum([sum(x) for x in intersection])

if __name__ == "__main__":
    #11133 is too high
    print(''.join(["The solution to Part One is ", str(solve1(getData()))]))