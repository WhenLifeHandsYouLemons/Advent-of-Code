"""
Advent of Code: Day 4
"""

all_lines = []

with open('2023/Day 4/data.txt', 'r') as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)
# print(all_lines)

def part1():
    global all_lines
    line_no = 0
    points = []
    while line_no != len(all_lines):
        line = all_lines[line_no]

        line = line.split(": ")[-1].split(" | ")

        winning_numbers = line[0].split(" ")
        card_numbers = line[1].split(" ")

        winning_numbers = [num for num in winning_numbers if num != ""]
        card_numbers = [num for num in card_numbers if num != ""]

        total_points_to_add = 0
        for card_num in card_numbers:
            if card_num in winning_numbers:
                if total_points_to_add == 0:
                    total_points_to_add = 1
                else:
                    total_points_to_add *= 2

        points.append(int(total_points_to_add))

        line_no += 1

    print(sum(points))

def part2():
    global all_lines
    line_no = 0

    all_copies = [[] for i in all_lines]

    while line_no != len(all_lines):
        if all_copies[card_number] == []:
            line = all_lines[line_no]

            line = line.split(": ")
            card_number = int(line[0].split(" ")[-1]) - 1
            line = line[-1].split(" | ")

            winning_numbers = line[0].split(" ")
            card_numbers = line[1].split(" ")

            winning_numbers = [num for num in winning_numbers if num != ""]
            card_numbers = [num for num in card_numbers if num != ""]

            matching_nums = 0
            for card_num in card_numbers:
                if card_num in winning_numbers:
                    matching_nums += 1

            for i in range(matching_nums):
                all_lines.append(card_number+i)

        line_no += 1

    print(len(all_lines))

# part1()
part2()
