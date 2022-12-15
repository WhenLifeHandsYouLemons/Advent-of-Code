"""
Advent of Code: Day 13
"""

all_lines = []
line_no = 0

with open("2022/Day 13/data.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)

while line_no <= len(all_lines)-2:
    pair1 = eval(all_lines[line_no])
    pair2 = eval(all_lines[line_no+1])
    print(pair1, pair2)
    line_no += 3
