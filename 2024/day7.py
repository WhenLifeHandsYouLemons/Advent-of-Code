'''
Advent of Code: Day 7
'''
from helper_methods import *

all_lines = readfile('2024/data.txt')

def increasePossibility(possibility: list[int], max: int) -> list[int]:
    for i in range(len(possibility)-1, -1, -1):
        if possibility[i] == max:
            possibility[i] = 0
        else:
            possibility[i] += 1
            break

    return possibility

def part1():
    global all_lines
    line_no = 0

    valid_calculations = []

    while line_no != len(all_lines):
        line = all_lines[line_no]

        line = line.split(": ")

        required_result = int(line[0])
        numbers = [int(i) for i in line[1].split(" ")]

        possibilities = [["+", "*"] for i in range(len(numbers)-1)]
        current_posibility = [0 for i in range(len(possibilities))]

        completed = False
        while not completed:
            result = numbers[0]
            for i in range(1, len(numbers)):
                if possibilities[i-1][current_posibility[i-1]] == "+":
                    result += numbers[i]
                else:
                    result *= numbers[i]

            if result == required_result:
                valid_calculations.append(required_result)
                completed = True

            current_posibility = increasePossibility(current_posibility, 1)
            if 1 not in current_posibility:
                completed = True

        line_no += 1

    total = 0
    for i in valid_calculations:
        total += i

    return total

def part2():
    global all_lines
    line_no = 0

    valid_calculations = []

    while line_no != len(all_lines):
        line = all_lines[line_no]

        line = line.split(": ")

        required_result = int(line[0])
        numbers = [int(i) for i in line[1].split(" ")]

        possibilities = [["+", "*", "||"] for i in range(len(numbers)-1)]
        current_posibility = [0 for i in range(len(possibilities))]

        completed = False
        can_remove = False
        while not completed:
            result = numbers[0]
            for i in range(1, len(numbers)):
                if possibilities[i-1][current_posibility[i-1]] == "+":
                    result += numbers[i]
                elif possibilities[i-1][current_posibility[i-1]] == "*":
                    result *= numbers[i]
                else:
                    result = int(f"{str(result)}{str(numbers[i])}")

            if result == required_result:
                valid_calculations.append(required_result)
                can_remove = True
                completed = True

            current_posibility = increasePossibility(current_posibility, 1)
            if 1 not in current_posibility:
                completed = True

        if can_remove:
            all_lines.pop(line_no)
        else:
            line_no += 1

    print("Completed part 1")

    line_no = 0
    while line_no != len(all_lines):
        line = all_lines[line_no]

        line = line.split(": ")

        required_result = int(line[0])
        numbers = [int(i) for i in line[1].split(" ")]

        possibilities = [["+", "*", "||"] for i in range(len(numbers)-1)]
        current_posibility = [0 for i in range(len(possibilities))]

        completed = False
        while not completed:
            result = numbers[0]
            for i in range(1, len(numbers)):
                if possibilities[i-1][current_posibility[i-1]] == "+":
                    result += numbers[i]
                elif possibilities[i-1][current_posibility[i-1]] == "*":
                    result *= numbers[i]
                else:
                    result = int(f"{str(result)}{str(numbers[i])}")

            if result == required_result:
                valid_calculations.append(required_result)
                completed = True

            current_posibility = increasePossibility(current_posibility, 2)
            if 1 not in current_posibility and 2 not in current_posibility:
                completed = True

        line_no += 1

    total = 0
    for i in valid_calculations:
        total += i

    return total

print('Part 1 answer:', part1())
print('Part 2 answer:', part2())
