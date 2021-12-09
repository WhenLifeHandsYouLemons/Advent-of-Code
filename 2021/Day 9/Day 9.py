"""
Advent of Code: Day 9
"""

all_lines = []
line_no = 0

with open("2021/Day 9/Day 9 Resources.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)
# print(all_lines)

def part_1():
    row_no = 0
    total_smaller = 0
    risk_level = 0
    while row_no < len(all_lines):
        row_chose = all_lines[row_no]
        row = []

        # Organise the row
        for number in row_chose:
            row.append(number)

        row_type = "other"
        # If it's the first row
        if row_no == 0:
            row_type = "first"
        # If it's the last row
        elif row_no == len(all_lines)-1:
            row_type = "last"

        column_no = 0
        while column_no != len(row):
            current_no = row[column_no]
            column_type = "other"
            # If it's the first column
            if column_no == 0:
                column_type = "first"
            # If it's the last column
            if column_no == len(row_chose)-1:
                column_type = "last"

            # If it's the first row, first column
            if row_type == "first" and column_type == "first":
                # Set the values of the ones around it
                right = row[column_no+1]

                temp_row = []
                for number in all_lines[row_no+1]:
                    temp_row.append(number)
                down = temp_row[column_no]

                # Check if they're all smaller
                if current_no < down and current_no < right:
                    total_smaller += 1
                    risk_level = risk_level + 1 + int(current_no)
            # If it's the other row, first column
            elif row_type == "other" and column_type == "first":
                # Set the values of the ones around it
                right = row[column_no+1]

                temp_row = []
                for number in all_lines[row_no+1]:
                    temp_row.append(number)
                down = temp_row[column_no]

                temp_row = []
                for number in all_lines[row_no-1]:
                    temp_row.append(number)
                up = temp_row[column_no]

                # Check if they're all smaller
                if current_no < down and current_no < up and current_no < right:
                    total_smaller += 1
                    risk_level = risk_level + 1 + int(current_no)
            # If it's the last row, first column
            elif row_type == "last" and column_type == "first":
                # Set the values of the ones around it
                right = row[column_no+1]

                temp_row = []
                for number in all_lines[row_no-1]:
                    temp_row.append(number)
                up = temp_row[column_no]

                # Check if they're all smaller
                if current_no < up and current_no < right:
                    total_smaller += 1
                    risk_level = risk_level + 1 + int(current_no)
            # If it's the first row, other column
            elif row_type == "first" and column_type == "other":
                # Set the values of the ones around it
                right = row[column_no+1]
                left = row[column_no-1]

                temp_row = []
                for number in all_lines[row_no+1]:
                    temp_row.append(number)
                down = temp_row[column_no]

                # Check if they're all smaller
                if current_no < down and current_no < right and current_no < left:
                    total_smaller += 1
                    risk_level = risk_level + 1 + int(current_no)
            # If it's the first row, last column
            elif row_type == "first" and column_type == "last":
                # Set the values of the ones around it
                left = row[column_no-1]

                temp_row = []
                for number in all_lines[row_no+1]:
                    temp_row.append(number)
                down = temp_row[column_no]

                # Check if they're all smaller
                if current_no < down and current_no < left:
                    total_smaller += 1
                    risk_level = risk_level + 1 + int(current_no)
            # If it's the other row, other column
            elif row_type == "other" and column_type == "other":
                # Set the values of the ones around it
                left = row[column_no-1]
                right = row[column_no+1]

                temp_row = []
                for number in all_lines[row_no+1]:
                    temp_row.append(number)
                down = temp_row[column_no]

                temp_row = []
                for number in all_lines[row_no-1]:
                    temp_row.append(number)
                up = temp_row[column_no]

                # Check if they're all smaller
                if current_no < down and current_no < left and current_no < up and current_no < right:
                    total_smaller += 1
                    risk_level = risk_level + 1 + int(current_no)
            # If it's the other row, last column
            elif row_type == "other" and column_type == "last":
                # Set the values of the ones around it
                left = row[column_no-1]

                temp_row = []
                for number in all_lines[row_no+1]:
                    temp_row.append(number)
                down = temp_row[column_no]

                temp_row = []
                for number in all_lines[row_no-1]:
                    temp_row.append(number)
                up = temp_row[column_no]

                # Check if they're all smaller
                if current_no < down and current_no < left and current_no < up:
                    total_smaller += 1
                    risk_level = risk_level + 1 + int(current_no)
            # If it's the last row, other column
            elif row_type == "last" and column_type == "other":
                # Set the values of the ones around it
                right = row[column_no+1]
                left = row[column_no-1]

                temp_row = []
                for number in all_lines[row_no-1]:
                    temp_row.append(number)
                up = temp_row[column_no]

                # Check if they're all smaller
                if current_no < up and current_no < right and current_no < left:
                    total_smaller += 1
                    risk_level = risk_level + 1 + int(current_no)
            # If it's the last row, last column
            elif row_type == "last" and column_type == "last":
                # Set the values of the ones around it
                left = row[column_no-1]

                temp_row = []
                for number in all_lines[row_no-1]:
                    temp_row.append(number)
                up = temp_row[column_no]

                # Check if they're all smaller
                if current_no < up and current_no < left:
                    total_smaller += 1
                    risk_level = risk_level + 1 + int(current_no)

            # print(row_type, column_type, total_smaller, risk_level)
            column_no += 1

        row_no += 1

    return risk_level

def part_2():
    print('TOO HARD')

# print("Part 1: ", part_1())
part_2()