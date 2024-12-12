"""
Advent of Code: Day 1
"""

all_lines = []
line_no = 0

with open("2021/Day 1/Day 1 Resources.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(int(line))

increased = 0
decreased = 0

# while line_no != len(all_lines)-1:
while line_no != len(all_lines)-3:

    first_sum = all_lines[line_no] + all_lines[line_no+1] + all_lines[line_no+2]
    second_sum = all_lines[line_no+1] + all_lines[line_no+2] + all_lines[line_no+3]

    # if all_lines[line_no] < all_lines[line_no+1]:
    if first_sum < second_sum:
        increased = increased + 1
        print(f"{second_sum} has increased from {first_sum}")
        # print(f"{all_lines[line_no+1]} has increased from {all_lines[line_no]}")
    # elif all_lines[line_no] > all_lines[line_no+1]:
    elif first_sum > second_sum:
        decreased = decreased + 1
        print(f"{second_sum} has decreased from {first_sum}")
        # print(f"{all_lines[line_no+1]} has decreased from {all_lines[line_no]}")

    line_no = line_no + 1

print(f"Increased: {increased}")
print(f"Decreased: {decreased}")
