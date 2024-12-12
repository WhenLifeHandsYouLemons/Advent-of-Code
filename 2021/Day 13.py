"""
Advent of Code: Day 13
"""

def print_paper(full_paper):
    for r in range(0, len(full_paper)):
        for c in range(0, len(full_paper[r])):
            print(full_paper[r][c], end="")
        print()
    print()


all_lines = []
line_no = 0

with open("C:/Users/2005s/Desktop/Advent-of-Code/2021/Day 13/Day 13 Resources.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)

coords = []
full_paper = []
instructions = []

# Seperate the instructions and coordinates
for line in all_lines:
    if "fold" in line:
        instructions.append(line)
    elif "," in line:
        coords.append(line)

# print(coords, instructions)

# Plot all the points
# Go through eah row
max_row = 0
max_column = 0
row_no = 0
while row_no != 1000:
    # Go through each column
    column_no = 0
    while column_no != 1320:
        current_coord = str(column_no) + "," + str(row_no)
        if current_coord in coords:
            if column_no > max_column:
                max_column = column_no
            if row_no > max_row:
                max_row = row_no
        column_no += 1
    row_no += 1

print("Creating array")
max_row = max_row
max_column = max_column
row_no = 0
while row_no != max_row+1:
    temp_row = []
    # Go through each column
    column_no = 0
    while column_no != max_column+1:
        current_coord = str(column_no) + "," + str(row_no)

        if current_coord in coords:
            temp_row.append("#")
            if column_no > max_column:
                max_column = column_no
            if row_no > max_row:
                max_row = row_no
        else:
            temp_row.append(".")

        column_no += 1

    full_paper.append(temp_row)

    row_no += 1

print("Doing folds")
# Do all folds
for current_instruction in instructions:
    # Print needed part of paper
    print_paper(full_paper)
    #i = 0
    #while i != 7:
    #    row = full_paper[i]
        # print(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29], row[30], row[31], row[32], row[33], row[34], row[35], row[36], row[37], row[38], row[39])
        # print(row[0], row[1], row[2], row[3], row[4])
    #    i += 1

    # FOr example
    # for row in full_paper:
    #     print(row)

    current_instruction = current_instruction.split(" ")
    current_instruction = current_instruction[-1]
    current_instruction = current_instruction.split("=")
    # Get the y or x and where
    fold_direction = current_instruction[0]
    fold_line = int(current_instruction[1])
    print(fold_direction, fold_line)

    # Do this if fold line is horizontal
    if fold_direction == "y":
        # Fold each line
        row_no = len(full_paper)-1
        while row_no != fold_line:
            # Go through the columns to change the rows from the end
            column_no = 0
            while column_no != len(full_paper[0]):
                current_row = full_paper[row_no]
                current_dot = current_row[column_no]
                # If there's a dot
                if current_dot == "#":
                    distance = row_no - fold_line
                    row_to_change = full_paper[fold_line - distance]
                    # column_to_change = row_to_change[column_no]
                    row_to_change.pop(column_no)
                    row_to_change.insert(column_no, "#")
                # print(row_no, column_no, len(full_paper[0]))
                column_no += 1
            row_no -= 1

        # Remove any folded lines
        row_no = len(full_paper)-1
        while row_no != fold_line:
            full_paper.pop(row_no)
            row_no -= 1
        full_paper.pop(row_no-1)
    # Do this if fold line is vertical
    elif fold_direction == "x":
        # Fold each row
        row_no = 0
        while row_no != len(full_paper):
            current_row = full_paper[row_no]
            # Go through each column from the back
            column_no = len(current_row)-1
            while column_no != fold_line:
                current_dot = current_row[column_no]
                if current_dot == "#":
                    distance = column_no - fold_line
                    column_to_change = fold_line - distance
                    current_row.pop(column_to_change)
                    current_row.insert(column_to_change, "#")
                column_no -= 1
            row_no += 1

        # Remove any folded lines
        row_no = 0
        column_no = len(full_paper[-1])-1
        while row_no != len(full_paper):
            current_row = full_paper[row_no]
            column_no = len(full_paper[-1])-1
            while column_no != fold_line-1:
                current_row.pop(column_no)
                column_no -= 1
            row_no += 1

# Print needed part of paper
print_paper(full_paper)

exit()
i = 0
while i != 7:
    row = full_paper[i]
    print(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29], row[30], row[31], row[32], row[33], row[34], row[35], row[36], row[37], row[38], row[39])
    # print(row[0], row[1], row[2], row[3], row[4])
    i += 1

# FOr example
# for row in full_paper:
#     print(row)

# Count the number of dots
    total_dots = 0
for row in full_paper:
    for column in row:
        if column == "#":
            total_dots += 1

print(total_dots)