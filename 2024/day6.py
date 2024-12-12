'''
Advent of Code: Day 6
'''
from helper_methods import *

all_lines = readfile('2024/data.txt')

def part1():
    global all_lines
    line_no = 0

    grid = []

    while line_no != len(all_lines):
        line = all_lines[line_no]

        grid.append([i for i in line])

        line_no += 1

    def updateGrid(grid: list):
        # Find where the person is currently
        person_pos = (-1, -1)
        direction = ""
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] in "^>v<":
                    person_pos = (j, i)
                    direction = grid[i][j]

        try:
            if direction == "^":
                if person_pos[1]-1 < 0:
                    raise Exception()
                elif grid[person_pos[1]-1][person_pos[0]] == "#":
                    grid[person_pos[1]][person_pos[0]] = ">"
                else:
                    grid[person_pos[1]-1][person_pos[0]] = "^"
                    grid[person_pos[1]][person_pos[0]] = "X"
            elif direction == ">":
                if person_pos[0]+1 >= len(grid[0]):
                    raise Exception()
                elif grid[person_pos[1]][person_pos[0]+1] == "#":
                    grid[person_pos[1]][person_pos[0]] = "v"
                else:
                    grid[person_pos[1]][person_pos[0]+1] = ">"
                    grid[person_pos[1]][person_pos[0]] = "X"
            elif direction == "v":
                if person_pos[1]+1 >= len(grid):
                    raise Exception()
                elif grid[person_pos[1]+1][person_pos[0]] == "#":
                    grid[person_pos[1]][person_pos[0]] = "<"
                else:
                    grid[person_pos[1]+1][person_pos[0]] = "v"
                    grid[person_pos[1]][person_pos[0]] = "X"
            elif direction == "<":
                if person_pos[0]-1 < 0:
                    raise Exception()
                elif grid[person_pos[1]][person_pos[0]-1] == "#":
                    grid[person_pos[1]][person_pos[0]] = "^"
                else:
                    grid[person_pos[1]][person_pos[0]-1] = "<"
                    grid[person_pos[1]][person_pos[0]] = "X"
        except Exception as e:
            grid[person_pos[1]][person_pos[0]] = "X"
            return True

        return False

    # Update the grid
    complete = False
    while not complete:
        complete = updateGrid(grid)

    total = 0
    for i in grid:
        for j in i:
            if j == "X":
                total += 1

    return total

def part2():
    return None

print('Part 1 answer:', part1())
print('Part 2 answer:', part2())
