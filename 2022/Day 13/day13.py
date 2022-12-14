"""
Advent of Code: Day 13
"""

all_lines = []
line_no = 0

with open("2022/Day 13/data.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(int(line))
print(all_lines)

while line_no != len(all_lines):
    
    line_no += 1
