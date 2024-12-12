'''
Advent of Code: Day 1
'''
all_lines = []

with open('2024/Day 1/data.txt', 'r') as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)

def part1():
    global all_lines
    line_no = 0

    left_list = []
    right_list = []

    while line_no != len(all_lines):
        line = all_lines[line_no]

        line_split = line.split("   ")
        left_list.append(int(line_split[0]))
        right_list.append(int(line_split[-1]))

        line_no += 1

    left_list.sort()
    right_list.sort()

    distances = []
    for i in range(len(left_list)):
        distances.append(abs(left_list[i] - right_list[i]))

    total = sum(distances)

    return total

def part2():
    global all_lines
    line_no = 0

    left_list = []
    right_list = []

    while line_no != len(all_lines):
        line = all_lines[line_no]

        line_split = line.split("   ")
        left_list.append(int(line_split[0]))
        right_list.append(int(line_split[-1]))

        line_no += 1

    similarities = []
    for i in range(len(left_list)):
        similarities.append(left_list[i] * right_list.count(left_list[i]))

    total = sum(similarities)

    return total

print("Part 1 answer:", part1())
print("Part 2 answer:", part2())
