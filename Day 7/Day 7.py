"""
# Advent of Code: Day 7
"""

all_lines = []
current_line = ""
line_no = 0

checked = []
not_checked = []

with open("C:/Users/2005s/Documents/Visual Studio Code/Advent-of-Code-2020/Day 7/Day 7 Resources.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)
print(all_lines)

with open("C:/Users/2005s/Documents/Visual Studio Code/Advent-of-Code-2020/Day 7/not_checked.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        not_checked.append(line)
print(not_checked)

with open("C:/Users/2005s/Documents/Visual Studio Code/Advent-of-Code-2020/Day 7/checked.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        checked.append(line)
print(checked)

spliting = []

print("")
print("----------------------------------------------------------------------------------------------------------------")

continuing = True
while continuing == True:
    if continuing == True:
        line_no = 0
    else:
        line_no = len(all_lines)

    while line_no != len(all_lines):
        current_line = all_lines[line_no]

        try:
            if f"{not_checked[0]} bags contain" in current_line:
                line_no = line_no + 1
            elif f"{not_checked[0]}" in current_line:
                print(f"There is a {not_checked[0]} bag in line {line_no + 1}.")
                print(f"'{all_lines[line_no]}'")
                spliting = all_lines[line_no].split(" ")
                print(f"This is what is spliting {spliting}")
                spliting = spliting[0] + " " + spliting[1]
                print(f"This is what is spliting {spliting}")
                not_checked.append(spliting)
                all_lines.pop(line_no)
            else:
                line_no = line_no + 1
        except IndexError:
            print("")
            print("----------------------------------------------------------------------------------------------------------------")
            print("The program has found no other matches!")
            line_no = len(all_lines)
            continuing = False

    if not_checked != []:
        checked.append(not_checked[0])
    save = "\n".join(checked)
    with open("C:/Users/2005s/Documents/Visual Studio Code/Advent-of-Code-2020/Day 7/checked.txt", "w") as f:
        f.write(save)

    if not_checked != []:
        not_checked.pop(0)
    save = "\n".join(not_checked)
    with open("C:/Users/2005s/Documents/Visual Studio Code/Advent-of-Code-2020/Day 7/not_checked.txt", "w") as f:
        f.write(save)

    save = "\n".join(all_lines)
    with open("C:/Users/2005s/Documents/Visual Studio Code/Advent-of-Code-2020/Day 7/Day 7 Resources.txt", "w") as f:
        f.write(save)

print(f"The number of bag colours that can eventually hold a shiny gold bag is {len(checked)-1}.")
