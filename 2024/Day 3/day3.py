'''
Advent of Code: Day 3
'''
import re   # https://www.geeksforgeeks.org/pattern-matching-python-regex/
all_lines = []

with open('2024/Day 3/data.txt', 'r') as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)

def part1():
    global all_lines
    line_no = 0

    valid_instructions = []
    mul_regex = re.compile("mul\((\d){1,3}\,(\d){1,3}\)")

    while line_no != len(all_lines):
        line = str(all_lines[line_no])

        while (mul_regex.search(line) != None):
            valid_instructions.append(mul_regex.search(line).group())
            line = line[line.find(mul_regex.search(line).group()) + len(mul_regex.search(line).group()):]

        line_no += 1

    total = 0
    for instruction in valid_instructions:
        instruction = f"{instruction.split(')')[0]})"

        num1 = int(instruction.split(",")[0].split("(")[-1])
        num2 = int(instruction.split(",")[-1].split(")")[0])
        total += num1 * num2

    return total

def part2():
    global all_lines
    line_no = 0

    valid_instructions = []
    mul_regex = re.compile("mul\((\d){1,3}\,(\d){1,3}\)|don\'t\(\)|do\(\)")

    while line_no != len(all_lines):
        line = str(all_lines[line_no])

        while (mul_regex.search(line) != None):
            valid_instructions.append(mul_regex.search(line).group())
            line = line[line.find(mul_regex.search(line).group()) + len(mul_regex.search(line).group()):]

        line_no += 1

    total = 0
    allow = True
    for instruction in valid_instructions:
        if "don't" in instruction:
            allow = False
        elif "do" in instruction:
            allow = True
        elif allow:
            instruction = f"{instruction.split(')')[0]})"

            num1 = int(instruction.split(",")[0].split("(")[-1])
            num2 = int(instruction.split(",")[-1].split(")")[0])
            total += num1 * num2

    return total

print('Part 1 answer:', part1())
print('Part 2 answer:', part2())
