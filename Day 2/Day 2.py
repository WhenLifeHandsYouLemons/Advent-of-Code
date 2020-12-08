"""
Advent of Code: Day 2
"""

all_lines = []
valid_lines = 0
line_no = 0
current_line = 0
current_policy = 0
min_no_of_times = 0
max_no_of_times = 0
policy_letter = ""
password = ""
count_for_letter = 0

with open("C:/Users/2005s/Documents/Visual Studio Code/Advent-of-Code-2020/Day 2/Day 2 Resources.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)
print(all_lines)

while line_no != len(all_lines):
    current_line = all_lines[line_no].split(":")
    password = current_line[1]
    print(password)

    current_policy = current_line[0].split(" ")
    policy_letter = current_policy[1]
    print(policy_letter)

    current_min_max = current_policy[0].split("-")
    min_no_of_times = int(current_min_max[0])
    print(min_no_of_times)

    max_no_of_times = int(current_min_max[1])
    print(max_no_of_times)

    for letter in password:
        if letter == policy_letter:
            count_for_letter = count_for_letter + 1

    if count_for_letter >= min_no_of_times and count_for_letter <= max_no_of_times:
        valid_lines = valid_lines + 1
        print(valid_lines)

    line_no = line_no + 1
    current_line = 0
    current_policy = 0
    min_no_of_times = 0
    max_no_of_times = 0
    policy_letter = ""
    password = ""
    count_for_letter = 0

print(f"The total number of passwords are {len(all_lines)}")
print(f"The total number of valid passwords are {valid_lines}.")
