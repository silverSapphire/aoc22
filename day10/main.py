#!/usr/bin/env python3

def getData():
    return [x.strip() for x in open('input.txt').readlines()]

def parseData(lines):
    ins = []
    for line in lines:
        ins.append(tuple(line.split()))

    return ins

def process(ins):
    cycle = 0
    x = 1
    states = [(cycle, x)]
    for i in ins:
        if i[0] == 'addx':
            states.append((cycle + 1, x))
            states.append((cycle + 2, x))
            cycle = cycle + 2
            x = x + int(i[1])
        else:
            states.append((cycle + 1, x))
            cycle = cycle + 1

    return states

def solve1(data):
    states = process(data)
    sum = 0
    for i in range(20, 221, 40):
        sum = sum + states[i][0] * states[i][1]

    return sum

if __name__ == "__main__":
    data = parseData(getData())
    print(''.join(["The solution to Part One is ", str(solve1(data))]))