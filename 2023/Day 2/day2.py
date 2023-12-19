"""
Advent of Code: Day 2
"""
all_lines = []

with open('2023/Day 2/data.txt', 'r') as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)

def part1():
    global all_lines
    line_no = 0
    max_red = 12
    max_green = 13
    max_blue = 14

    valid_ids = []
    while line_no != len(all_lines):
        end = False
        line = all_lines[line_no]
        line = line.split(": ")

        game_id = int(line[0].split(" ")[-1])
        game = line[1]

        rounds = game.split("; ")
        for round in rounds:
            cubes = round.split(", ")
            for cube in cubes:
                num = int(cube.split(" ")[0])
                if "green" in cube:
                    if num > max_green:
                        end = True
                elif "red" in cube:
                    if num > max_red:
                        end = True
                elif "blue" in cube:
                    if num > max_blue:
                        end = True

        if not end:
            valid_ids.append(game_id)

        line_no += 1

    print(sum(valid_ids))

def part2():
    global all_lines
    line_no = 0

    powers = []
    while line_no != len(all_lines):
        line = all_lines[line_no]
        line = line.split(": ")

        min_red = 0
        min_green = 0
        min_blue = 0

        rounds = line[1].split("; ")
        for round in rounds:
            cubes = round.split(", ")
            for cube in cubes:
                num = int(cube.split(" ")[0])
                if "green" in cube:
                    if -num < -min_green:
                        min_green = num
                elif "red" in cube:
                    if -num < -min_red:
                        min_red = num
                elif "blue" in cube:
                    if -num < -min_blue:
                        min_blue = num

        powers.append(min_red * min_green * min_blue)

        line_no += 1

    print(sum(powers))

part1()
part2()
