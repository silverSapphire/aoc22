#!/usr/bin/env python3

def getData():
    return [x.strip() for x in open('input.txt').readlines()]

def parseData(lines):
    return lines[0]

def solve1(data, markerlen):
    for start in range(len(data)):
        s = {y for y in [x for x in data[start:start + markerlen]]}
        if len(s) == markerlen:
            return start + markerlen

if __name__ == "__main__":
    data = parseData(getData())
    print(''.join(["The solution to Part One is ", str(solve1(data, 4))]))
    print(''.join(["The solution to Part One is ", str(solve1(data, 14))]))