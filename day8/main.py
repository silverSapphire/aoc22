#!/usr/bin/env python3
import numpy as np

def getData():
    return [x.strip() for x in open('input.txt').readlines()]

def parseData(lines):

    heights = []
    for line in lines:
        for x in line:
            heights.append(int(x))
            
    return np.array(heights).reshape((len(lines[0]), len(lines)))

def solve1(data):
    (width, height) = data.shape
    nvisible = 2 * width + height * 2 - 4

    for i in range(1, width-1):
        for j in range(1, height-1):
            tree = data[i, j]
            left = [tree > x for x in data[i, :j]]
            right = [tree > x for x in data[i, j+1:]]
            up = [tree > x for x in data[:i, j]]
            down = [tree > x for x in data[i+1:, j]]

            isVisible = sum(left) == len(left) or sum(right) == len(right) or sum(up) == len(up) or sum(down) == len(down)
            if isVisible: nvisible = nvisible + 1

    return nvisible

def solve2(data):
    (width, height) = data.shape

    scores = []
    for i in range(1, width-1):
        for j in range(1, height-1):
            tree = data[i][j]

            # Look left
            nleft = 0
            k = j-1
            while k >= 0:
                if data[i, k] < tree: 
                    nleft = nleft + 1
                if data[i, k] >= tree:
                    nleft = nleft + 1
                    break
                k = k - 1
            # Look right
            nright = 0
            k = j+1
            while k < width :
                if data[i, k] < tree: 
                    nright = nright + 1
                if data[i, k] >= tree:
                    nright = nright + 1
                    break
                k = k + 1
            # Look up
            nup = 0
            k = i-1
            while k >= 0:
                if data[k, j] < tree: 
                    nup = nup + 1
                if data[k, j] >= tree:
                    nup = nup + 1
                    break
                k = k - 1
            if k < 0: k = k + 1
            # Look down
            ndown = 0
            k = i+1
            while k < height:
                if data[k, j] < tree: 
                    ndown = ndown + 1
                if data[k, j] >= tree:
                    ndown = ndown + 1
                    break
                k = k + 1
            if k == height: k = k + 1
            
            scores.append(nleft * nright * nup * ndown)

    return max(scores)

if __name__ == "__main__":
    data = parseData(getData())
    print(''.join(["The solution to Part One is ", str(solve1(data))]))
    print(''.join(["The solution to Part One is ", str(solve2(data))]))