"""
Advent of Code: Day 2
"""

all_lines = []
line_no = 0

with open("C:/Users/2005s/Desktop/Advent-of-Code/2021/Day 2/Day 2 Resources.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)
print(all_lines)

horizontal = 0
depth = 0

while line_no != len(all_lines):
    current_line = all_lines[line_no].split(" ")
    current_command = current_line[0]
    current_units = int(current_line[1])
    if current_command == "forward":
        horizontal = horizontal + current_units
    elif current_command == "down":
        depth = depth + current_units
    elif current_command == "up":
        depth = depth - current_units
    line_no = line_no + 1

print(horizontal)
print(depth)
print(horizontal * depth)