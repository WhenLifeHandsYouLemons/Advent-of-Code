"""
Advent of Code: Day 14
"""

all_groups = []
all_lines_in_current_group = []
line_no = 0
temp = ""



number = 4929712
def denary_to_binary_convert(denary):
    complete = []
    x = denary
    d = 2 **  35
    completed = False
    while completed == False:
        x = x - d
        if x < 0:
            complete.append("1")
            x = x + d
        else:
            complete.append("0")
        d = d / 2
        if d < 1:
            completed = True
    complete = "".join(complete)
    print(f"The number, {number} is {complete} in binary.")

denary_to_binary_convert(number)



with open("C:/Users/2005s/Documents/Visual Studio Code/Advent-of-Code-2020/Day 14/Day 14 Resources.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_groups.append(line)
print(all_groups)

while line_no != len(all_groups):
    mask = ""
    temp = ""
    memory_lines = []

    temp = all_groups[line_no].split("\n")
    all_lines_in_current_group.append(temp[0])
    print(all_lines_in_current_group)

    finished = False
    while finished != True:
        mask = all_lines_in_current_group[0]
        mask = mask.split("=")
        mask = mask[1]
        mask = mask.split(" ")
        mask = mask[1]
        print(mask)

        temp = 1
        while temp != len(all_lines_in_current_group):
            memory_lines.append(all_lines_in_current_group[temp])
            temp = temp + 1
        print(memory_lines)

        current_line = True
        while current_line == True:
            current_line = False

        finished = True

    line_no = line_no + 1
