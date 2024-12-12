'''
Advent of Code: Day 5
'''
all_lines = []

with open('2024/Day 5/data.txt', 'r') as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)

def part1():
    global all_lines
    line_no = 0

    ruleset = {}
    add_to_ruleset = True
    correct_order = []

    while line_no != len(all_lines):
        line = all_lines[line_no]

        if line == "":
            add_to_ruleset = False
        elif add_to_ruleset:
            pages = line.split("|")

            if pages[0] in ruleset.keys():
                ruleset[pages[0]].append(pages[1])
            else:
                ruleset[pages[0]] = [pages[1]]

            if pages[1] not in ruleset.keys():
                ruleset[pages[1]] = []
        else:
            pages = line.split(",")
            correct = True

            for i in range(0, len(pages) - 1):
                for j in range(i+1, len(pages)):
                    if pages[j] not in ruleset[pages[i]]:
                        correct = False
                        break

            if correct:
                correct_order.append(line)

        line_no += 1

    total = 0
    for order in correct_order:
        order = order.split(",")

        while len(order) > 1:
            order.pop(0)
            order.pop(-1)

        total += int(order[0])

    return total

def part2():
    global all_lines
    line_no = 0

    ruleset = {}
    add_to_ruleset = True
    incorrect_order = []

    while line_no != len(all_lines):
        line = all_lines[line_no]

        if line == "":
            add_to_ruleset = False
        elif add_to_ruleset:
            pages = line.split("|")

            if pages[0] in ruleset.keys():
                ruleset[pages[0]].append(pages[1])
            else:
                ruleset[pages[0]] = [pages[1]]

            if pages[1] not in ruleset.keys():
                ruleset[pages[1]] = []
        else:
            pages = line.split(",")

            incorrect = False
            for i in range(0, len(pages) - 1):
                for j in range(i+1, len(pages)):
                    if pages[j] not in ruleset[pages[i]]:
                        incorrect_order.append(line)
                        incorrect = True
                        break

                if incorrect:
                    break


        line_no += 1

    def isAfter(val1: str, val2: str) -> bool:
        if val1 in ruleset[val2]:
            return True
        return False

    fixed_order = []
    for pages in incorrect_order:
        pages = pages.split(",")
        correct_order = []

        # Do a bubble sort with a custom bool function that checks whether one value should be "higher" or "lower" than another
        # Bubble sort algorithm from: https://www.geeksforgeeks.org/python-program-for-bubble-sort/
        for n in range(len(pages) - 1, 0, -1):
            swapped = False

            for i in range(n):
                if isAfter(pages[i], pages[i + 1]):
                    pages[i], pages[i + 1] = pages[i + 1], pages[i]
                    swapped = True

            if not swapped:
                break

        correct_order = pages.copy()
        fixed_order.append(correct_order)

    total = 0
    for order in fixed_order:
        while len(order) > 1:
            order.pop(0)
            order.pop(-1)

        total += int(order[0])

    return total

print('Part 1 answer:', part1())
print('Part 2 answer:', part2())
