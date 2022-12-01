"""
Advent of Code: Day 1
"""
all_lines = []

with open("Advent-of-Code/2022/Day 2/data.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(int(line))
print(all_lines)

i = 0
maxes = []
done = False
total = 0
for i in all_lines:
    if i != "":
        total += int(i)
    else:
        maxes.append(total)
        total = 0

maxes.append(total)

full = max(maxes)
maxes.remove(max(maxes))
full += max(maxes)
maxes.remove(max(maxes))
full += max(maxes)
maxes.remove(max(maxes))
print(full)
