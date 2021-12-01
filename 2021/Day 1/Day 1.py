"""
Advent of Code: Day 1
"""

all_lines = []
line_no = 0

with open("C:/Users/2005s/Desktop/Advent-of-Code/2021/Day 1/Day 1 Resources.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(int(line))
# print(all_lines)

increased = 0
decreased = 0

while line_no != len(all_lines)-3:

    first_sum = all_lines[line_no] + all_lines[line_no+1] + all_lines[line_no+2]
    second_sum = all_lines[line_no+1] + all_lines[line_no+2] + all_lines[line_no+3]

    if first_sum < second_sum:
        increased = increased + 1
        print(f"{second_sum} has increased from {first_sum}")
    if first_sum > second_sum:
        decreased = decreased + 1
        print(f"{second_sum} has decreased from {first_sum}")

    line_no = line_no + 1

print(f"Increased: {increased}")
print(f"Decreased: {decreased}")
