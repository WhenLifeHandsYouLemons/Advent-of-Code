'''
Advent of Code: Day 2
'''
all_lines = []

with open('2024/Day 2/data.txt', 'r') as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)

def part1():
    global all_lines
    line_no = 0
    total_safe = 0

    while line_no != len(all_lines):
        line = all_lines[line_no]

        levels = line.split(" ")
        safe = True
        change = None

        # Check if the current row of levels are safe
        for i in range(len(levels)):
            if i != 0:
                prev_level = int(levels[i-1])
                cur_level = int(levels[i])

                if change == None and prev_level < cur_level:
                    change = "increase"
                elif change == None and prev_level > cur_level:
                    change = "decrease"

                if change == "increase" and prev_level > cur_level:
                    safe = False
                    break
                elif change == "decrease" and prev_level < cur_level:
                    safe = False
                    break
                elif abs(max(prev_level, cur_level) - min(prev_level, cur_level)) > 3 or abs(max(prev_level, cur_level) - min(prev_level, cur_level)) < 1:
                    safe = False
                    break

        if safe == True:
            total_safe += 1

        line_no += 1

    return total_safe

def part2():
    global all_lines
    line_no = 0

    # def isDampened(change, pprev, prev, cur) -> bool:
    #     if change == "increase" and pprev > cur:
    #         return False
    #     elif change == "decrease" and pprev < cur:
    #         return False
    #     elif abs(max(pprev, cur) - min(pprev, cur)) > 3 or abs(max(pprev, cur) - min(pprev, cur)) < 1:
    #         return False

    #     return True

    def checkLevel(levels: list, dampened: bool):
        change = None

        for i in range(len(levels)):
            if i != 0:
                prev_level = int(levels[i-1])
                cur_level = int(levels[i])

                if change == None and prev_level < cur_level:
                    change = "increase"
                elif change == None and prev_level > cur_level:
                    change = "decrease"

                if change == "increase" and prev_level > cur_level:
                    if not dampened:
                        new_levels = levels.copy()
                        new_levels.pop(i - 1)

                        return checkLevel(new_levels, True)
                    return False
                elif change == "decrease" and prev_level < cur_level:
                    if not dampened:
                        new_levels = levels.copy()
                        new_levels.pop(i - 1)

                        return checkLevel(new_levels, True)
                    return False
                elif abs(max(prev_level, cur_level) - min(prev_level, cur_level)) > 3 or abs(max(prev_level, cur_level) - min(prev_level, cur_level)) < 1:
                    if not dampened:
                        new_levels = levels.copy()
                        new_levels.pop(i - 1)

                        return checkLevel(new_levels, True)
                    return False

        return True


    total_safe = 0

    while line_no != len(all_lines):
        line = all_lines[line_no]

        cur_level = line.split(" ")

        # Check if the current row of levels are safe
        if checkLevel(cur_level, False):
            total_safe += 1

        line_no += 1

    return total_safe

print('Part 1 answer:', part1())
print('Part 2 answer:', part2())
