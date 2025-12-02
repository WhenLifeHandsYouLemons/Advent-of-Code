'''
Advent of Code: Day 1
'''
from helper_methods import *

all_lines = readfile('2025/data.txt')
# arrayPrint(all_lines, separate=True)

def part1():
    global all_lines
    line_no = 0

    value = 50
    total_zeros = 0
    while line_no != len(all_lines):
        line = all_lines[line_no]

        direction = -1 if line[0] == "L" else 1

        if direction == 1:
            value += int(line[1:])
            value %= 100
        else:
            value -= int(line[1:])
            value %= 100

        if value == 0:
            total_zeros += 1

        line_no += 1

    return total_zeros

def part2():
    global all_lines
    line_no = 0

    value = 50
    total_zeros = 0
    while line_no != len(all_lines):
        line = all_lines[line_no]

        direction = -1 if line[0] == "L" else 1

        if direction == 1:
            value += int(line[1:])
            while value > 99:
                value -= 100
                total_zeros += 1
        else:
            value -= int(line[1:])
            while value < 0:
                value += 100
                total_zeros += 1

        line_no += 1

    return total_zeros

print('Part 1 answer:', part1())
print('Part 2 answer:', part2())
