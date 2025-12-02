'''
Advent of Code: Day 2
'''
from helper_methods import *

all_lines = readfile('2025/data.txt')
# arrayPrint(all_lines, separate=True)

def part1():
    global all_lines
    line_no = 0

    valid = 0
    invalid = 0
    total = 0
    while line_no != len(all_lines):
        line = all_lines[line_no]

        ranges = line.split(",")

        for range_val in ranges:
            start, stop = range_val.split("-")
            for val in range(int(start), int(stop)+1, 1):
                sval = str(val)
                if len(sval) % 2 == 0:
                    if sval[:int(len(sval)/2)] != sval[int(len(sval)/2):]:
                        valid += 1
                    else:
                        invalid += 1
                        total += val

        line_no += 1

    return total

def part2():
    global all_lines
    line_no = 0

    while line_no != len(all_lines):
        line = all_lines[line_no]

        line_no += 1

    return ''

print('Part 1 answer:', part1())
print('Part 2 answer:', part2())
