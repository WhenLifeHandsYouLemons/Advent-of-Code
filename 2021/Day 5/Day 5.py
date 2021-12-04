"""
Advent of Code: Day 5
"""

all_lines = []
line_no = 0

with open("C:/Users/2005s/Desktop/Advent-of-Code/2021/Day 5/Day 5 Resources.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(int(line))
print(all_lines)

while line_no != len(all_lines):
    
    line_no = line_no + 1
