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

# Split the inputs into seperate ints
all_fish = all_lines[0].split(",")
while line_no != len(all_fish):
    temp_fish = int(all_fish[line_no])
    all_fish.pop(line_no)
    all_fish.insert(line_no, temp_fish)
    line_no = line_no + 1

# Go through each day
total_days = 200
def days(day, life):
    # Base cases
    if day == 0 and life == -1:
        return 1
    if life == -1:
        return days(day, 8) + days(day, 6)
    elif day == 0:
        return 1
    # Any other case
    else:
        return days(day-1, life-1)

total_fish = 0
for fish in all_fish:
    total_fish = total_fish + days(total_days+1, fish)
print(total_fish)
