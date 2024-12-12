"""
Advent of Code: Day 7
"""

all_lines = []
line_no = 0

with open("2021/Day 7/Day 7 Resources.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)

print(all_lines)
all_crabs = all_lines[0].split(",")

# Convert to int from string and find the mean
converting = 0
while converting < len(all_crabs):
    temp = int(all_crabs[converting])
    all_crabs.pop(converting)
    all_crabs.insert(converting, temp)
    converting = converting + 1

converting = 0
mean = 0
while converting < len(all_crabs):
    mean = mean + all_crabs[converting]
    converting = converting + 1

mean = round(mean / len(all_crabs))

# Check numbers close to the mean
minimum_number = mean - 10
maximum_number = mean + 10
numbers_done = False
current_number = minimum_number
all_fuel_used = []
while numbers_done == False:
    # Check all crabs with current number
    crab_check = True
    current_crab = 0
    total_fuel = 0

    while crab_check == True:
        # Part 1
        if all_crabs[current_crab] < current_number:
            current_difference = current_number - all_crabs[current_crab]
        else:
            current_difference = all_crabs[current_crab] - current_number

        # Part 2
        current_no = 0
        fuel_to_add = 0
        adding_to_increase = 1
        while current_difference != current_no:
            fuel_to_add = fuel_to_add + adding_to_increase
            adding_to_increase = adding_to_increase + 1
            current_no = current_no + 1

        total_fuel = total_fuel + fuel_to_add

        if current_crab == len(all_crabs)-1:
            crab_check = False

        current_crab = current_crab + 1

    all_fuel_used.append(total_fuel)

    if current_number == maximum_number:
        numbers_done = True

    current_number = current_number + 1

print(all_fuel_used)

check_least = 0
lowest_fuel = 1000000000
best = 0
while check_least < len(all_fuel_used):
    if all_fuel_used[check_least] < lowest_fuel:
        lowest_fuel = all_fuel_used[check_least]
        best = check_least
    check_least = check_least + 1

print(best, lowest_fuel)
