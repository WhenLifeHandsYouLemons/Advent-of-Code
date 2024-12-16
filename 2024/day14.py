'''
Advent of Code: Day 14
'''
from helper_methods import *

all_lines = readfile('2024/data.txt')

def part1():
    global all_lines
    line_no = 0

    robots: list[list[tuple[int, int]]] = []

    while line_no != len(all_lines):
        line = all_lines[line_no]

        line = line.split(" ")
        position = tuple([int(i) for i in line[0].split("=")[-1].split(",")])
        velocity = tuple([int(i) for i in line[1].split("=")[-1].split(",")])

        robots.append([position, velocity])

        line_no += 1

    # Go through each robot and simulate 100 seconds
    quadrants: list[int] = [0, 0, 0, 0]
    seconds = 100
    width = 101
    height = 103

    for robot in robots:
        start_pos = robot[0]
        velocity = robot[1]

        end_pos = ((start_pos[0] + (seconds * velocity[0])) % width, (start_pos[1] + (seconds * velocity[1])) % height)

        if end_pos[0] < math.floor(width / 2) and end_pos[1] < math.floor(height / 2):
            quadrants[0] += 1
        elif end_pos[0] > math.floor(width / 2) and end_pos[1] < math.floor(height / 2):
            quadrants[1] += 1
        elif end_pos[0] > math.floor(width / 2) and end_pos[1] > math.floor(height / 2):
            quadrants[2] += 1
        elif end_pos[0] < math.floor(width / 2) and end_pos[1] > math.floor(height / 2):
            quadrants[3] += 1

    total = 1
    for quad in quadrants:
        total *= quad

    return total

def part2():
    global all_lines
    line_no = 0

    robots: list[list[tuple[int, int]]] = []

    while line_no != len(all_lines):
        line = all_lines[line_no]

        line = line.split(" ")
        position = tuple([int(i) for i in line[0].split("=")[-1].split(",")])
        velocity = tuple([int(i) for i in line[1].split("=")[-1].split(",")])

        robots.append([position, velocity])

        line_no += 1

    # Go through each robot and simulate 100 seconds
    quadrants: list[int] = [0, 0, 0, 0]
    seconds = 10000000
    width = 101
    height = 103
    empty_string = "."

    tiles: list[list[int]] = []

    for second in range(1, seconds + 1):
        tiles = [[empty_string for j in range(width)] for i in range(height)]

        for robot in robots:
            start_pos = robot[0]
            velocity = robot[1]

            end_pos = ((start_pos[0] + (second * velocity[0])) % width, (start_pos[1] + (second * velocity[1])) % height)

            if tiles[end_pos[1]][end_pos[0]] == empty_string:
                tiles[end_pos[1]][end_pos[0]] = 1
            else:
                tiles[end_pos[1]][end_pos[0]] += 1

        # Check that there's a 1 with 8 1's around it
        found = False
        for row in range(1, height-1):
            for col in range(1, width-1):
                if tiles[row-1][col-1] != empty_string and tiles[row-1][col] != empty_string and tiles[row-1][col+1] != empty_string and tiles[row][col-1] != empty_string and tiles[row][col+1] != empty_string and tiles[row+1][col-1] != empty_string and tiles[row+1][col] != empty_string and tiles[row+1][col+1] != empty_string:
                    gridPrint(tiles, join_row=True, newline=True)
                    return second

print('Part 1 answer:', part1())
print('Part 2 answer:', part2())
