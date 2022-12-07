"""
Advent of Code: Day 6
"""

all_lines = []
line_no = 0

with open("2022/Day 6/data.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)
print(all_lines)

all_letters = []
for letter in all_lines[0]:
    all_letters.append(letter)

chars = 14
while line_no != len(all_letters)-chars:
    temp = []
    for i in range(line_no, line_no+chars):
        temp.append(all_letters[i])
    temp_set = set(temp)

    if len(temp) == len(temp_set):
        break

    line_no = line_no + 1

print(line_no+chars)