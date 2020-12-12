"""
Advent of Code: Day 11
"""

all_lines = []
changed_all_lines = []
current_line = ""
below_line = ""
above_line = ""
current_have = 0
min_needed = 4
seperated_current_line = []
seperated_below_line = []
seperated_above_line = []
line_no = 0

with open("C:/Users/2005s/Documents/Visual Studio Code/Advent-of-Code-2020/Day 11/Day 11 Resources.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)
print(all_lines)

row = len(all_lines[0])
column = len(all_lines)

while line_no != column:
    seperated_current_line = []
    current_line = all_lines[line_no]

    if line_no != 0:
        above_line = all_lines[line_no-1]
        for space in above_line:
            seperated_above_line.append(space)

    if line_no != row-1:
        print("Below line has changed!")
        below_line = all_lines[line_no+1]

        for space in below_line:
            seperated_below_line.append(space)

    print(current_line)

    for space in current_line:
        seperated_current_line.append(space)
    print(seperated_current_line)

    lining = 0
    while lining != row:
        # If it's a floor
        if seperated_current_line[lining] == ".":
            pass
        # If it's an empty seat
        elif seperated_current_line[lining] == "L":
            # If it's the first row
            if above_line == "":
                # If it's the first column
                if lining == 0:
                    # If the right is empty
                    if seperated_current_line[lining+1] == "L" or seperated_current_line[lining+1] == ".":
                        # If the bottom is empty
                        if seperated_below_line[lining] == "L" or seperated_below_line[lining] == ".":
                            # If the bottom-right is empty
                            if seperated_below_line[lining+1] == "L" or seperated_below_line[lining+1] == ".":
                                seperated_current_line.pop(lining)
                                seperated_current_line.insert(lining, "#")
                                print("The top left is changed!")
                # If it's the last column
                if lining == row-1:
                    # If the left is empty
                    if seperated_current_line[lining-1] == "L" or seperated_current_line[lining-1] == ".":
                        # If the bottom is empty
                        if seperated_below_line[lining] == "L" or seperated_below_line[lining] == ".":
                            # If the bottom-left is empty
                            if seperated_below_line[lining-1] == "L" or seperated_below_line[lining-1] == ".":
                                seperated_current_line.pop(lining)
                                seperated_current_line.insert(lining, "#")
                                print("The top right has changed!")
            # If it's the last row
            if below_line == "":
                print("It's the last line")
                # If it's the first column
                if lining == 0:
                    # If the right is empty
                    if seperated_current_line[lining+1] == "L" or seperated_current_line[lining+1] == ".":
                        # If the above is empty
                        if seperated_above_line[lining] == "L" or seperated_above_line[lining] == ".":
                            # If the above-right is empty
                            if seperated_above_line[lining+1] == "L" or seperated_above_line[lining+1] == ".":
                                seperated_current_line.pop(lining)
                                seperated_current_line.insert(lining, "#")
                                print("The bottom left has changed!")
                # If it's the last column
                if lining == row-1:
                    # If the left is empty
                    if seperated_current_line[lining-1] == "L" or seperated_current_line[lining-1] == ".":
                        # If the above is empty
                        if seperated_above_line[lining] == "L" or seperated_above_line[lining] == ".":
                            # If the above-left is empty
                            if seperated_above_line[lining-1] == "L" or seperated_above_line[lining-1] == ".":
                                seperated_current_line.pop(lining)
                                seperated_current_line.insert(lining, "#")
                                print("The bottom right has changed!")
        # If it's a full seat
        # elif seperated_current_line[lining] == "#":
            #

        lining = lining + 1

    appending = "".join(seperated_current_line)
    print(appending)
    changed_all_lines.append(appending)

    line_no = line_no + 1

save = "\n".join(changed_all_lines)
with open("C:/Users/2005s/Documents/Visual Studio Code/Advent-of-Code-2020/Day 11/After changing.txt", "w") as f:
    f.write(save)
