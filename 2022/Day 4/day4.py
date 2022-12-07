"""
Advent of Code: Day 4
"""

all_lines = []
line_no = 0

with open("2022/Day 4/data.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)

duplicates = 0
while line_no != len(all_lines):
    pairs = all_lines[line_no].split(",")
    first_pair = pairs[0].split("-")
    second_pair = pairs[1].split("-")
    first_array = []
    second_array = []

    for i in range(int(first_pair[0]), int(first_pair[1])+1):
        first_array.append(i)

    for i in range(int(second_pair[0]), int(second_pair[1])+1):
        second_array.append(i)

    for i in first_array:
        if i in second_array:
            duplicates += 1
            break

    line_no = line_no + 1

print(duplicates)