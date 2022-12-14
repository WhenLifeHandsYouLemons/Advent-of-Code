"""
Advent of Code: Day 12
"""

all_lines = []
line_no = 0

with open("2022/Day 12/part2.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)

total = 0
for line in all_lines:
    for letter in line:
        try:
            letter = int(letter)
            total += 1
        except:
            continue

print(total)
