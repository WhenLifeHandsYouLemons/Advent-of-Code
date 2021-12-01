"""
Advent of Code: Day 2
"""

all_lines = []
valid_lines = 0
line_no = 0
current_line = 0
current_policy = 0
pos1 = 0
pos2 = 0
policy_letter = ""
password = ""
password_seperation = []
count_for_letter = 0

with open("C:/Users/2005s/Documents/Visual Studio Code/Advent-of-Code-2020/Day 2/Day 2 Resources.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)
print(all_lines)

while line_no != len(all_lines):
    current_line = all_lines[line_no].split(":")
    password = current_line[1].split(" ")
    password = password[1]
    print(password)

    current_policy = current_line[0].split(" ")
    policy_letter = current_policy[1]
    print(policy_letter)

    current_min_max = current_policy[0].split("-")
    pos1 = int(current_min_max[0])
    print(pos1)

    pos2 = int(current_min_max[1])
    print(pos2)

    for letter in password:
        password_seperation.append(letter)
# Please comment out this print line unless you want a really cool wallpaper,
# or you want it to take 3 minutes to give you the result!
#    print(password_seperation)

    if password_seperation[pos1-1] == policy_letter:
        if password_seperation[pos2-1] != policy_letter:
            print(valid_lines)
            valid_lines = valid_lines + 1
    elif password_seperation[pos2-1] == policy_letter:
        valid_lines = valid_lines + 1
        print(valid_lines)

    line_no = line_no + 1
    current_line = 0
    current_policy = 0
    pos1 = 0
    pos2 = 0
    policy_letter = ""
    password = ""
    count_for_letter = 0
    password_seperation = []

print(f"The total number of passwords are {len(all_lines)}")
print(f"The total number of valid passwords are {valid_lines}.")
