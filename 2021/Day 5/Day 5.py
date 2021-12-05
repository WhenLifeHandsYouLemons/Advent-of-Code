"""
Advent of Code: Day 5
"""

all_lines = []
line_no = 0

with open("C:/Users/2005s/Desktop/Advent-of-Code/2021/Day 5/Day 5 Resources.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)
print(all_lines)

# Making the empty grid
grid = []
y = 0
total_y = 1000
total_x = 1000
while y < total_y:
    row = []
    x = 0
    while x < total_x:
        row.append(0)
        x = x + 1
    grid.append(row)
    y = y + 1

# Going through all the inputs
while line_no != len(all_lines):
    # Sorting the current input
    current_line = all_lines[line_no].split(" -> ")
    coord1 = current_line[0]
    coord2 = current_line[1]
    coord1 = coord1.split(",")
    coord2 = coord2.split(",")
    x1 = int(coord1[0])
    y1 = int(coord1[1])
    x2 = int(coord2[0])
    y2 = int(coord2[1])

    # Check if the current coords are a straight line
    if x1 == x2:
        # If it's a vertical line
        checking_y = True
        while checking_y == True:
            current_row = grid[y1]
            past_no = current_row[x1]
            current_row.pop(x1)
            current_row.insert(x1, past_no+1)
            if y1 == y2:
                checking_y = False
            elif y1 < y2:
                y1 = y1 + 1
            elif y1 > y2:
                y1 = y1 - 1
    elif y1 == y2:
        # If it's a horizontal line
        checking_x = True
        current_row = grid[y1]
        while checking_x == True:
            past_no = current_row[x1]
            current_row.pop(x1)
            current_row.insert(x1, past_no+1)
            if x1 == x2:
                checking_x = False
            elif x1 < x2:
                x1 = x1 + 1
            elif x1 > x2:
                x1 = x1 - 1
    # Coords are diagonals
    # else:
    #     checking = True
    #     while checking == True:
    #         current_row = grid[y1]
    #         past_no = current_row[x1]
    #         current_row.pop(x1)
    #         current_row.insert(x1, past_no+1)
    #         if y1 == y2 and x1 == x2:
    #             checking = False
    #         elif y1 < y2:
    #             y1 = y1 + 1
    #         elif y1 > y2:
    #             y1 = y1 - 1
    #         if x1 < x2:
    #             x1 = x1 + 1
    #         elif x1 > x2:
    #             x1 = x1 - 1

    line_no = line_no + 1

# Going through the grid and counting
threshold = 2
total_points = 0
a = 0
while a != total_y:
    current_row = grid[a]
    b = 0
    while b != total_x:
        current_no = current_row[b]
        if current_no >= threshold:
            total_points = total_points + 1
        b = b + 1
    a = a + 1

print(total_points)
