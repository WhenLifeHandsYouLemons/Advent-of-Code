"""
Advent of Code: Day 8
"""
import math
import sys
# Set a larger recursion limit for tail recursion
print(f"Old recursion limit: {sys.getrecursionlimit()}")
sys.setrecursionlimit(25000)
print(f"New recursion limit: {sys.getrecursionlimit()}\n")

all_lines = []

with open('2023/Day 8/data.txt', 'r') as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)

def part1():
    global all_lines
    line_no = 2

    class Node():
        def __init__(self, name, left, right) -> None | bool:
            self.name = name
            self.left = left
            self.right = right

        def getLeft(self):
            return getNode(self.left)

        def getRight(self):
            return getNode(self.right)

    nodes = []
    # Returns node for given node name
    def getNode(name: str) -> Node:
        for node in nodes:
            if name == node.name:
                return node
        return False

    directions = [path for path in all_lines[0]]

    # Create graph
    while line_no != len(all_lines):
        line = all_lines[line_no]
        name = line.split(" = ")[0]
        paths = line.split(" = ")[1]
        left = paths.split(", ")[0].split("(")[1]
        right = paths.split(", ")[1].split(")")[0]

        # Create node and set its name and left and right
        # Add it to the list of nodes
        nodes.append(Node(name, left, right))

        line_no += 1

    # Get starting node
    for node in nodes:
        if node.name == "AAA":
            starting_node = node

    # Traverse the graph starting at AAA, counting the total steps we take
    def stepThrough(node, directions, direction_pos, steps_taken):
        # If we ran out of directions, restart
        if direction_pos == len(directions):
            direction_pos = 0

        # If we reached the end
        if node.name == "ZZZ":
            return steps_taken
        # Go left
        elif directions[direction_pos] == "L":
            return stepThrough(node.getLeft(), directions, direction_pos+1, steps_taken+1)
        # Go right
        elif directions[direction_pos] == "R":
            return stepThrough(node.getRight(), directions, direction_pos+1, steps_taken+1)

    total_steps = stepThrough(starting_node, directions, 0, 0)
    print(total_steps)

def part2():
    global all_lines
    line_no = 2

    class Node():
        def __init__(self, name, left, right) -> None | bool:
            self.name = name
            self.left = left
            self.right = right

        def getLeft(self):
            return getNode(self.left)

        def getRight(self):
            return getNode(self.right)

    nodes = []
    # Returns node for given node name
    def getNode(name: str) -> Node:
        for node in nodes:
            if name == node.name:
                return node
        return False

    directions = [path for path in all_lines[0]]

    # Create graph
    while line_no != len(all_lines):
        line = all_lines[line_no]
        name = line.split(" = ")[0]
        paths = line.split(" = ")[1]
        left = paths.split(", ")[0].split("(")[1]
        right = paths.split(", ")[1].split(")")[0]

        # Create node and set its name and left and right
        # Add it to the list of nodes
        nodes.append(Node(name, left, right))

        line_no += 1

    # Get starting node
    starting_nodes = []
    for node in nodes:
        if node.name[2] == "A":
            starting_nodes.append(node)

    # Traverse the graph starting at AAA, counting the total steps we take
    def stepThrough(node, directions, direction_pos, steps_taken):
        # If we ran out of directions, restart
        if direction_pos == len(directions):
            direction_pos = 0

        # If we reached the end
        if node.name[2] == "Z":
            return steps_taken
        # Go left
        elif directions[direction_pos] == "L":
            return stepThrough(node.getLeft(), directions, direction_pos+1, steps_taken+1)
        # Go right
        elif directions[direction_pos] == "R":
            return stepThrough(node.getRight(), directions, direction_pos+1, steps_taken+1)

    # Get the number of steps taken from each starting point
    steps = []
    for start_node in starting_nodes:
        steps.append(stepThrough(start_node, directions, 0, 0))

    # Calculate the LCM of all the step counts as each one can cycle infinitely as needed
    total_lcm = steps[0]
    i = 1
    while i < len(steps):
        total_lcm = math.lcm(total_lcm, steps[i])
        i += 1

    print(total_lcm)

part1()
part2()
