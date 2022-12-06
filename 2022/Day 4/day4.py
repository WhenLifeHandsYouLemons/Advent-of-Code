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

    # Check if second pair is inside the first
    if int(second_pair[0]) >= int(first_pair[0]) and int(second_pair[1]) <= int(first_pair[1]):
        duplicates += 1
    # Check if first pair is inside second pair
    elif int(second_pair[0]) <= int(first_pair[0]) and int(second_pair[1]) >= int(first_pair[1]):
        duplicates += 1

    line_no = line_no + 1

print(duplicates)