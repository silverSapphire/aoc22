#!/usr/bin/env python3
class Node:
    def __init__(self, name):
        self.name = name
        self.size = 0
        self.parent = None
        self.children = []

    def add_child(self, node):
        node.parent = self
        self.children.append(node)
        self.add_size(node.size)

    def add_size(self, size):
        self.size = self.size + size
        if self.parent: self.parent.add_size(size)

    def find(self, x):
        queue = [self]
        visited = [self]

        while queue:
            node = queue.pop(0)
            if node.name == x: return node
            for child in node.children:
                if child not in visited:
                    visited.append(child)
                    queue.append(child)

    def find_all_less_equal(self, thresh, list):
        if self.size <= thresh: list.append(self)
        for node in self.children:
            node.find_all_less_equal(thresh, list)

    def find_all_greater_equal(self, thresh, list):
        if self.size >= thresh: list.append(self)
        for node in self.children:
            node.find_all_greater_equal(thresh, list)

def getData():
    return [x for x in open('input.txt').readlines()]

def parseData(lines):
    lines = [x.replace("$", "").replace("ls", "").strip() for x in lines]
    cmds = [x.split() for x in lines if x]

    root = Node("/")
    current = root
    for c in cmds[1:]:
        if c[0] == "cd":
            if c[1] == "..": current = current.parent
            else: current = current.find(c[1])
        elif c[0] == "dir":
            n = current.find(c[1])
            if not n: 
                n = Node(c[1])
                current.add_child(n)
        else:
            current.add_size(int(c[0]))

    return root

def solve1(root):
    littleNodes = []
    root.find_all_less_equal(100000, littleNodes)
    return sum([x.size for x in littleNodes])

def solve2(root):
    remaining = 70000000 - root.size
    required = 30000000 - remaining
    rightNodes = []
    root.find_all_greater_equal(required, rightNodes)
    return min([x.size for x in rightNodes])

if __name__ == "__main__":
    root = parseData(getData())
    print(''.join(["The solution to Part One is ", str(solve1(root))]))
    print(''.join(["The solution to Part Two is ", str(solve2(root))]))