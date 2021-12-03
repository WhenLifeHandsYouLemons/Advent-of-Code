"""
Advent of Code: Day 3
"""

all_lines = []
line_no = 0

with open("2021/Day 3/Day 3 Resources.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)
# print(all_lines)
backup_lines = all_lines.copy()

# Find out length of each line
length_of_bits = all_lines[0]
length_of_bits = len(length_of_bits)

# For oxygen rating system
zeros = 0
ones = 0
current_number = 0
position_bit = 0
true_position = 0
removing = False
oxygen_generator = ""

while true_position != length_of_bits:
    # Go through entire input list
    while line_no != len(all_lines):
        # Split each bit
        current_number = list(all_lines[line_no])

        # Get the first bit
        current_bit = int(current_number[true_position])

        if current_bit == 0:
            zeros = zeros + 1
        elif current_bit == 1:
            ones = ones + 1

        line_no = line_no + 1

    if zeros > ones and len(all_lines) != 1:
        removing = True
        lined = 0

        while removing == True and lined != len(all_lines):
            current_numbered = list(all_lines[lined])

            if current_numbered[true_position] == "1":
                all_lines.pop(lined)
                lined = 0
            else:
                lined = lined + 1
    elif zeros < ones and len(all_lines) != 1:
        removing = True
        lined = 0

        while removing == True and lined != len(all_lines):
            current_numbered = list(all_lines[lined])

            if current_numbered[true_position] == "0":
                all_lines.pop(lined)
                lined = 0
            else:
                lined = lined + 1
    elif zeros == ones and len(all_lines) != 1:
        removing = True
        lined = 0

        while removing == True and lined != len(all_lines):
            current_numbered = list(all_lines[lined])

            if current_numbered[true_position] == "0":
                all_lines.pop(lined)
                lined = 0
            else:
                lined = lined + 1

    oxygen_generator = all_lines[0]
    removing = False

    true_position = true_position + 1
    zeros = 0
    ones = 0
    line_no = 0

print(f"Oxygen generator rating: {oxygen_generator}")


# For CO2 rating system
line_no = 0
zeros = 0
ones = 0
current_number = 0
position_bit = 0
true_position = 0
removing = False
co2_generator = ""

while true_position != length_of_bits:
    # Go through entire input list
    while line_no != len(backup_lines):
        # Split each bit
        current_number = list(backup_lines[line_no])

        # Get the first bit
        current_bit = int(current_number[true_position])

        if current_bit == 0:
            zeros = zeros + 1
        elif current_bit == 1:
            ones = ones + 1

        line_no = line_no + 1

    if zeros < ones and len(backup_lines) != 1:
        removing = True
        lined = 0

        while removing == True and lined != len(backup_lines):
            current_numbered = list(backup_lines[lined])

            if current_numbered[true_position] == "1":
                backup_lines.pop(lined)
                lined = 0
            else:
                lined = lined + 1
    elif zeros > ones and len(backup_lines) != 1:
        removing = True
        lined = 0

        while removing == True and lined != len(backup_lines):
            current_numbered = list(backup_lines[lined])

            if current_numbered[true_position] == "0":
                backup_lines.pop(lined)
                lined = 0
            else:
                lined = lined + 1
    elif zeros == ones and len(backup_lines) != 1:
        removing = True
        lined = 0

        while removing == True and lined != len(backup_lines):
            current_numbered = list(backup_lines[lined])
            
            if current_numbered[true_position] == "1":
                backup_lines.pop(lined)
                lined = 0
            else:
                lined = lined + 1

    co2_generator = backup_lines[0]
    removing = False

    true_position = true_position + 1
    zeros = 0
    ones = 0
    line_no = 0

print(f"CO2 scrubber rating: {co2_generator}")

life_support_rating = int(co2_generator, 2) * int(oxygen_generator, 2)
print(f"Life support rating: {life_support_rating}")
