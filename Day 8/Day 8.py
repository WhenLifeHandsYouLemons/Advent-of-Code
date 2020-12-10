"""
# Advent of Code: Day 8
"""

all_lines = []
current_line = ""
current_command = ""
current_number = 0
line_no = 0
accumulator = 0
finished_lines = []

with open("C:/Users/2005s/Documents/Visual Studio Code/Advent-of-Code-2020/Day 8/Day 8 Resources.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)
print(all_lines)

changing = 1
while line_no < len(all_lines):
    changed = 0
    line_no = 0
    finished = False
    accumulator = 0
    finished_lines = []
    while finished == False:
        finished_lines.append(line_no)
        current_line = all_lines[line_no]
        current_line = current_line.split(" ")
        current_command = current_line[0]
        current_number = int(current_line[1])
        if "nop" in current_command:
            line_no = line_no + 1
            if changed == changing:
                line_no = line_no - 1
                line_no = line_no + current_number
                print(f"Changed line {line_no} from nop to jmp")
        elif "acc" in current_command:
            accumulator = accumulator + current_number
            line_no = line_no + 1
        elif "jmp" in current_command:
            line_no = line_no + current_number
            if changed == changing:
                line_no = line_no - current_number
                line_no = line_no + 1
                print(f"Changed line {line_no} from jmp to nop")
        if line_no in finished_lines:
            finished = True
        if line_no >= len(all_lines):
            finished = True
        changed = changed + 1
        print(line_no)
    changing = changing + 1

print(f"The accumulator accumulated a total of {accumulator}, and the line it was on was {line_no}")
