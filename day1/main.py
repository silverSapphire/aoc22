#!/usr/bin/env python3
import itertools as it

def getData():
    return parseData(getLines())

def getLines():
    return open('input.txt').readlines()

def parseData(lines):
    nums = [int(x.strip()) if x.strip().isdigit() else None for x in lines]
    return [list(i) for match, i in it.groupby(nums, lambda p: p != None) if match]

def solve1(data):
    return max([sum(i) for i in data])

def solve2(data):
    return sum(sorted([sum(i) for i in data], reverse=True)[:3])
        
if __name__ == "__main__":
    data = getData()
    print(''.join(["The solution to Part One is ", str(solve1(data))]))
    print(''.join(["The solution to Part Two is ", str(solve2(data))]))