"""
Advent of Code: Day 14
"""

all_lines = []
line_no = 0

with open("2022/Day 14/data.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)

cave = []

x_min = 444-100
x_max = 504+100
y_min = 0 # rock=14
y_max = 161+2

# x_min = 494-10
# x_max = 503+10
# y_min = 0
# y_max = 9+2

for row in range(y_max-y_min+1):
    temp_array = []
    for column in range(x_max-x_min+1):
        temp_array.append(".")
    cave.append(temp_array)

# Set sand gen point
cave[0][500-x_min] = "+"
sand_x = 500-x_min
sand_y = 0

#    EXAMPLE INPUT:
#
#    494,0 -> 503,0 -> 503,4
#    503,9 -> 494,9 -> 494,5 -> 500,5
#
#    SHOULD OUTPUT:
#
#      4     5  5
#      9     0  0
#      4     0  3
#    0 ##########
#    1 .........#
#    2 .........#
#    3 .........#
#    4 .........#
#    5 #######...
#    6 #.........
#    7 #.........
#    8 #.........
#    9 ##########

# Go through and add all the rocks
for rock_formation in all_lines:
    rock_coords = rock_formation.split(" -> ")
    i = 0
    while i != len(rock_coords)-1:
        start_coords = rock_coords[i].split(",")
        start_x = int(start_coords[0]) - x_min
        start_y = int(start_coords[1])
        end_coords = rock_coords[i + 1].split(",")
        end_x = int(end_coords[0]) - x_min
        end_y = int(end_coords[1])
        if start_x != end_x:
            if start_x > end_x:
                inc = -1
            else:
                inc = 1
            for a in range(start_x, end_x, inc):
                cave[end_y][a] = "#"
            cave[end_y][end_x] = "#"
        else:
            if start_y > end_y:
                inc = -1
            else:
                inc = 1
            for b in range(start_y, end_y, inc):
                cave[b][end_x] = "#"
            cave[end_y][end_x] = "#"
        i += 1

# Print out the cave with rocks
print()
for print_row in cave:
    print(print_row)

# Sand simulator
start_print = 0
possible = True
while possible is True:
    # Spawn sand
    cave[sand_y + 1][sand_x] = "o"

    fall_x = sand_x
    fall_y = sand_y

    # Simulate fall
    falling = True
    while falling is True:
        if fall_x == sand_x and fall_y == sand_y:
            changer = "+"
        else:
            changer = "."
        # Check down
        if cave[fall_y + 1][fall_x] == ".":
            cave[fall_y][fall_x] = changer
            fall_y += 1
            cave[fall_y][fall_x] = "o"
        # Check down left
        elif cave[fall_y + 1][fall_x - 1] == ".":
            cave[fall_y][fall_x] = changer
            fall_y += 1
            fall_x -= 1
            cave[fall_y][fall_x] = "o"
        # Check down right
        elif cave[fall_y + 1][fall_x + 1] == ".":
            cave[fall_y][fall_x] = changer
            fall_y += 1
            fall_x += 1
            cave[fall_y][fall_x] = "o"
        else:
            if changer == "+":
                possible = False
            falling = False

    # Print out the cave with rocks and sand
    if start_print >= 10000:
        print()
        for print_row in cave:
            print(print_row)
    start_print += 1

total = 0
for row in cave:
    for column in row:
        if column == "o":
            total += 1

print(total + 1)