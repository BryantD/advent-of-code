#!/usr/bin/env python3


class TreeNode:
    def __init__(self, name, type, size, parent):
        self.name = name
        self.type = type
        self.size = size
        self.parent = parent
        self.contents = []

    def add_node(self, node):
        if node.name not in self.contents:
            self.contents.append(node)
            if node.type == "file":
                self.resize_node(node.size)

    def resize_node(self, size):
        self.size += size
        if self.parent:
            self.parent.resize_node(size)

    def print_tree(self, depth):
        print(f"{'  '*depth}{self.name} ({self.size})")
        for node in self.contents:
            node.print_tree(depth + 1)


def scan_tree1(node):
    total_size = 0
    
    if node.size <= 100000:
        total_size += node.size
    for subnode in node.contents:
        if subnode.type == "dir":
            total_size += scan_tree1(subnode)
            
    return total_size


def scan_tree2(node, goal, current_best):    
    if node.type == "dir" and node.size >= goal and node.size < current_best:
        current_best = node.size
    for subnode in node.contents:
        if subnode.type == "dir":
            current_best = scan_tree2(subnode, goal, current_best)
                
    return current_best


def part1(data):
    total_score = 0
    top_node = TreeNode("/", "dir", 0, None)
    for line in data:
        if line[0:4] == "$ cd":
            directory = line[5:]
            if directory == "/":
                current_node = top_node
            elif directory == "..":
                current_node = current_node.parent
            else:
                new_node = TreeNode(directory, "dir", 0, current_node)
                current_node.add_node(new_node)
                current_node = new_node
        elif line[0].isdigit():
            (size, name) = line.split()
            size = int(size)
            new_node = TreeNode(name, "file", size, current_node)
            current_node.add_node(new_node)
        elif line[0:4] == "$ ls":
            ...
        elif line[0:4] == "dir ":
            ...
        else:
            ...

    total_score = scan_tree1(top_node)
    return top_node, total_score


def part2(top_node):
    total_space = 70000000
    used_space = top_node.size
    needed_space = 30000000
    
    required_space = used_space - (total_space - needed_space)
    
    if required_space <= 0:
        return 0
        
    total_score = scan_tree2(top_node, required_space, total_space)

    return total_score


def main():
    with open("data.txt") as data_file:
        data_string = data_file.read()
    data_lines = data_string.splitlines()
    top_node, solution1 = part1(data_lines)
    print(solution1)

    print()

    solution2 = part2(top_node)
    print(solution2)


if __name__ == "__main__":
    main()
