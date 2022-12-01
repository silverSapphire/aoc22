#!/usr/bin/env python3
import itertools as it

if __name__ == "__main__":
    print(''.join(["Part One: ", str(max([sum(i) for i in [list(i) for match, i in it.groupby([int(x.strip()) if x.strip().isdigit() else None for x in\
        open('input.txt').readlines()], lambda p: p != None) if match]])), "\nPart Two: ", str(sum(sorted([sum(i) for i in [list(i) for match, i in\
            it.groupby([int(x.strip()) if x.strip().isdigit() else None for x in open('input.txt').readlines()], lambda p: p != None) if match]], reverse=True)[:3]))]))