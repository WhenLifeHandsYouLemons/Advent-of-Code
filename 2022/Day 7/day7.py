"""
Advent of Code: Day 7
"""
all_lines = []
line_no = 0

with open("2022/Day 7/data.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)

directory = {}
file_check = False
HOME = "home"
pointer = [HOME]
while line_no != len(all_lines):
    # Create files and folders
    if "$ cd " in all_lines[line_no]:
        file_check = False
    elif file_check is True:
        if "dir " not in all_lines[line_no]:
            if len(pointer) >= 2:
                directory.setdefault(f"{pointer[-2]}/{pointer[-1]}", [])
                directory[f"{pointer[-2]}/{pointer[-1]}"].append(f"{pointer[-1]}/{all_lines[line_no].split(' ')[0]}")
            else:
                directory.setdefault(pointer[-1], [])
                directory[pointer[-1]].append(f"home/{all_lines[line_no].split(' ')[0]}")
        else:
            if len(pointer) >= 2:
                directory.setdefault(f"{pointer[-2]}/{pointer[-1]}", [])
                directory[f"{pointer[-2]}/{pointer[-1]}"].append(f"{pointer[-1]}/{all_lines[line_no].split(' ')[-1]}")
            else:
                directory.setdefault(pointer[-1], [])
                directory[pointer[-1]].append(f"home/{all_lines[line_no].split(' ')[-1]}")
    elif "$ ls" in all_lines[line_no]:
        file_check = True

    # Move into folders
    if "$ cd /" in all_lines[line_no]:
        pointer = [HOME]
    elif "$ cd .." in all_lines[line_no]:
        pointer.pop()
    elif "$ cd " in all_lines[line_no]:
        command = all_lines[line_no].split(" ")
        folder_name = command[-1]
        pointer.append(folder_name)

    line_no = line_no + 1


def traverse(key):
    total = 0
    for value in directory[key]:
        next = value.split("/")[-1]
        try:
            total += int(next)
        except ValueError:
            total += traverse(value)

    return total

totals = []
for item in directory:
    totals.append(traverse(item))

summed = 0
for i in totals:
    if i <= 100000:
        summed += i

print(summed)
