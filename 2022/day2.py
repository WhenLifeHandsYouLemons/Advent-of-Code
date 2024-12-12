"""
Advent of Code: Day 2
"""

all_lines = []
line_no = 0

with open("2022/Day 2/data.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)

total = 0
while line_no != len(all_lines):
    options = all_lines[line_no].split(" ")
    your_option = options[1]
    opponent_option = options[0]

    # Rock
    if opponent_option == "A":
        # Lose
        if your_option == "X":
            total += 3
        # Draw
        elif your_option == "Y":
            total += 4
        # Win
        elif your_option == "Z":
            total += 8
    # Paper
    elif opponent_option == "B":
        # Lose
        if your_option == "X":
            total += 1
        # Draw
        elif your_option == "Y":
            total += 5
        # Win
        elif your_option == "Z":
            total += 9
    # Scissors
    elif opponent_option == "C":
        # Lose
        if your_option == "X":
            total += 2
        # Draw
        elif your_option == "Y":
            total += 6
        # Win
        elif your_option == "Z":
            total += 7

    line_no = line_no + 1

print(total)