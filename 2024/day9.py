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

        data = True
        current_data_num = 0
        disk: list[list[str]] = []
        for i in line:
            if data:
                disk.append([str(current_data_num) for i in range(int(i))])
            else:
                disk.append(["." for i in range(int(i))])

            data = not data
            if data:
                current_data_num += 1

        for data in range(len(disk) - 1, -1, -1):
            if "." not in disk[data]:
                # Find empty space on the left of the current data space
                left_of_data = disk[:data]

                for empty_space in range(len(left_of_data)):
                    if len(left_of_data[empty_space]) >= len(disk[data]) and "." in disk[empty_space]:
                        disk[empty_space] = ["." for i in range(len(disk[empty_space]) - len(disk[data]))]

                        disk.insert(empty_space, disk[data].copy())
                        disk[data + 1] = ["." for i in range(len(disk[data + 1]))]

                        if disk[empty_space] == []:
                            disk.pop(empty_space)
                        break

        # Calculate checksum
        total = 0
        i = 0
        for partition in disk:
            for data in partition:
                if data != ".":
                    total += int(data) * i
                i += 1

        line_no += 1

    return total

print('Part 1 answer:', part1())
print('Part 2 answer:', part2())
