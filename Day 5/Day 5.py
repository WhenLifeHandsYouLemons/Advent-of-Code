"""
# Advent of Code: Day 5
"""

all_lines = []
current_line = 0
split_current_line = []
highest_id_value = 0
row = 0
column = 0
max_row = 127
min_row = 0
total_rows = 127
max_column = 7
min_column = 0
total_columns = 7
line_no = 0
line_done = False
split_line_no = 0
total = row * 8 + column
all_id_values = []

with open("C:/Users/2005s/Documents/Visual Studio Code/Advent-of-Code-2020/Day 5/Day 5 Resources.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)
print(all_lines)

while line_no != len(all_lines):
    current_line = []
    current_line = all_lines[line_no]
    line_done = False

    while line_done == False:
        split_current_line = []
        max_column = total_columns
        max_row = total_rows
        min_column = 0
        max_column = 7
        min_row = 0
        max_row = 127
        split_line_no = 0

        for letter in current_line:
            split_current_line.append(letter)
        print(current_line)
        print(split_current_line)

        while split_line_no != len(split_current_line):
            current_letter = split_current_line[split_line_no]

            if current_letter == "F":
                max_row = ((min_row + (max_row + 1)) / 2) - 1
                print(f"The max row is {max_row}")
            elif current_letter == "B":
                min_row = (min_row + (max_row + 1)) / 2
                print(f"The min row is {min_row}")
            elif current_letter == "R":
                min_column = (min_column + (max_column + 1)) / 2
                print(f"The min column is {min_column}")
            elif current_letter == "L":
                max_column = ((min_column + (max_column + 1)) / 2) - 1
                print(f"The max column is {max_column}")
            else:
                print("Error!")

            split_line_no = split_line_no + 1
        
        total = (min_row * 8) + min_column
        all_id_values.append(total)
        print(f"The total is ({min_row} * 8) + {min_column} = {total}")
        if total > highest_id_value:
            highest_id_value = total

        line_done = True

    line_no = line_no + 1

print("")
print(f"The highest id value is {highest_id_value}")

print(all_id_values)
all_id_values.sort()
print(all_id_values)

check = []
check.append(all_id_values[0])
check.append(all_id_values[1])

line_no = 2
while line_no != len(all_id_values):
    if check[0]+1 != check[1]:
        print(f"The 2 values are {check[0]}, and {check[1]}")
        exit()
    else:
        check.append(all_id_values[line_no])
        check.pop(0)

    line_no = line_no + 1
