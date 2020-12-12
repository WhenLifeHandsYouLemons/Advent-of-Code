"""
Advent of Code: Day 12
"""

all_lines = []
line_no = 0
north = "N"
south = "S"
east = "E"
west = "W"
right = "R"
left = "L"
forward = "F"
starting_direction = east
current_direction = starting_direction
current_line = ""
split_current_line = []
current_direction_need = ""
current_number = 0
current_position_leftright = 0
current_position_updown = 0

with open("C:/Users/2005s/Documents/Visual Studio Code/Advent-of-Code-2020/Day 12/Day 12 Resources.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)
print(all_lines)

while line_no != len(all_lines):
    split_current_line = []
    current_line = all_lines[line_no]

    for command in current_line:
        split_current_line.append(command)

    current_direction_need = split_current_line[0]
    split_current_line.pop(0)
    current_number = int("".join(split_current_line))
    print(split_current_line, current_direction_need, current_number)

    # If ship is facing east
    if current_direction == east:
        # If command is turn left
        if current_direction_need == left:
            # If turn is 90 degrees
            if current_number == 90:
                current_direction = north
                print("Current direction is North")
            # If turn is 180 degrees
            elif current_number == 180:
                current_direction = west
                print("Current direction is West")
            # If turn is 270 degrees
            elif current_number == 270:
                current_direction = south
                print("Current direction is South")
        # If command is turn right
        elif current_direction_need == right:
            # If turn is 90 degrees
            if current_number == 90:
                current_direction = south
                print("Current direction is South")
            # If turn is 180 degrees
            elif current_number == 180:
                current_direction = west
                print("Current direction is West")
            # If turn is 270 degrees
            elif current_number == 270:
                current_direction = north
                print("Current direction is North")
        # If command is go forward
        elif current_direction_need == forward:
            current_position_leftright = current_position_leftright + current_number
            print(f"Ship went forward to {current_position_leftright}")
    # If ship is facing west
    elif current_direction == west:
        # If command is turn left
        if current_direction_need == left:
            # If turn is 90 degrees
            if current_number == 90:
                current_direction = south
                print("Current direction is South")
            # If turn is 180 degrees
            elif current_number == 180:
                current_direction = east
                print("Current direction is East")
            # If turn is 270 degrees
            elif current_number == 270:
                current_direction = north
                print("Current direction is North")
        # If command is turn right
        elif current_direction_need == right:
            # If turn is 90 degrees
            if current_number == 90:
                current_direction = north
                print("Current direction is North")
            # If turn is 180 degrees
            elif current_number == 180:
                current_direction = east
                print("Current direction is East")
            # If turn is 270 degrees
            elif current_number == 270:
                current_direction = south
                print("Current direction is South")
        # If command is go forward
        elif current_direction_need == forward:
            current_position_leftright = current_position_leftright - current_number
            print(f"Ship went forward to {current_position_leftright}")
    # If ship is facing north
    elif current_direction == north:
        # If command is turn left
        if current_direction_need == left:
            # If turn is 90 degrees
            if current_number == 90:
                current_direction = west
                print("Current direction is West")
            # If turn is 180 degrees
            elif current_number == 180:
                current_direction = south
                print("Current direction is South")
            # If turn is 270 degrees
            elif current_number == 270:
                current_direction = east
                print("Current direction is East")
        # If command is turn right
        elif current_direction_need == right:
            # If turn is 90 degrees
            if current_number == 90:
                current_direction = east
                print("Current direction is East")
            # If turn is 180 degrees
            elif current_number == 180:
                current_direction = south
                print("Current direction is South")
            # If turn is 270 degrees
            elif current_number == 270:
                current_direction = west
                print("Current direction is West")
        # If command is go forward
        elif current_direction_need == forward:
            current_position_updown = current_position_updown + current_number
            print(f"Ship went forward to {current_position_updown}")
    # If ship is facing south
    elif current_direction == south:
        # If command is turn left
        if current_direction_need == left:
            # If turn is 90 degrees
            if current_number == 90:
                current_direction = east
                print("Current direction is East")
            # If turn is 180 degrees
            elif current_number == 180:
                current_direction = north
                print("Current direction is North")
            # If turn is 270 degrees
            elif current_number == 270:
                current_direction = west
                print("Current direction is West")
        # If command is turn right
        elif current_direction_need == right:
            # If turn is 90 degrees
            if current_number == 90:
                current_direction = west
                print("Current direction is West")
            # If turn is 180 degrees
            elif current_number == 180:
                current_direction = north
                print("Current direction is North")
            # If turn is 270 degrees
            elif current_number == 270:
                current_direction = east
                print("Current direction is East")
        # If command is go forward
        elif current_direction_need == forward:
            current_position_updown = current_position_updown - current_number
            print(f"Ship went forward to {current_position_updown}")

    # If command is east
    if current_direction_need == "E":
        current_position_leftright = current_position_leftright + current_number
        print(f"Ship went East to {current_position_leftright}")
    # If command is west
    elif current_direction_need == "W":
        current_position_leftright = current_position_leftright - current_number
        print(f"Ship went West to {current_position_leftright}")
    # If command is north
    elif current_direction_need == "N":
        current_position_updown = current_position_updown + current_number
        print(f"Ship went North to {current_position_updown}")
    # If command is south
    elif current_direction_need == "S":
        current_position_updown = current_position_updown - current_number
        print(f"Ship went South to {current_position_updown}")

    line_no = line_no + 1

if current_position_leftright < 0:
    current_position_leftright = current_position_leftright * -1

if current_position_updown < 0:
    current_position_updown = current_position_updown * -1

manhattan_distance = current_position_updown + current_position_leftright

print(f"The final position is ({current_position_leftright}, {current_position_updown}).")
print(f"The ship's Manhattan distance is {manhattan_distance}")
