'''
Advent of Code: Day 10
'''
from helper_methods import *

all_lines = readfile('2024/data.txt')

class Node():pass

class TrailNode(Node):
    def __init__(self, x: int, y: int, height: int, total_neighbours: int = 4):
        self.pos: tuple = (x, y)
        self.height: int = height
        if height == 9:
            self.reached: bool = False

        self.trailhead: bool = self.height == 0

        # 0: up, 1: right, 2: down, 3: left
        self.neighbours: list[TrailNode] = [None for i in range(total_neighbours)]

    def isTrailHead(self) -> bool:
        return self.trailhead

    def isTrailTail(self) -> bool:
        return self.height == 9

    def addNeighbours(self, neighbour: Node, direction: int) -> None:
        self.neighbours[direction] = neighbour

    def findPathsPart1(self) -> int:
        if self.height == 9 and not self.reached:
            self.reached = True
            return 1

        total_valid_paths = 0

        for i in self.neighbours:
            if i != None and self.height + 1 == i.height:
                total_valid_paths += i.findPathsPart1()

        return total_valid_paths

    def findPathsPart2(self) -> int:
        if self.height == 9:
            return 1

        total_valid_paths = 0

        for i in self.neighbours:
            if i != None and self.height + 1 == i.height:
                total_valid_paths += i.findPathsPart2()

        return total_valid_paths

    def __str__(self) -> str:
        return str(self.height)

def part1():
    global all_lines
    line_no = 0

    grid: list[list[TrailNode]] = []

    while line_no != len(all_lines):
        line = all_lines[line_no]

        grid.append([TrailNode(x, line_no, int(line[x])) for x in range(len(line))])

        line_no += 1

    # Add neighbours to all TrailNodes and get trailheads
    trailheads: list[TrailNode] = []
    trailtails: list[TrailNode] = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if x != 0:
                grid[y][x].addNeighbours(grid[y][x - 1], 3)
            if x != len(grid[y]) - 1:
                grid[y][x].addNeighbours(grid[y][x + 1], 1)

            if y != 0:
                grid[y][x].addNeighbours(grid[y - 1][x], 0)
            if y != len(grid) - 1:
                grid[y][x].addNeighbours(grid[y + 1][x], 2)

            if grid[y][x].isTrailHead():
                trailheads.append(grid[y][x])
            elif grid[y][x].isTrailTail():
                trailtails.append(grid[y][x])

    # Go through each trailhead and run the find paths function
    total = 0
    for trailhead in trailheads:
        total += trailhead.findPathsPart1()
        for trailtail in trailtails:
            trailtail.reached = False

    return total

def part2():
    global all_lines
    line_no = 0

    grid: list[list[TrailNode]] = []

    while line_no != len(all_lines):
        line = all_lines[line_no]

        grid.append([TrailNode(x, line_no, int(line[x])) for x in range(len(line))])

        line_no += 1

    # Add neighbours to all TrailNodes and get trailheads
    trailheads: list[TrailNode] = []
    trailtails: list[TrailNode] = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if x != 0:
                grid[y][x].addNeighbours(grid[y][x - 1], 3)
            if x != len(grid[y]) - 1:
                grid[y][x].addNeighbours(grid[y][x + 1], 1)

            if y != 0:
                grid[y][x].addNeighbours(grid[y - 1][x], 0)
            if y != len(grid) - 1:
                grid[y][x].addNeighbours(grid[y + 1][x], 2)

            if grid[y][x].isTrailHead():
                trailheads.append(grid[y][x])
            elif grid[y][x].isTrailTail():
                trailtails.append(grid[y][x])

    # Go through each trailhead and run the find paths function
    total = 0
    for trailhead in trailheads:
        total += trailhead.findPathsPart2()

    return total

print('Part 1 answer:', part1())
print('Part 2 answer:', part2())
