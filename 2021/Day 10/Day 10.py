"""
Advent of Code: Day 10
"""

all_lines = []

with open("C:/Users/2005s/Desktop/Advent-of-Code/2021/Day 10/Day 10 Resources.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)

def part_1():
    # Go through each line
    new_list = []
    line_no = 0
    while line_no != len(all_lines):
        # Split the current line
        current_line = []
        for syntax in all_lines[line_no]:
            current_line.append(syntax)

        # Check if there's any that can cancel out
        checking = 0
        while checking != len(current_line):
            if checking == len(current_line)-1:
                checking = len(current_line)
            # Check the ()
            elif current_line[checking] == "(" and current_line[checking+1] == ")":
                current_line.pop(checking)
                current_line.pop(checking)
                checking = 0
            # Check the {}
            elif current_line[checking] == "{" and current_line[checking+1] == "}":
                current_line.pop(checking)
                current_line.pop(checking)
                checking = 0
            # Check the []
            elif current_line[checking] == "[" and current_line[checking+1] == "]":
                current_line.pop(checking)
                current_line.pop(checking)
                checking = 0
            # Check the <>
            elif current_line[checking] == "<" and current_line[checking+1] == ">":
                current_line.pop(checking)
                current_line.pop(checking)
                checking = 0
            else:
                checking += 1

        new_list.append("".join(current_line))

        line_no = line_no + 1

    # Remove any that don't have an ending bracket
    remove = 0
    while remove != len(new_list):
        if ")" not in new_list[remove] and "}" not in new_list[remove] and "]" not in new_list[remove] and ">" not in new_list[remove]:
            new_list.pop(remove)
            remove = 0
        else:
            remove += 1

    # Check if there's any start and end brackets and which they are
    square = 0
    curly = 0
    arrow = 0
    normal = 0
    line_no = 0
    while line_no != len(new_list):
        # Split the current line
        current_line = []
        for syntax in new_list[line_no]:
            current_line.append(syntax)

        # Go through each syntax in the current line
        find = 0
        while find != len(current_line):
            if find == len(current_line)-1:
                find = len(current_line)
            # Find any which have a start bracket and end bracket next to each other
            elif current_line[find] in "([{<" and current_line[find+1] in "]}>)":
                # Check what bracket was wrong
                if current_line[find+1] == "]":
                    square += 1
                elif current_line[find+1] == "}":
                    curly += 1
                elif current_line[find+1] == ")":
                    normal += 1
                elif current_line[find+1] == ">":
                    arrow += 1
                find = len(current_line)
            else:
                find += 1

        line_no += 1

    # Find the total
    total = (square*57) + (curly*1197) + (arrow*25137) + (normal*3)
    return total

def part_2():
    # Go through each line
    new_list = []
    line_no = 0
    while line_no != len(all_lines):
        # Split the current line
        current_line = []
        for syntax in all_lines[line_no]:
            current_line.append(syntax)

        # Check if there's any that can cancel out
        checking = 0
        while checking != len(current_line):
            if checking == len(current_line)-1:
                checking = len(current_line)
            # Check the ()
            elif current_line[checking] == "(" and current_line[checking+1] == ")":
                current_line.pop(checking)
                current_line.pop(checking)
                checking = 0
            # Check the {}
            elif current_line[checking] == "{" and current_line[checking+1] == "}":
                current_line.pop(checking)
                current_line.pop(checking)
                checking = 0
            # Check the []
            elif current_line[checking] == "[" and current_line[checking+1] == "]":
                current_line.pop(checking)
                current_line.pop(checking)
                checking = 0
            # Check the <>
            elif current_line[checking] == "<" and current_line[checking+1] == ">":
                current_line.pop(checking)
                current_line.pop(checking)
                checking = 0
            else:
                checking += 1

        new_list.append("".join(current_line))

        line_no = line_no + 1

    # Remove any that have an ending bracket
    remove = 0
    while remove != len(new_list):
        if ")" in new_list[remove] or "}" in new_list[remove] or "]" in new_list[remove] or ">" in new_list[remove]:
            new_list.pop(remove)
            remove = 0
        else:
            remove += 1

    # Go backwards through new_list and see what there is to complete
    all_additions = []
    go_in = 0
    while go_in != len(new_list):
        current_line = new_list[go_in]
        go = len(current_line)-1
        temp_additions = []
        while go >= 0:
            if current_line[go] == "(":
                temp_additions.append(")")
            elif current_line[go] == "{":
                temp_additions.append("}")
            elif current_line[go] == "[":
                temp_additions.append("]")
            elif current_line[go] == "<":
                temp_additions.append(">")

            go -= 1

        all_additions.append(temp_additions)
        go_in += 1

    # Go through all_additions and add up the total
    add_in = 0
    totals = []
    while add_in != len(all_additions):
        current_line = all_additions[add_in]
        add = 0
        temp_total = 0

        while add != len(current_line):
            if current_line[add] == ")":
                temp_total = (temp_total * 5) + 1
            elif current_line[add] == "]":
                temp_total = (temp_total * 5) + 2
            elif current_line[add] == "}":
                temp_total = (temp_total * 5) + 3
            elif current_line[add] == ">":
                temp_total = (temp_total * 5) + 4

            add += 1

        totals.append(temp_total)

        add_in += 1

    totals = sorted(totals, reverse=False)
    middle_no = totals[int((len(totals)-1)/2)]
    return middle_no


print("Part 1: ", part_1())
print("Part 2: ", part_2())
