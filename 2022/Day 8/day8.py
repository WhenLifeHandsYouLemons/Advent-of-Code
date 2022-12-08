"""
Advent of Code: Day 8
"""

tree_grid = []
with open("2022/Day 8/data.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()

    for line in lines:
        temp_array = []
        for char in line:
            temp_array.append(int(char))
        tree_grid.append(temp_array)


# Go through each row
scenic_score = []
row_no = 0
while row_no != len(tree_grid):
    column_no = 0
    temp_scenic = []

    while column_no != len(tree_grid[row_no]):

        hidden = True
        # Check left
        check_column = column_no-1
        total_visible_left = 0
        while check_column >= 0 and hidden is True:
            if tree_grid[row_no][check_column] < tree_grid[row_no][column_no]:
                total_visible_left += 1
            elif tree_grid[row_no][check_column] >= tree_grid[row_no][column_no]:
                total_visible_left += 1
                hidden = False
            check_column -= 1
        # Check right
        hidden = True
        check_column = column_no+1
        total_visible_right = 0
        while check_column != len(tree_grid[row_no]) and hidden is True:
            if tree_grid[row_no][check_column] < tree_grid[row_no][column_no]:
                total_visible_right += 1
            elif tree_grid[row_no][check_column] >= tree_grid[row_no][column_no]:
                total_visible_right += 1
                hidden = False
            check_column += 1
        # Check up
        hidden = True
        check_row = row_no-1
        total_visible_up = 0
        while check_row >= 0 and hidden is True:
            if tree_grid[check_row][column_no] < tree_grid[row_no][column_no]:
                total_visible_up += 1
            elif tree_grid[check_row][column_no] >= tree_grid[row_no][column_no]:
                total_visible_up += 1
                hidden = False
            check_row -= 1
        # Check down
        hidden = True
        check_row = row_no+1
        total_visible_down = 0
        while check_row != len(tree_grid) and hidden is True:
            if tree_grid[check_row][column_no] < tree_grid[row_no][column_no]:
                total_visible_down += 1
            elif tree_grid[check_row][column_no] >= tree_grid[row_no][column_no]:
                total_visible_down += 1
                hidden = False
            check_row += 1

        temp_scenic.append(total_visible_up * total_visible_down * total_visible_left * total_visible_right)
        column_no += 1
    scenic_score.append(temp_scenic)
    row_no += 1

maxes = []
for row in scenic_score:
    maxes.append(max(row))

print(max(maxes))
