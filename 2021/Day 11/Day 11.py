"""
Advent of Code: Day 11
"""

all_lines = []

with open("C:/Users/2005s/Desktop/Advent-of-Code/2021/Day 11/Day 11 Resources.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)

def part_1():
    line_no = 0
    # Go through each line and split each number and put it into a list into a list
    all_octopus = []
    while line_no != len(all_lines):
        # Go through the current line and add it to temp row
        current_line = all_lines[line_no]
        temp_row = []
        for octo in current_line:
            temp_row.append(int(octo))
        # Add it to the master array
        all_octopus.append(temp_row)

        line_no += 1

    # Go through each step until the desired step
    step = 0
    max_steps = 100
    total_flashes = 0
    while step < max_steps:
        # Increase octopus energy level by 1
        # Go through each row
        row_no = 0
        while row_no != len(all_octopus):
            # Go through each column in the current row
            current_row = all_octopus[row_no]
            column_no = 0
            while column_no != len(current_row):
                current_no = current_row[column_no]
                current_row.pop(column_no)
                current_row.insert(column_no, current_no + 1)
                column_no += 1
            row_no += 1

        # Flash any octopuses that are more than 9
        flashing = True
        complete = 0
        while flashing == True:
            # Go through each row
            row_no = 0
            while row_no != len(all_octopus):
                # Go through each column in the current row
                current_row = all_octopus[row_no]
                column_no = 0
                while column_no != len(current_row):
                    current_no = current_row[column_no]
                    # If the current energy level is 9
                    if current_no > 9:
                        total_flashes += 1
                        current_row.pop(column_no)
                        current_row.insert(column_no, -100)
                        # If the current row is the first one
                        if row_no == 0:
                            # If the current column is the first one
                            if column_no == 0:
                                # Change the right one
                                temp_no = current_row[column_no+1]
                                current_row.pop(column_no+1)
                                current_row.insert(column_no+1, temp_no + 1)

                                # Change the bottom one
                                temp_row = all_octopus[row_no+1]
                                temp_no = temp_row[column_no]
                                temp_row.pop(column_no)
                                temp_row.insert(column_no, temp_no + 1)

                                # Change the bottom right one
                                temp_row = all_octopus[row_no+1]
                                temp_no = temp_row[column_no+1]
                                temp_row.pop(column_no+1)
                                temp_row.insert(column_no+1, temp_no + 1)
                            # If the current column is the last one
                            elif column_no == len(current_row)-1:
                                # Change the left one
                                temp_no = current_row[column_no-1]
                                current_row.pop(column_no-1)
                                current_row.insert(column_no-1, temp_no + 1)

                                # Change the bottom one
                                temp_row = all_octopus[row_no+1]
                                temp_no = temp_row[column_no]
                                temp_row.pop(column_no)
                                temp_row.insert(column_no, temp_no + 1)

                                # Change the bottom left one
                                temp_row = all_octopus[row_no+1]
                                temp_no = temp_row[column_no-1]
                                temp_row.pop(column_no-1)
                                temp_row.insert(column_no-1, temp_no + 1)
                            # If the current column is any other
                            elif column_no > 0 and column_no < len(current_row)-1:
                                # Change the right one
                                temp_no = current_row[column_no+1]
                                current_row.pop(column_no+1)
                                current_row.insert(column_no+1, temp_no + 1)

                                # Change the left one
                                temp_no = current_row[column_no-1]
                                current_row.pop(column_no-1)
                                current_row.insert(column_no-1, temp_no + 1)

                                # Change the bottom one
                                temp_row = all_octopus[row_no+1]
                                temp_no = temp_row[column_no]
                                temp_row.pop(column_no)
                                temp_row.insert(column_no, temp_no + 1)

                                # Change the bottom left one
                                temp_row = all_octopus[row_no+1]
                                temp_no = temp_row[column_no-1]
                                temp_row.pop(column_no-1)
                                temp_row.insert(column_no-1, temp_no + 1)

                                # Change the bottom right one
                                temp_row = all_octopus[row_no+1]
                                temp_no = temp_row[column_no+1]
                                temp_row.pop(column_no+1)
                                temp_row.insert(column_no+1, temp_no + 1)
                        # If the current row is the last one
                        elif row_no == len(all_octopus)-1:
                            # If the current column is the first one
                            if column_no == 0:
                                # Change the right one
                                temp_no = current_row[column_no+1]
                                current_row.pop(column_no+1)
                                current_row.insert(column_no+1, temp_no + 1)

                                # Change the top one
                                temp_row = all_octopus[row_no-1]
                                temp_no = temp_row[column_no]
                                temp_row.pop(column_no)
                                temp_row.insert(column_no, temp_no + 1)

                                # Change the top right one
                                temp_row = all_octopus[row_no-1]
                                temp_no = temp_row[column_no+1]
                                temp_row.pop(column_no+1)
                                temp_row.insert(column_no+1, temp_no + 1)
                            # If the current column is the last one
                            elif column_no == len(current_row)-1:
                                # Change the left one
                                temp_no = current_row[column_no-1]
                                current_row.pop(column_no-1)
                                current_row.insert(column_no-1, temp_no + 1)

                                # Change the top one
                                temp_row = all_octopus[row_no-1]
                                temp_no = temp_row[column_no]
                                temp_row.pop(column_no)
                                temp_row.insert(column_no, temp_no + 1)

                                # Change the top left one
                                temp_row = all_octopus[row_no-1]
                                temp_no = temp_row[column_no-1]
                                temp_row.pop(column_no-1)
                                temp_row.insert(column_no-1, temp_no + 1)
                            # If the current column is any other
                            elif column_no > 0 and column_no < len(current_row)-1:
                                # Change the right one
                                temp_no = current_row[column_no+1]
                                current_row.pop(column_no+1)
                                current_row.insert(column_no+1, temp_no + 1)

                                # Change the left one
                                temp_no = current_row[column_no-1]
                                current_row.pop(column_no-1)
                                current_row.insert(column_no-1, temp_no + 1)

                                # Change the top one
                                temp_row = all_octopus[row_no-1]
                                temp_no = temp_row[column_no]
                                temp_row.pop(column_no)
                                temp_row.insert(column_no, temp_no + 1)

                                # Change the top left one
                                temp_row = all_octopus[row_no-1]
                                temp_no = temp_row[column_no-1]
                                temp_row.pop(column_no-1)
                                temp_row.insert(column_no-1, temp_no + 1)

                                # Change the top right one
                                temp_row = all_octopus[row_no-1]
                                temp_no = temp_row[column_no+1]
                                temp_row.pop(column_no+1)
                                temp_row.insert(column_no+1, temp_no + 1)
                        # If the current row is any other one
                        elif row_no > 0 and row_no < len(all_octopus)-1:
                            # If the current column is the first one
                            if column_no == 0:
                                # Change the top one
                                temp_row = all_octopus[row_no-1]
                                temp_no = temp_row[column_no]
                                temp_row.pop(column_no)
                                temp_row.insert(column_no, temp_no + 1)

                                # Change the top right one
                                temp_row = all_octopus[row_no-1]
                                temp_no = temp_row[column_no+1]
                                temp_row.pop(column_no+1)
                                temp_row.insert(column_no+1, temp_no + 1)

                                # Change the right one
                                temp_no = current_row[column_no+1]
                                current_row.pop(column_no+1)
                                current_row.insert(column_no+1, temp_no + 1)

                                # Change the bottom one
                                temp_row = all_octopus[row_no+1]
                                temp_no = temp_row[column_no]
                                temp_row.pop(column_no)
                                temp_row.insert(column_no, temp_no + 1)

                                # Change the bottom right one
                                temp_row = all_octopus[row_no+1]
                                temp_no = temp_row[column_no+1]
                                temp_row.pop(column_no+1)
                                temp_row.insert(column_no+1, temp_no + 1)
                            # If the current column is the last one
                            elif column_no == len(current_row)-1:
                                # Change the top one
                                temp_row = all_octopus[row_no-1]
                                temp_no = temp_row[column_no]
                                temp_row.pop(column_no)
                                temp_row.insert(column_no, temp_no + 1)

                                # Change the top left one
                                temp_row = all_octopus[row_no-1]
                                temp_no = temp_row[column_no-1]
                                temp_row.pop(column_no-1)
                                temp_row.insert(column_no-1, temp_no + 1)

                                # Change the left one
                                temp_no = current_row[column_no-1]
                                current_row.pop(column_no-1)
                                current_row.insert(column_no-1, temp_no + 1)

                                # Change the bottom one
                                temp_row = all_octopus[row_no+1]
                                temp_no = temp_row[column_no]
                                temp_row.pop(column_no)
                                temp_row.insert(column_no, temp_no + 1)

                                # Change the bottom left one
                                temp_row = all_octopus[row_no+1]
                                temp_no = temp_row[column_no-1]
                                temp_row.pop(column_no-1)
                                temp_row.insert(column_no-1, temp_no + 1)
                            # If the current column is any other
                            elif column_no > 0 and column_no < len(current_row)-1:
                                # Change the top one
                                temp_row = all_octopus[row_no-1]
                                temp_no = temp_row[column_no]
                                temp_row.pop(column_no)
                                temp_row.insert(column_no, temp_no + 1)

                                # Change the top right one
                                temp_row = all_octopus[row_no-1]
                                temp_no = temp_row[column_no+1]
                                temp_row.pop(column_no+1)
                                temp_row.insert(column_no+1, temp_no + 1)

                                # Change the right one
                                temp_no = current_row[column_no+1]
                                current_row.pop(column_no+1)
                                current_row.insert(column_no+1, temp_no + 1)

                                # Change the bottom one
                                temp_row = all_octopus[row_no+1]
                                temp_no = temp_row[column_no]
                                temp_row.pop(column_no)
                                temp_row.insert(column_no, temp_no + 1)

                                # Change the bottom right one
                                temp_row = all_octopus[row_no+1]
                                temp_no = temp_row[column_no+1]
                                temp_row.pop(column_no+1)
                                temp_row.insert(column_no+1, temp_no + 1)

                                # Change the bottom left one
                                temp_row = all_octopus[row_no+1]
                                temp_no = temp_row[column_no-1]
                                temp_row.pop(column_no-1)
                                temp_row.insert(column_no-1, temp_no + 1)

                                # Change the top left one
                                temp_row = all_octopus[row_no-1]
                                temp_no = temp_row[column_no-1]
                                temp_row.pop(column_no-1)
                                temp_row.insert(column_no-1, temp_no + 1)

                                # Change the left one
                                temp_no = current_row[column_no-1]
                                current_row.pop(column_no-1)
                                current_row.insert(column_no-1, temp_no + 1)
                        column_no = 0
                        complete = 0
                    elif current_no <= 9:
                        complete += 1

                    if complete == 100:
                        flashing = False

                    column_no += 1
                row_no += 1

        # Make all the negative numbers equal to 0 instead
        reset = True
        while reset == True:
            # Go through each row
            row_no = 0
            while row_no != len(all_octopus):
                # Go through each column in the current row
                current_row = all_octopus[row_no]
                column_no = 0
                while column_no != len(current_row):
                    current_no = current_row[column_no]
                    # If the current energy level is negative
                    if current_no < 0 or current_no > 9:
                        current_row.pop(column_no)
                        current_row.insert(column_no, 0)
                    column_no += 1
                row_no += 1
            reset = False

        # Go through and see if every single one is a 0
        total = 0
        for row in all_octopus:
            for column in row:
                if column == 0:
                    total += 1
        if total == 100:
            finished = 0
        else:
            step += 1
    return total_flashes

def part_2():
    line_no = 0
    # Go through each line and split each number and put it into a list into a list
    all_octopus = []
    while line_no != len(all_lines):
        # Go through the current line and add it to temp row
        current_line = all_lines[line_no]
        temp_row = []
        for octo in current_line:
            temp_row.append(int(octo))
        # Add it to the master array
        all_octopus.append(temp_row)

        line_no += 1

    # Go through each step until the desired step
    step = 0
    max_steps = 100
    total_flashes = 0
    finished = False
    while finished == False:
        # Increase octopus energy level by 1
        # Go through each row
        row_no = 0
        while row_no != len(all_octopus):
            # Go through each column in the current row
            current_row = all_octopus[row_no]
            column_no = 0
            while column_no != len(current_row):
                current_no = current_row[column_no]
                current_row.pop(column_no)
                current_row.insert(column_no, current_no + 1)
                column_no += 1
            row_no += 1

        # Flash any octopuses that are more than 9
        flashing = True
        complete = 0
        while flashing == True:
            # Go through each row
            row_no = 0
            while row_no != len(all_octopus):
                # Go through each column in the current row
                current_row = all_octopus[row_no]
                column_no = 0
                while column_no != len(current_row):
                    current_no = current_row[column_no]
                    # If the current energy level is 9
                    if current_no > 9:
                        total_flashes += 1
                        current_row.pop(column_no)
                        current_row.insert(column_no, -100)
                        # If the current row is the first one
                        if row_no == 0:
                            # If the current column is the first one
                            if column_no == 0:
                                # Change the right one
                                temp_no = current_row[column_no+1]
                                current_row.pop(column_no+1)
                                current_row.insert(column_no+1, temp_no + 1)

                                # Change the bottom one
                                temp_row = all_octopus[row_no+1]
                                temp_no = temp_row[column_no]
                                temp_row.pop(column_no)
                                temp_row.insert(column_no, temp_no + 1)

                                # Change the bottom right one
                                temp_row = all_octopus[row_no+1]
                                temp_no = temp_row[column_no+1]
                                temp_row.pop(column_no+1)
                                temp_row.insert(column_no+1, temp_no + 1)
                            # If the current column is the last one
                            elif column_no == len(current_row)-1:
                                # Change the left one
                                temp_no = current_row[column_no-1]
                                current_row.pop(column_no-1)
                                current_row.insert(column_no-1, temp_no + 1)

                                # Change the bottom one
                                temp_row = all_octopus[row_no+1]
                                temp_no = temp_row[column_no]
                                temp_row.pop(column_no)
                                temp_row.insert(column_no, temp_no + 1)

                                # Change the bottom left one
                                temp_row = all_octopus[row_no+1]
                                temp_no = temp_row[column_no-1]
                                temp_row.pop(column_no-1)
                                temp_row.insert(column_no-1, temp_no + 1)
                            # If the current column is any other
                            elif column_no > 0 and column_no < len(current_row)-1:
                                # Change the right one
                                temp_no = current_row[column_no+1]
                                current_row.pop(column_no+1)
                                current_row.insert(column_no+1, temp_no + 1)

                                # Change the left one
                                temp_no = current_row[column_no-1]
                                current_row.pop(column_no-1)
                                current_row.insert(column_no-1, temp_no + 1)

                                # Change the bottom one
                                temp_row = all_octopus[row_no+1]
                                temp_no = temp_row[column_no]
                                temp_row.pop(column_no)
                                temp_row.insert(column_no, temp_no + 1)

                                # Change the bottom left one
                                temp_row = all_octopus[row_no+1]
                                temp_no = temp_row[column_no-1]
                                temp_row.pop(column_no-1)
                                temp_row.insert(column_no-1, temp_no + 1)

                                # Change the bottom right one
                                temp_row = all_octopus[row_no+1]
                                temp_no = temp_row[column_no+1]
                                temp_row.pop(column_no+1)
                                temp_row.insert(column_no+1, temp_no + 1)
                        # If the current row is the last one
                        elif row_no == len(all_octopus)-1:
                            # If the current column is the first one
                            if column_no == 0:
                                # Change the right one
                                temp_no = current_row[column_no+1]
                                current_row.pop(column_no+1)
                                current_row.insert(column_no+1, temp_no + 1)

                                # Change the top one
                                temp_row = all_octopus[row_no-1]
                                temp_no = temp_row[column_no]
                                temp_row.pop(column_no)
                                temp_row.insert(column_no, temp_no + 1)

                                # Change the top right one
                                temp_row = all_octopus[row_no-1]
                                temp_no = temp_row[column_no+1]
                                temp_row.pop(column_no+1)
                                temp_row.insert(column_no+1, temp_no + 1)
                            # If the current column is the last one
                            elif column_no == len(current_row)-1:
                                # Change the left one
                                temp_no = current_row[column_no-1]
                                current_row.pop(column_no-1)
                                current_row.insert(column_no-1, temp_no + 1)

                                # Change the top one
                                temp_row = all_octopus[row_no-1]
                                temp_no = temp_row[column_no]
                                temp_row.pop(column_no)
                                temp_row.insert(column_no, temp_no + 1)

                                # Change the top left one
                                temp_row = all_octopus[row_no-1]
                                temp_no = temp_row[column_no-1]
                                temp_row.pop(column_no-1)
                                temp_row.insert(column_no-1, temp_no + 1)
                            # If the current column is any other
                            elif column_no > 0 and column_no < len(current_row)-1:
                                # Change the right one
                                temp_no = current_row[column_no+1]
                                current_row.pop(column_no+1)
                                current_row.insert(column_no+1, temp_no + 1)

                                # Change the left one
                                temp_no = current_row[column_no-1]
                                current_row.pop(column_no-1)
                                current_row.insert(column_no-1, temp_no + 1)

                                # Change the top one
                                temp_row = all_octopus[row_no-1]
                                temp_no = temp_row[column_no]
                                temp_row.pop(column_no)
                                temp_row.insert(column_no, temp_no + 1)

                                # Change the top left one
                                temp_row = all_octopus[row_no-1]
                                temp_no = temp_row[column_no-1]
                                temp_row.pop(column_no-1)
                                temp_row.insert(column_no-1, temp_no + 1)

                                # Change the top right one
                                temp_row = all_octopus[row_no-1]
                                temp_no = temp_row[column_no+1]
                                temp_row.pop(column_no+1)
                                temp_row.insert(column_no+1, temp_no + 1)
                        # If the current row is any other one
                        elif row_no > 0 and row_no < len(all_octopus)-1:
                            # If the current column is the first one
                            if column_no == 0:
                                # Change the top one
                                temp_row = all_octopus[row_no-1]
                                temp_no = temp_row[column_no]
                                temp_row.pop(column_no)
                                temp_row.insert(column_no, temp_no + 1)

                                # Change the top right one
                                temp_row = all_octopus[row_no-1]
                                temp_no = temp_row[column_no+1]
                                temp_row.pop(column_no+1)
                                temp_row.insert(column_no+1, temp_no + 1)

                                # Change the right one
                                temp_no = current_row[column_no+1]
                                current_row.pop(column_no+1)
                                current_row.insert(column_no+1, temp_no + 1)

                                # Change the bottom one
                                temp_row = all_octopus[row_no+1]
                                temp_no = temp_row[column_no]
                                temp_row.pop(column_no)
                                temp_row.insert(column_no, temp_no + 1)

                                # Change the bottom right one
                                temp_row = all_octopus[row_no+1]
                                temp_no = temp_row[column_no+1]
                                temp_row.pop(column_no+1)
                                temp_row.insert(column_no+1, temp_no + 1)
                            # If the current column is the last one
                            elif column_no == len(current_row)-1:
                                # Change the top one
                                temp_row = all_octopus[row_no-1]
                                temp_no = temp_row[column_no]
                                temp_row.pop(column_no)
                                temp_row.insert(column_no, temp_no + 1)

                                # Change the top left one
                                temp_row = all_octopus[row_no-1]
                                temp_no = temp_row[column_no-1]
                                temp_row.pop(column_no-1)
                                temp_row.insert(column_no-1, temp_no + 1)

                                # Change the left one
                                temp_no = current_row[column_no-1]
                                current_row.pop(column_no-1)
                                current_row.insert(column_no-1, temp_no + 1)

                                # Change the bottom one
                                temp_row = all_octopus[row_no+1]
                                temp_no = temp_row[column_no]
                                temp_row.pop(column_no)
                                temp_row.insert(column_no, temp_no + 1)

                                # Change the bottom left one
                                temp_row = all_octopus[row_no+1]
                                temp_no = temp_row[column_no-1]
                                temp_row.pop(column_no-1)
                                temp_row.insert(column_no-1, temp_no + 1)
                            # If the current column is any other
                            elif column_no > 0 and column_no < len(current_row)-1:
                                # Change the top one
                                temp_row = all_octopus[row_no-1]
                                temp_no = temp_row[column_no]
                                temp_row.pop(column_no)
                                temp_row.insert(column_no, temp_no + 1)

                                # Change the top right one
                                temp_row = all_octopus[row_no-1]
                                temp_no = temp_row[column_no+1]
                                temp_row.pop(column_no+1)
                                temp_row.insert(column_no+1, temp_no + 1)

                                # Change the right one
                                temp_no = current_row[column_no+1]
                                current_row.pop(column_no+1)
                                current_row.insert(column_no+1, temp_no + 1)

                                # Change the bottom one
                                temp_row = all_octopus[row_no+1]
                                temp_no = temp_row[column_no]
                                temp_row.pop(column_no)
                                temp_row.insert(column_no, temp_no + 1)

                                # Change the bottom right one
                                temp_row = all_octopus[row_no+1]
                                temp_no = temp_row[column_no+1]
                                temp_row.pop(column_no+1)
                                temp_row.insert(column_no+1, temp_no + 1)

                                # Change the bottom left one
                                temp_row = all_octopus[row_no+1]
                                temp_no = temp_row[column_no-1]
                                temp_row.pop(column_no-1)
                                temp_row.insert(column_no-1, temp_no + 1)

                                # Change the top left one
                                temp_row = all_octopus[row_no-1]
                                temp_no = temp_row[column_no-1]
                                temp_row.pop(column_no-1)
                                temp_row.insert(column_no-1, temp_no + 1)

                                # Change the left one
                                temp_no = current_row[column_no-1]
                                current_row.pop(column_no-1)
                                current_row.insert(column_no-1, temp_no + 1)
                        column_no = 0
                        complete = 0
                    elif current_no <= 9:
                        complete += 1

                    if complete == 100:
                        flashing = False

                    column_no += 1
                row_no += 1

        # Make all the negative numbers equal to 0 instead
        reset = True
        while reset == True:
            # Go through each row
            row_no = 0
            while row_no != len(all_octopus):
                # Go through each column in the current row
                current_row = all_octopus[row_no]
                column_no = 0
                while column_no != len(current_row):
                    current_no = current_row[column_no]
                    # If the current energy level is negative
                    if current_no < 0 or current_no > 9:
                        current_row.pop(column_no)
                        current_row.insert(column_no, 0)
                    column_no += 1
                row_no += 1
            reset = False

        # Go through and see if every single one is a 0
        total = 0
        for row in all_octopus:
            for column in row:
                if column == 0:
                    total += 1
        if total == 100:
            finished = True
        else:
            step += 1
    return step+1

print("Part 1: ", part_1())
print("Part 2: ", part_2())
