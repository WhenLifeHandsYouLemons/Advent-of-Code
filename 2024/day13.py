'''
Advent of Code: Day 13
'''
from helper_methods import *

all_lines = readfile('2024/data.txt')

def part1():
    global all_lines
    line_no = 0

    games: list[list[str]] = []

    game: list[str] = []
    while line_no != len(all_lines):
        line = all_lines[line_no]

        if line == "":
            games.append(game)
            game = []
        else:
            game.append(line)

        line_no += 1
    games.append(game)

    total_cost = 0
    for game in games:
        button_a = game[0].split(", ")
        button_a = (int(button_a[0].split("+")[-1]), int(button_a[1].split("+")[-1]))

        button_b = game[1].split(", ")
        button_b = (int(button_b[0].split("+")[-1]), int(button_b[1].split("+")[-1]))

        result = game[2].split(", ")
        result = (int(result[0].split("=")[-1]), int(result[1].split("=")[-1]))

        possible_presses: list[tuple[int, int]] = []
        for a in range(101):
            remainder = (result[0] - (button_a[0] * a), result[1] - (button_a[1] * a))
            if float(remainder[0]).is_integer() and float(remainder[1]).is_integer():   # https://stackoverflow.com/a/21583817
                if remainder[0] / button_b[0] == remainder[1] / button_b[1] and float(remainder[0] / button_b[0]).is_integer():
                    possible_presses.append((a, int(remainder[0] / button_b[0])))

        lowest_cost: int = math.inf

        for i in possible_presses:
            lowest_cost = i[0]*3 + i[1]*1

        if lowest_cost != math.inf:
            total_cost += lowest_cost

    return total_cost

def part2():
    global all_lines
    line_no = 0

    games: list[list[str]] = []

    game: list[str] = []
    while line_no != len(all_lines):
        line = all_lines[line_no]

        if line == "":
            games.append(game)
            game = []
        else:
            game.append(line)

        line_no += 1
    games.append(game)

    total_cost = 0
    for game in games:
        button_a = game[0].split(", ")
        button_a = (int(button_a[0].split("+")[-1]), int(button_a[1].split("+")[-1]))

        button_b = game[1].split(", ")
        button_b = (int(button_b[0].split("+")[-1]), int(button_b[1].split("+")[-1]))

        result = game[2].split(", ")
        result = (10000000000000 + int(result[0].split("=")[-1]), 10000000000000 + int(result[1].split("=")[-1]))

        lowest_cost: int = math.inf
        for a in range(10000000000000):
            remainder = (result[0] - (button_a[0] * a), result[1] - (button_a[1] * a))
            if float(remainder[0]).is_integer() and float(remainder[1]).is_integer():   # https://stackoverflow.com/a/21583817
                if remainder[0] / button_b[0] == remainder[1] / button_b[1] and float(remainder[0] / button_b[0]).is_integer():
                    cur_cost = (a * 3) + int(remainder[0] / button_b[0])
                    if cur_cost < lowest_cost:
                        lowest_cost = cur_cost
                    else:
                        break

        if lowest_cost != math.inf:
            total_cost += lowest_cost

    return total_cost

print('Part 1 answer:', part1())
print('Part 2 answer:', part2())
