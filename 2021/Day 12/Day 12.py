"""
Advent of Code: Day 12
"""
from collections import defaultdict

all_lines = []

with open("C:/Users/2005s/Desktop/Advent-of-Code/2021/Day 12/Day 12 Resources.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)

small_caves = 'abcdefghijklmnopqrstuvwxyz'

all_caves = defaultdict(list)
for line in all_lines:
    x, y = line.split("-")
    all_caves[x].append(y)
    all_caves[y].append(x)


def part_1(current_cave, visited_small_caves):
    # If it's at the end hooray!
    if current_cave == 'end':
        return 1

    # Number of pathways
    count = 0

    for next in all_caves[current_cave]:
        # If it's at the end or in a small cave
        if next != 'end' and next[0] in small_caves:
            # If it hasn't visited this small cave once
            if next not in visited_small_caves:
                # Add this cave to visited cave and continue
                count += part_1(next, visited_small_caves | set([next]))
        # If it's in a big cave
        else:
            # Just continue
            count += part_1(next, visited_small_caves)

    return count

def part_2(current, visited_small_caves_once, visited_small_caves_twice):
    # If it's at the end hooray!
    if current == 'end':
        return 1

    # Number of pathways
    count = 0

    for next in all_caves[current]:
        # If it's at the start
        if next == 'start':
            # Don't do anything
            continue
        # If it's at the end or in a small cave
        elif next != 'end' and next[0] in small_caves:
            # If it visited this small cave once
            if next in visited_small_caves_once:
                # If didn't visit it twice
                if not visited_small_caves_twice:
                    # Continue from there but make it have visited this cave twice
                    count += part_2(next, visited_small_caves_once, True)
            # If it didn't visit this at all
            else:
                # Add this cave to the visited once and continue
                count += part_2(next, visited_small_caves_once | set([next]), visited_small_caves_twice)
        # If it's in a big cave
        else:
            # Just continue
            count += part_2(next, visited_small_caves_once, visited_small_caves_twice)

    return count

print("Part 1: ", part_1('start', set(['start'])))
print("Part 2: ", part_2('start', set(), False))
