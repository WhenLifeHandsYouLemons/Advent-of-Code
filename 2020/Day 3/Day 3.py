"""
Advent of Code: Day 3
"""

all_lines = []

with open("C:/Users/2005s/Documents/Visual Studio Code/Advent-of-Code-2020/Day 3/Day 3 Resources.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)
print(all_lines)

spaces_in_current_line = []
max_in_1_line = len(all_lines[0])
tree_counter = 0

# Increment for moving right and down
# Just incase it needs to be changed ;) (Who knows!)
right = 3
down = 1
rollover_no = max_in_1_line - right + 1

# Starting point for right and down
in_line_pos = 1
current_line = 1

# Calculation
while current_line < len(all_lines):
    # Counting to the right
    in_line_pos = in_line_pos + right
    print(f"current inline pos {in_line_pos}")

    # Rollover; For when the counter for moving right gets to the maximum number.
    if in_line_pos >= rollover_no:
        # Reset counter
        in_line_pos = in_line_pos - max_in_1_line

        # Only printing positive values
        if in_line_pos > 0:
            print(f"current inline pos {in_line_pos}")

    # Counting downwards
    current_line = current_line + down
    print(f"current line {current_line}")

    for space in all_lines[current_line-1]:
        spaces_in_current_line.append(space)
    print(f"current spaces list {spaces_in_current_line}")

    if spaces_in_current_line[in_line_pos-1] == "#":
        tree_counter = tree_counter + 1

    print(f"tree counter {tree_counter}")

    spaces_in_current_line = []

print(f"You will encounter {tree_counter} trees.")
