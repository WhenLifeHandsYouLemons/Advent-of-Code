'''
Advent of Code: Day 5
'''
all_lines = []

with open('2024/Day 5/data.txt', 'r') as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)
print(all_lines)

def part1():
    global all_lines
    line_no = 0

    while line_no != len(all_lines):
        line = all_lines[line_no]

        

        line_no += 1

def part2():
    global all_lines
    line_no = 0

    while line_no != len(all_lines):
        line = all_lines[line_no]

        line_no += 1

print('Part 1 answer:', part1())
print('Part 2 answer:', part2())
