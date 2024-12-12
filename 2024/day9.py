'''
Advent of Code: Day 9
'''
from helper_methods import *

all_lines = readfile('2024/data.txt')

def part1():
    global all_lines
    line_no = 0

    while line_no != len(all_lines):
        line = all_lines[line_no]

        data = True
        current_num = ""
        current_data_num = 0
        disk = []
        for i in line:
            for j in range(int(i)):
                if data:
                    disk.append(current_data_num)
                else:
                    disk.append(".")

            if i != current_num:
                data = not data
                if data:
                    current_data_num += 1

        space = 0
        while space < len(disk):
            if disk[space] == ".":
                while disk[-1] == ".":
                    disk.pop()
                if space < len(disk) - 1:
                    disk[space] = disk.pop()
                else:
                    space = len(disk)
            space += 1

        arrayPrint(disk)

        # Calculate checksum
        total = 0
        for i in range(len(disk)):
            total += disk[i] * i

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
