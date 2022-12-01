#!/usr/bin/env python3
import itertools as it

def getData():
    return parseData(getLines())

def getLines():
    return open('input.txt').readlines()

def parseData(lines):
    nums = [int(x.strip()) if x.strip().isdigit() else None for x in lines]
    return [list(i) for match, i in it.groupby(nums, lambda p: p != None) if match]

def solve(data):
    return max([sum(x) for x in data])
        
if __name__ == "__main__":
    data = getData()
    print(''.join(["The solution is ", str(solve(data))]))