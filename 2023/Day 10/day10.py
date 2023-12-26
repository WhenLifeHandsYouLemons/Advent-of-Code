"""
Advent of Code: Day 10
"""
import sys
# Set a larger recursion limit for tail recursion
print(f"Old recursion limit: {sys.getrecursionlimit()}")
sys.setrecursionlimit(14000)
print(f"New recursion limit: {sys.getrecursionlimit()}\n")

all_lines = []

with open('2023/Day 10/data.txt', 'r') as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)

def part1():
    global all_lines

    possible_pipes = ["|", "-", "L", "J", "7", "F"]

    # Add all positions into a 2d array
    floor_map = [[pos for pos in line] for line in all_lines]

    # Go through and find the starting point S
    y = 0
    found = False
    while not found:
        x = 0
        if "S" in floor_map[y]:
            x = floor_map[y].index("S")
            y -= 1
            found = True
        y += 1

    starting_coords = (x, y)

    # Figure out what type of pipe the S is supposed to be
    s = "|"     #! REMEMBER TO CHANGE THIS DEPENDING ON THE INPUT

    def traverseMap(cur_pos: tuple, prev_pos: tuple, steps: int, start: bool=False):
        if start:
            cur_symbol = s
        else:
            cur_symbol = floor_map[cur_pos[1]][cur_pos[0]]

        if cur_symbol == "S" and not start:
            return steps
        elif cur_symbol == possible_pipes[0]:    # "|"
            # Calculate which direction we need to go in
            if prev_pos[1] < cur_pos[1]:
                return traverseMap((cur_pos[0], cur_pos[1]+1), cur_pos, steps+1)
            else:
                return traverseMap((cur_pos[0], cur_pos[1]-1), cur_pos, steps+1)
        elif cur_symbol == possible_pipes[1]:    # "-"
            # Calculate which direction we need to go in
            if prev_pos[0] < cur_pos[0]:
                return traverseMap((cur_pos[0]+1, cur_pos[1]), cur_pos, steps+1)
            else:
                return traverseMap((cur_pos[0]-1, cur_pos[1]), cur_pos, steps+1)
        elif cur_symbol == possible_pipes[2]:    # "L"
            # Calculate which direction we need to go in
            if prev_pos[1] < cur_pos[1]:
                return traverseMap((cur_pos[0]+1, cur_pos[1]), cur_pos, steps+1)
            else:
                return traverseMap((cur_pos[0], cur_pos[1]-1), cur_pos, steps+1)
        elif cur_symbol == possible_pipes[3]:    # "J"
            # Calculate which direction we need to go in
            if prev_pos[1] < cur_pos[1]:
                return traverseMap((cur_pos[0]-1, cur_pos[1]), cur_pos, steps+1)
            else:
                return traverseMap((cur_pos[0], cur_pos[1]-1), cur_pos, steps+1)
        elif cur_symbol == possible_pipes[4]:    # "7"
            # Calculate which direction we need to go in
            if prev_pos[1] > cur_pos[1]:
                return traverseMap((cur_pos[0]-1, cur_pos[1]), cur_pos, steps+1)
            else:
                return traverseMap((cur_pos[0], cur_pos[1]+1), cur_pos, steps+1)
        elif cur_symbol == possible_pipes[5]:    # "F"
            # Calculate which direction we need to go in
            if prev_pos[1] > cur_pos[1]:
                return traverseMap((cur_pos[0]+1, cur_pos[1]), cur_pos, steps+1)
            else:
                return traverseMap((cur_pos[0], cur_pos[1]+1), cur_pos, steps+1)

    steps_taken = traverseMap(starting_coords, starting_coords, 0, True)

    furthest_distance = int(steps_taken / 2)

    print(furthest_distance)

def part2():
    global all_lines
    line_no = 0
    while line_no != len(all_lines):
        line = all_lines[line_no]

        line_no += 1

    print()

part1()
part2()
