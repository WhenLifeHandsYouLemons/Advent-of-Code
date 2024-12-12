"""
Advent of Code: Day 3
"""

all_lines = []

with open('2023/Day 3/data.txt', 'r') as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        temp = []
        for char in line:
            temp.append(char)
        all_lines.append(temp)
# print(all_lines)

def part1():
    global all_lines

    parts = []
    row_no = 0
    while row_no < len(all_lines):
        row = all_lines[row_no]

        column_no = 0
        # Go through each column in each row
        while column_no < len(row):
            cur_char = row[column_no]
            # If there's a number
            if cur_char.isdigit():
                number = []
                has_symbol = False
                # while the current char is a number
                while cur_char.isdigit() and column_no < len(row):
                    # set new cur_char
                    cur_char = row[column_no]
                    if not cur_char.isdigit():
                        break

                    # Check for a symbol all around it
                    # if it's not the top left corner
                    if row_no != 0 and column_no != 0:
                        # check top left corner
                        if all_lines[row_no-1][column_no-1] not in ".1234567890":
                            has_symbol = True
                    # if it's not the top right corner
                    if row_no != 0 and column_no != len(row)-1:
                        # check top right corner
                        if all_lines[row_no-1][column_no+1] not in ".1234567890":
                            has_symbol = True
                    # if it's not the bottom left corner
                    if row_no != len(all_lines)-1 and column_no != 0:
                        # check bottom left corner
                        if all_lines[row_no+1][column_no-1] not in ".1234567890":
                            has_symbol = True
                    # if it's not the bottom right corner
                    if row_no != len(all_lines)-1 and column_no != len(row)-1:
                        # check bottom right corner
                        if all_lines[row_no+1][column_no+1] not in ".1234567890":
                            has_symbol = True
                    # if it's not on the top edge
                    if row_no != 0:
                        # check top
                        if all_lines[row_no-1][column_no] not in ".1234567890":
                            has_symbol = True
                    # if it's not on the bottom edge
                    if row_no != len(all_lines)-1:
                        # check bottom
                        if all_lines[row_no+1][column_no] not in ".1234567890":
                            has_symbol = True
                    # if it's not on the left edge
                    if column_no != 0:
                        # check left
                        if all_lines[row_no][column_no-1] not in ".1234567890":
                            has_symbol = True
                    # if it's not on the right edge
                    if column_no != len(row)-1:
                        # check right
                        if all_lines[row_no][column_no+1] not in ".1234567890":
                            has_symbol = True

                    # add current char to number
                    number.append(cur_char)

                    # Go to next column
                    column_no += 1

                # add to parts list
                if has_symbol:
                    parts.append(number)
            else:
                column_no += 1

        row_no += 1

    parts = [int("".join(num)) for num in parts]

    print(sum(parts))

def part2():
    global all_lines

    gears_pos = {}
    row_no = 0
    while row_no < len(all_lines):
        row = all_lines[row_no]

        column_no = 0
        # Go through each column in each row
        while column_no < len(row):
            cur_char = row[column_no]
            # If there's a number
            if cur_char.isdigit():
                number = []
                same_num = False
                cur_gears = []
                # while the current char is a number
                while cur_char.isdigit() and column_no < len(row):
                    # set new cur_char
                    cur_char = row[column_no]
                    if not cur_char.isdigit():
                        break

                    # Check for a symbol all around it
                    # if it's not the top left corner
                    if row_no != 0 and column_no != 0:
                        # check top left corner
                        if all_lines[row_no-1][column_no-1] in "*":
                            if not same_num:
                                same_num = True
                                cur_gears.append((row_no-1, column_no-1))
                    # if it's not the top right corner
                    if row_no != 0 and column_no != len(row)-1:
                        # check top right corner
                        if all_lines[row_no-1][column_no+1] in "*":
                            if not same_num:
                                    same_num = True
                                    cur_gears.append((row_no-1, column_no+1))
                    # if it's not the bottom left corner
                    if row_no != len(all_lines)-1 and column_no != 0:
                        # check bottom left corner
                        if all_lines[row_no+1][column_no-1] in "*":
                            if not same_num:
                                    same_num = True
                                    cur_gears.append((row_no+1, column_no-1))
                    # if it's not the bottom right corner
                    if row_no != len(all_lines)-1 and column_no != len(row)-1:
                        # check bottom right corner
                        if all_lines[row_no+1][column_no+1] in "*":
                            if not same_num:
                                    same_num = True
                                    cur_gears.append((row_no+1, column_no+1))
                    # if it's not on the top edge
                    if row_no != 0:
                        # check top
                        if all_lines[row_no-1][column_no] in "*":
                            if not same_num:
                                    same_num = True
                                    cur_gears.append((row_no-1, column_no))
                    # if it's not on the bottom edge
                    if row_no != len(all_lines)-1:
                        # check bottom
                        if all_lines[row_no+1][column_no] in "*":
                            if not same_num:
                                    same_num = True
                                    cur_gears.append((row_no+1, column_no))
                    # if it's not on the left edge
                    if column_no != 0:
                        # check left
                        if all_lines[row_no][column_no-1] in "*":
                            if not same_num:
                                    same_num = True
                                    cur_gears.append((row_no, column_no-1))
                    # if it's not on the right edge
                    if column_no != len(row)-1:
                        # check right
                        if all_lines[row_no][column_no+1] in "*":
                            if not same_num:
                                    same_num = True
                                    cur_gears.append((row_no, column_no+1))

                    # add current char to number
                    number.append(cur_char)

                    # Go to next column
                    column_no += 1

                # go through all the unique cur_gears
                cur_gears = list(set(cur_gears))
                for gear in cur_gears:
                    # if it exists
                    if gear in gears_pos:
                        # append the current number to its list
                        gears_pos[gear].append(int("".join(number)))
                    else:
                        # create new key and add current number to it as a list
                        gears_pos[gear] = [int("".join(number))]
            else:
                column_no += 1

        row_no += 1

    gear_ratios = []
    for key, val in gears_pos.items():
        if len(val) == 2:
            total = 1
            for num in val:
                total *= num
            gear_ratios.append(total)

    print(sum(gear_ratios))

part1()
part2()
