"""
Advent of Code: Day 9
"""
all_lines = []

with open('2023/Day 9/data.txt', 'r') as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)

def part1():
    global all_lines

    extrapolated_total = 0

    line_no = 0
    while line_no != len(all_lines):
        line = all_lines[line_no]

        # Get the top level values
        values = [[int(i) for i in line.split(" ")]]

        continue_calc = True

        # Go through the values
        while continue_calc:
            # Go through the last list in values
            i = 1
            temp = []
            while i < len(values[-1]):
                cur_val = values[-1][i]
                prev_val = values[-1][i-1]

                temp.append(cur_val-prev_val)

                i += 1

            values.append(temp)

            # Check if we need to continue calculating differences
            continue_calc = True
            if set(values[-1]) == set([0]):
                continue_calc = False

        # Extrapolate the next value
        extrapolated_value = 0
        for i in range(len(values)-1, -1, -1):
            extrapolated_value += values[i][-1]
        extrapolated_total += extrapolated_value

        line_no += 1

    print(extrapolated_total)

def part2():
    global all_lines

    extrapolated_total = 0

    line_no = 0
    while line_no != len(all_lines):
        line = all_lines[line_no]

        # Get the top level values
        values = [[int(i) for i in line.split(" ")]]

        continue_calc = True

        # Go through the values
        while continue_calc:
            # Go through the last list in values
            i = 1
            temp = []
            while i < len(values[-1]):
                cur_val = values[-1][i]
                prev_val = values[-1][i-1]

                temp.append(cur_val-prev_val)

                i += 1

            values.append(temp)

            # Check if we need to continue calculating differences
            continue_calc = True
            if set(values[-1]) == set([0]):
                continue_calc = False

        # Extrapolate the next value
        extrapolated_value = 0
        for i in range(len(values)-1, -1, -1):
            extrapolated_value = values[i][0] - extrapolated_value
        extrapolated_total += extrapolated_value

        line_no += 1

    print(extrapolated_total)

part1()
part2()
