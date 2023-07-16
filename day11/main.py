#!/usr/bin/env python3
import numpy as np
from collections import deque
import copy

LINES_PER_MONKEY = 7

class Monkey:
    def __init__(self, items, op, test, ifTrue, ifFalse):
        self.items = deque(items)
        self.numInspected = 0
        self.op = eval("lambda old: " + op)
        self.testValue = int(test)
        self.testLambda = eval("lambda x: x % " + test + ("is 0"))
        self.ifTrue = int(ifTrue)
        self.ifFalse = int(ifFalse)

def getData():
    return [x.strip() for x in open('input.txt').readlines()]

def parseData(lines):
    data = []

    numMonkeys = len(lines) // LINES_PER_MONKEY
    groups = np.array_split(lines, numMonkeys)

    for g in groups:
        items = [x for x in g[1].replace(',', '').split() if x.strip().isdigit()]
        op = g[2].split('=')[1]
        test = g[3].split()[3]
        ifTrue = g[4].split()[5]
        ifFalse = g[5].split()[5]

        data.append(Monkey(items, op, test, ifTrue, ifFalse))

    return data

def process(monkeys, divisor):
    for m in monkeys:
       for i in range(len(m.items)):
           old = m.items.popleft()
           new = m.op(int(old)) // divisor
           m.numInspected = m.numInspected + 1
           if(m.testLambda(new)):
               monkeys[m.ifTrue].items.append(new)
           else:
               monkeys[m.ifFalse].items.append(new)

def process2(monkeys, mod):
    for m in monkeys:
       for i in range(len(m.items)):
           old = m.items.popleft()
           new = m.op(int(old)) % mod
           m.numInspected = m.numInspected + 1
           if(m.testLambda(new)):
               monkeys[m.ifTrue].items.append(new)
           else:
               monkeys[m.ifFalse].items.append(new)

def solve1(d, rounds):
    data = copy.deepcopy(d)

    for _ in range(rounds):
        process(data, 3)

    numInspected = [x.numInspected for x in data]
    numInspected.sort(reverse=True)

    return numInspected[0] * numInspected[1]

def solve2(d, rounds):
    data = copy.deepcopy(d)

    #Multiply all test values together to find minimum modulo value
    mod = 1
    for d in data:
        mod = mod * d.testValue

    for x in range(rounds):
        process2(data, mod)
        if x is 0:
            print("Monkey 0 has " + str(data[0].numInspected))


    numInspected = [x.numInspected for x in data]
    numInspected.sort(reverse=True)

    return numInspected[0] * numInspected[1]

if __name__ == "__main__":
    data = parseData(getData())
    print(''.join(["The solution to Part One is ", str(solve1(data, 20))]))
    print(''.join(["The solution to Part Two is ", str(solve2(data, 10000))]))