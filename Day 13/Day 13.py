"""
Advent of Code: Day 13
"""

all_lines = []
line_no = 0
starting_time = 0
current_time = starting_time
best_time = 2000000
best_bus_id = 0

with open("C:/Users/2005s/Documents/Visual Studio Code/Advent-of-Code-2020/Day 13/Day 13 Resources.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)
print(all_lines)

arrival_time = int(all_lines[0])
all_bus_id = all_lines[1]
all_bus_id = all_bus_id.split(",")
print(arrival_time)
print(all_bus_id)

while line_no != len(all_bus_id):
    current_time = starting_time
    while current_time < arrival_time:
        current_time = current_time + int(all_bus_id[line_no])

    print(f"Bus ID {all_bus_id[line_no]} departs at {current_time}.")

    if current_time < best_time:
        best_time = current_time
        best_bus_id = all_bus_id[line_no]

    line_no = line_no + 1

waiting_time = best_time - arrival_time

print(f"The quickest bus is bus ID {best_bus_id} and you have to wait only {waiting_time} minutes!")

product = int(waiting_time) * int(best_bus_id)

print(product)
