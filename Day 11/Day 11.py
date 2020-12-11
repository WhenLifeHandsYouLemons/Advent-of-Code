"""
Advent of Code: Day 11
"""

all_lines = []
line_no = 0

with open("C:/Users/2005s/Documents/Visual Studio Code/Advent-of-Code-2020/Day 11/Day 11 Resources.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)
print(all_lines)


while line_no != len(all_lines):
    line_no = line_no + 1
