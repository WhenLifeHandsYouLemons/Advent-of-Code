"""
Advent of Code: Day 3
"""

all_lines = []
line_no = 0

with open("2022/Day 3/data.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)

total = 0

while line_no <= len(all_lines)-2:
    all_doubles = []

    # Check if there's any duplicates across halves
    for i in all_lines[line_no]:
        if i in all_lines[line_no+1] and i in all_lines[line_no+2]:
            if i not in all_doubles:
                all_doubles.append(i)

    # Convert letter to number
    for i in all_doubles:
        if i.isupper(): # https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/
            total += ord(i) - 38 # https://bobbyhadz.com/blog/python-convert-letters-to-numbers
        elif i.islower():
            total += ord(i) - 96

    line_no = line_no + 3

print(total)
