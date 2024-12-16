'''
Advent of Code: Day 15
'''
from helper_methods import *

all_lines = readfile('2024/data.txt')

def part1():
    global all_lines
    line_no = 0

    moveset: list[str] = []
    grid: list[list[str]] = []
    add_to_grid = True

    while line_no != len(all_lines):
        line = all_lines[line_no]

        if line == "":
            add_to_grid = False
        elif add_to_grid:
            grid.append([i for i in line])
        else:
            for i in line:
                moveset.append(i)

        line_no += 1

    # Find the robot's location
    def findRobot() -> tuple[int, int]:
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "@":
                    return (col, row)

        return (len(grid[0]), len(grid))

    for move in moveset:
        robot = findRobot()
        free_space: tuple[int, int] = (len(grid[0]), len(grid))
        movable = False

        # See which direction it's moving in
        if move == "^":
            for row in range(robot[1], -1, -1):
                if grid[row][robot[0]] == "#":
                    break
                elif grid[row][robot[0]] == ".":
                    movable = True
                    free_space = (robot[0], row)
                    break

            if movable:
                for row in range(free_space[1], robot[1]):
                    grid[row][robot[0]] = grid[row+1][robot[0]]

                grid[robot[1]][robot[0]] = "."
        elif move == ">":
            for col in range(robot[0], len(grid[robot[1]])):
                if grid[robot[1]][col] == "#":
                    break
                elif grid[robot[1]][col] == ".":
                    movable = True
                    free_space = (col, robot[1])
                    break

            if movable:
                grid[robot[1]].insert(robot[0], grid[robot[1]].pop(free_space[0]))
        elif move == "v":
            for row in range(robot[1], len(grid)):
                if grid[row][robot[0]] == "#":
                    break
                elif grid[row][robot[0]] == ".":
                    movable = True
                    free_space = (robot[0], row)
                    break

            if movable:
                for row in range(free_space[1], robot[1], -1):
                    grid[row][robot[0]] = grid[row-1][robot[0]]

                grid[robot[1]][robot[0]] = "."
        elif move == "<":
            for col in range(robot[0], -1, -1):
                if grid[robot[1]][col] == "#":
                    break
                elif grid[robot[1]][col] == ".":
                    movable = True
                    free_space = (col, robot[1])
                    break

            if movable:
                grid[robot[1]].insert(robot[0], grid[robot[1]].pop(free_space[0]))

    total = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == "O":
                total += 100 * row + col

    return total

def part2():
    return ''

print('Part 1 answer:', part1())
print('Part 2 answer:', part2())
