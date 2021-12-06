"""
Advent of Code: Day 6
"""

all_lines = []
all_fish = []
line_no = 0

with open("C:/Users/2005s/Desktop/Advent-of-Code/2021/Day 6/Day 6 Resources.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)

all_fish = all_lines[0].split(",")

# Split the inputs into seperate ints
while line_no != len(all_fish):
    temp_fish = int(all_fish[line_no])
    all_fish.pop(line_no)
    all_fish.insert(line_no, temp_fish)
    line_no = line_no + 1
# print(all_fish)

# Go through each day
day = 0
while day != 256:
    # Go through each fish and change the value
    changing = True
    current_fish = 0

    new_fish = []

    while changing == True:
        # Remove one
        temp_fish = all_fish[current_fish]
        all_fish.pop(current_fish)
        all_fish.insert(current_fish, temp_fish-1)

        # Check if the fish life is -1
        if all_fish[current_fish] == -1:
            new_fish.append(8)
            all_fish.pop(current_fish)
            all_fish.insert(current_fish, 6)

        # Go to next fish
        current_fish = current_fish + 1

        # Check if all fish are checked for today
        if current_fish == len(all_fish):
            changing = False

    for fish in new_fish:
        all_fish.append(fish)

    day = day + 1

total_fish = len(all_fish)

print(total_fish)