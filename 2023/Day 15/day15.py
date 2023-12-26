"""
Advent of Code: Day 15
"""
all_lines = []

with open('2023/Day 15/data.txt', 'r') as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)
all_lines = all_lines[0].split(",")

def part1():
    global all_lines

    total = 0

    line_no = 0
    while line_no != len(all_lines):
        line = all_lines[line_no]

        current_value = 0
        for char in line:
            current_value += ord(char)
            current_value *= 17
            current_value %= 256

        total += current_value

        line_no += 1

    print(total)

def part2():
    global all_lines

    boxes = {}

    line_no = 0
    while line_no != len(all_lines):
        line = all_lines[line_no]

        current_value = 0
        for char in line:
            if char not in "-=0123456789":
                current_value += ord(char)
                current_value *= 17
                current_value %= 256

        string = line.replace("-", "").replace("=", "")
        if string[-1] in "0123456789":
            string = string[0:-1] + " " + string[-1]

        if string[-1] in "0123456789":
            if current_value in boxes:
                try:
                    for n in range(0, 10):
                        if f"{string[0:-1]}{n}" in boxes[current_value]:
                            boxes[current_value].pop(boxes[current_value].index(f"{string[0:-1]}{n}"))
                            boxes[current_value].insert(0, string)
                            raise InterruptedError
                    boxes[current_value].append(string)
                except InterruptedError:
                    pass
            else:
                boxes[current_value] = [string]
        else:
            if current_value in boxes:
                try:
                    for n in range(0, 10):
                        try:
                            boxes[current_value].remove(f"{string} {n}")
                            raise InterruptedError
                        except ValueError:
                            pass
                except InterruptedError:
                    pass

        line_no += 1

    # Get the focusing power of all the lenses
    total_focusing_power = 0
    for key, val in boxes.items():
        for pos, camera in enumerate(val):
            focusing_power = (key + 1) * (pos + 1) * (int(camera[-1]))
            total_focusing_power += focusing_power

    print(total_focusing_power)
    print(boxes)

part1()
part2() # Not working yet
