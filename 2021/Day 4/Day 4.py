"""
Advent of Code: Day 4
"""

all_lines = []
line_no = 0

with open("2021/Day 4/Day 4 Resources.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(int(line))
print(all_lines)

while line_no != len(all_lines):
    
    line_no = line_no + 1