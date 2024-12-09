'''
Advent of Code: Day 4
'''
all_lines = []

with open('2024/Day 4/data.txt', 'r') as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)

def part1():
    global all_lines
    line_no = 0

    grid = []

    while line_no != len(all_lines):
        line = all_lines[line_no]

        grid.append([i for i in line])

        line_no += 1

    # Go through and find all the X's
    search_pos = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "X":
                search_pos.append((x, y))

    # Go through each search pos and look in each direction
    def continueSearch(grid: list, letters_to_find: list, direction_to_look: int, position_to_look: tuple) -> bool:
        try:
            if position_to_look[0] < 0 or position_to_look[1] < 0:
                return False
            grid[position_to_look[1]][position_to_look[0]]
        except:
            return False

        if grid[position_to_look[1]][position_to_look[0]] == letters_to_find[0]:
            if len(letters_to_find) == 1:
                return True

            if direction_to_look == 0:
                return continueSearch(grid, letters_to_find[1:], direction_to_look, (position_to_look[0], position_to_look[1] - 1))
            elif direction_to_look == 1:
                return continueSearch(grid, letters_to_find[1:], direction_to_look, (position_to_look[0] + 1, position_to_look[1] - 1))
            elif direction_to_look == 2:
                return continueSearch(grid, letters_to_find[1:], direction_to_look, (position_to_look[0] + 1, position_to_look[1]))
            elif direction_to_look == 3:
                return continueSearch(grid, letters_to_find[1:], direction_to_look, (position_to_look[0] + 1, position_to_look[1] + 1))
            elif direction_to_look == 4:
                return continueSearch(grid, letters_to_find[1:], direction_to_look, (position_to_look[0], position_to_look[1] + 1))
            elif direction_to_look == 5:
                return continueSearch(grid, letters_to_find[1:], direction_to_look, (position_to_look[0] - 1, position_to_look[1] + 1))
            elif direction_to_look == 6:
                return continueSearch(grid, letters_to_find[1:], direction_to_look, (position_to_look[0] - 1, position_to_look[1]))
            elif direction_to_look == 7:
                return continueSearch(grid, letters_to_find[1:], direction_to_look, (position_to_look[0] - 1, position_to_look[1] - 1))

    total = 0
    for pos in search_pos:
        if continueSearch(grid, ["X", "M", "A", "S"], 0, pos):
            total += 1
        if continueSearch(grid, ["X", "M", "A", "S"], 1, pos):
            total += 1
        if continueSearch(grid, ["X", "M", "A", "S"], 2, pos):
            total += 1
        if continueSearch(grid, ["X", "M", "A", "S"], 3, pos):
            total += 1
        if continueSearch(grid, ["X", "M", "A", "S"], 4, pos):
            total += 1
        if continueSearch(grid, ["X", "M", "A", "S"], 5, pos):
            total += 1
        if continueSearch(grid, ["X", "M", "A", "S"], 6, pos):
            total += 1
        if continueSearch(grid, ["X", "M", "A", "S"], 7, pos):
            total += 1

    return total

def part2():
    global all_lines
    line_no = 0

    grid = []

    while line_no != len(all_lines):
        line = all_lines[line_no]

        grid.append([i for i in line])

        line_no += 1

    # Go through and find all the X's
    search_pos = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "A":
                search_pos.append((x, y))

    # Go through each search pos and look in each direction
    def search(grid: list, position_to_look: tuple) -> bool:
        try:
            if position_to_look[0] == 0 or position_to_look[1] == 0:
                return False
            grid[position_to_look[1]+1][position_to_look[0]+1]
        except:
            return False

        # Check if center is an A
        if grid[position_to_look[1]][position_to_look[0]] == "A":
            total_valid = 0

            # Check if a corner is an M and other corner is an S
            if grid[position_to_look[1] - 1][position_to_look[0] - 1] == "M" and grid[position_to_look[1] + 1][position_to_look[0] + 1] == "S":
                total_valid += 1
            elif grid[position_to_look[1] - 1][position_to_look[0] - 1] == "S" and grid[position_to_look[1] + 1][position_to_look[0] + 1] == "M":
                total_valid += 1

            # Check the other corner
            if grid[position_to_look[1] - 1][position_to_look[0] + 1] == "M" and grid[position_to_look[1] + 1][position_to_look[0] - 1] == "S":
                total_valid += 1
            elif grid[position_to_look[1] - 1][position_to_look[0] + 1] == "S" and grid[position_to_look[1] + 1][position_to_look[0] - 1] == "M":
                total_valid += 1

            if total_valid == 2:
                return True

        return False

    total = 0
    for pos in search_pos:
        if search(grid, pos):
            total += 1

    return total

print('Part 1 answer:', part1())
print('Part 2 answer:', part2())
