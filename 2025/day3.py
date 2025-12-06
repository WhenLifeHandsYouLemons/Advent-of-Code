'''
Advent of Code: Day 3
'''
from helper_methods import *

all_lines = readfile('2025/data.txt')
# arrayPrint(all_lines, separate=True)

def part1():
    global all_lines
    line_no = 0

    max_joltage = 0
    total_joltage = 0
    while line_no != len(all_lines):
        line = all_lines[line_no]
        oline = all_lines[line_no]

        joltage_pos = len(line)
        while joltage_pos >= len(oline)-1:
            max_joltage = 0
            for idx, char in enumerate(line):
                if int(char) > max_joltage:
                    max_joltage = int(char)
                    joltage_pos = idx

            if joltage_pos >= len(line)-1:
                line = line[:-1]

        oline = oline[joltage_pos+1:]
        max_joltage_2 = int(oline[0])
        joltage_2_pos = 0
        for idx, char in enumerate(oline):
            if int(char) > max_joltage_2:
                max_joltage_2 = int(char)
                joltage_2_pos = idx

        max_jolt = f"{max_joltage}{max_joltage_2}"
        total_joltage += int(max_jolt)

        line_no += 1

    return total_joltage

def part2():
    global all_lines
    line_no = 0

    while line_no != len(all_lines):
        line = all_lines[line_no]

        line_no += 1

    return ''

print('Part 1 answer:', part1())
print('Part 2 answer:', part2())
