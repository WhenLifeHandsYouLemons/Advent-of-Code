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
print(all_lines)

gamma_rate = []
epsilon_rate = []
zeros = 0
ones = 0
current_number = 0
position_bit = 0
true_position = 0

while true_position != 12:
    # Go through entire input list
    while line_no != len(all_lines):
        # Split each bit
        current_number = list(all_lines[line_no])
        # print(current_number)

        # Get the first bit
        current_bit = int(current_number[true_position])
        # print(current_bit)

        if current_bit == 0:
            zeros = zeros + 1
        elif current_bit == 1:
            ones = ones + 1

        # print(f"Total 0's: {zeros}")
        # print(f"Total 1's: {ones}")

        line_no = line_no + 1

    if zeros > ones:
        gamma_rate.append("0")
        epsilon_rate.append("1")
    elif zeros < ones:
        gamma_rate.append("1")
        epsilon_rate.append("0")

    true_position = true_position + 1
    zeros = 0
    ones = 0
    line_no = 0

gamma_rate = "".join(gamma_rate)
gamma_rate = int(gamma_rate, 2)
print(gamma_rate)

epsilon_rate = "".join(epsilon_rate)
epsilon_rate = int(epsilon_rate, 2)
print(epsilon_rate)

print(epsilon_rate * gamma_rate)