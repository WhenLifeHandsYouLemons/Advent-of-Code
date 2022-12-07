"""
Advent of Code: Day 5
"""

all_lines = []
line_no = 0

with open("2022/Day 5/data.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)

all_stacks = [["Z", "T", "F", "R", "W", "J", "G"], ["G", "W", "M"], ["J", "N", "H", "G"], ["J", "R", "C", "N", "W"], ["W", "F", "S", "B", "G", "Q", "V", "M"], ["S", "R", "T", "D", "V", "W", "C"], ["H", "B", "N", "C", "D", "Z", "G", "V"], ["S", "J", "N", "M", "G", "C"], ["G", "P", "N", "W", "C", "J", "D", "L"]]

# Get the instructions
instructions = []
started = False
for i in all_lines:
    if started is True:
        instructions.append(i)
    if i == "":
        started = True

while line_no != len(instructions):
    split_instructions = instructions[line_no].split(" ")
    number_of_boxes = int(split_instructions[1])
    starting_stack = int(split_instructions[3]) - 1
    final_stack = int(split_instructions[5]) - 1

    temp_array = []
    for i in range(number_of_boxes):
        temp_array.append(all_stacks[starting_stack].pop())

    for i in range(number_of_boxes):
        all_stacks[final_stack].append(temp_array.pop())

    line_no = line_no + 1

all_letters = []
for i in all_stacks:
    all_letters.append(i[-1])

print("".join(all_letters))