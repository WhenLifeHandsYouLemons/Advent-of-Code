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
waypoint_position_leftright = 10
waypoint_position_updown = 1
current_direction = east
current_line = ""
split_current_line = []
current_direction_need = ""
current_number = 0
current_position_leftright = 0
current_position_updown = 0
temp = 0

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

    # If waypoint is top left
    if waypoint_position_leftright <= 0 and waypoint_position_updown >= 0:
        # If command is turn left
        if current_direction_need == left:
            # If turn is 90 degrees
            if current_number == 90:
                temp = waypoint_position_leftright
                waypoint_position_leftright = waypoint_position_updown * -1
                waypoint_position_updown = temp
                temp = 0
                print(f"The waypoint turned left 90 degrees to ({waypoint_position_leftright}, {waypoint_position_updown})")
            # If turn is 180 degrees
            elif current_number == 180:
                waypoint_position_leftright = waypoint_position_leftright * -1
                waypoint_position_updown = waypoint_position_updown * -1
                print(f"The waypoint turned left 180 degrees to ({waypoint_position_leftright}, {waypoint_position_updown})")
            # If turn is 270 degrees
            elif current_number == 270:
                temp = waypoint_position_leftright * -1
                waypoint_position_leftright = waypoint_position_updown
                waypoint_position_updown = temp
                temp = 0
                print(f"The waypoint turned left 270 degrees to ({waypoint_position_leftright}, {waypoint_position_updown})")
        # If command is turn right
        elif current_direction_need == right:
            # If turn is 90 degrees
            if current_number == 90:
                temp = waypoint_position_leftright * -1
                waypoint_position_leftright = waypoint_position_updown
                waypoint_position_updown = temp
                temp = 0
                print(f"The waypoint turned right 90 degrees to ({waypoint_position_leftright}, {waypoint_position_updown})")
            # If turn is 180 degrees
            elif current_number == 180:
                waypoint_position_leftright = waypoint_position_leftright * -1
                waypoint_position_updown = waypoint_position_updown * -1
                print(f"The waypoint turned right 180 degrees to ({waypoint_position_leftright}, {waypoint_position_updown})")
            # If turn is 270 degrees
            elif current_number == 270:
                temp = waypoint_position_leftright
                waypoint_position_leftright = waypoint_position_updown * -1
                waypoint_position_updown = temp
                temp = 0
                print(f"The waypoint turned right 270 degrees to ({waypoint_position_leftright}, {waypoint_position_updown})")
    # If waypoint is top right
    elif waypoint_position_leftright >= 0 and waypoint_position_updown >= 0:
        # If command is turn left
        if current_direction_need == left:
            # If turn is 90 degrees
            if current_number == 90:
                temp = waypoint_position_leftright
                waypoint_position_leftright = waypoint_position_updown * -1
                waypoint_position_updown = temp
                temp = 0
                print(f"The waypoint turned left 90 degrees to ({waypoint_position_leftright}, {waypoint_position_updown})")
            # If turn is 180 degrees
            elif current_number == 180:
                waypoint_position_leftright = waypoint_position_leftright * -1
                waypoint_position_updown = waypoint_position_updown * -1
                print(f"The waypoint turned left 180 degrees to ({waypoint_position_leftright}, {waypoint_position_updown})")
            # If turn is 270 degrees
            elif current_number == 270:
                temp = waypoint_position_leftright * -1
                waypoint_position_leftright = waypoint_position_updown
                waypoint_position_updown = temp
                temp = 0
                print(f"The waypoint turned left 270 degrees to ({waypoint_position_leftright}, {waypoint_position_updown})")
        # If command is turn right
        elif current_direction_need == right:
            # If turn is 90 degrees
            if current_number == 90:
                temp = waypoint_position_leftright * -1
                waypoint_position_leftright = waypoint_position_updown
                waypoint_position_updown = temp
                temp = 0
                print(f"The waypoint turned right 90 degrees to ({waypoint_position_leftright}, {waypoint_position_updown})")
            # If turn is 180 degrees
            elif current_number == 180:
                waypoint_position_leftright = waypoint_position_leftright * -1
                waypoint_position_updown = waypoint_position_updown * -1
                print(f"The waypoint turned right 180 degrees to ({waypoint_position_leftright}, {waypoint_position_updown})")
            # If turn is 270 degrees
            elif current_number == 270:
                temp = waypoint_position_leftright
                waypoint_position_leftright = waypoint_position_updown * -1
                waypoint_position_updown = temp
                temp = 0
                print(f"The waypoint turned right 270 degrees to ({waypoint_position_leftright}, {waypoint_position_updown})")
    # If waypoint is bottom left
    elif waypoint_position_leftright <= 0 and waypoint_position_updown <= 0:
        # If command is turn left
        if current_direction_need == left:
            # If turn is 90 degrees
            if current_number == 90:
                temp = waypoint_position_leftright
                waypoint_position_leftright = waypoint_position_updown * -1
                waypoint_position_updown = temp
                temp = 0
                print(f"The waypoint turned left 90 degrees to ({waypoint_position_leftright}, {waypoint_position_updown})")
            # If turn is 180 degrees
            elif current_number == 180:
                waypoint_position_leftright = waypoint_position_leftright * -1
                waypoint_position_updown = waypoint_position_updown * -1
                print(f"The waypoint turned left 180 degrees to ({waypoint_position_leftright}, {waypoint_position_updown})")
            # If turn is 270 degrees
            elif current_number == 270:
                temp = waypoint_position_leftright * -1
                waypoint_position_leftright = waypoint_position_updown
                waypoint_position_updown = temp
                temp = 0
                print(f"The waypoint turned left 270 degrees to ({waypoint_position_leftright}, {waypoint_position_updown})")
        # If command is turn right
        elif current_direction_need == right:
            # If turn is 90 degrees
            if current_number == 90:
                temp = waypoint_position_leftright * -1
                waypoint_position_leftright = waypoint_position_updown
                waypoint_position_updown = temp
                temp = 0
                print(f"The waypoint turned right 90 degrees to ({waypoint_position_leftright}, {waypoint_position_updown})")
            # If turn is 180 degrees
            elif current_number == 180:
                waypoint_position_leftright = waypoint_position_leftright * -1
                waypoint_position_updown = waypoint_position_updown * -1
                print(f"The waypoint turned right 180 degrees to ({waypoint_position_leftright}, {waypoint_position_updown})")
            # If turn is 270 degrees
            elif current_number == 270:
                temp = waypoint_position_leftright
                waypoint_position_leftright = waypoint_position_updown * -1
                waypoint_position_updown = temp
                temp = 0
                print(f"The waypoint turned right 270 degrees to ({waypoint_position_leftright}, {waypoint_position_updown})")
    # If waypoint is bottom right
    elif waypoint_position_leftright >= 0 and waypoint_position_updown <= 0:
        # If command is turn left
        if current_direction_need == left:
            # If turn is 90 degrees
            if current_number == 90:
                temp = waypoint_position_leftright
                waypoint_position_leftright = waypoint_position_updown * -1
                waypoint_position_updown = temp
                temp = 0
                print(f"The waypoint turned left 90 degrees to ({waypoint_position_leftright}, {waypoint_position_updown})")
            # If turn is 180 degrees
            elif current_number == 180:
                waypoint_position_leftright = waypoint_position_leftright * -1
                waypoint_position_updown = waypoint_position_updown * -1
                print(f"The waypoint turned left 180 degrees to ({waypoint_position_leftright}, {waypoint_position_updown})")
            # If turn is 270 degrees
            elif current_number == 270:
                temp = waypoint_position_leftright * -1
                waypoint_position_leftright = waypoint_position_updown
                waypoint_position_updown = temp
                temp = 0
                print(f"The waypoint turned left 270 degrees to ({waypoint_position_leftright}, {waypoint_position_updown})")
        # If command is turn right
        elif current_direction_need == right:
            # If turn is 90 degrees
            if current_number == 90:
                temp = waypoint_position_leftright * -1
                waypoint_position_leftright = waypoint_position_updown
                waypoint_position_updown = temp
                temp = 0
                print(f"The waypoint turned right 90 degrees to ({waypoint_position_leftright}, {waypoint_position_updown})")
            # If turn is 180 degrees
            elif current_number == 180:
                waypoint_position_leftright = waypoint_position_leftright * -1
                waypoint_position_updown = waypoint_position_updown * -1
                print(f"The waypoint turned right 180 degrees to ({waypoint_position_leftright}, {waypoint_position_updown})")
            # If turn is 270 degrees
            elif current_number == 270:
                temp = waypoint_position_leftright
                waypoint_position_leftright = waypoint_position_updown * -1
                waypoint_position_updown = temp
                temp = 0
                print(f"The waypoint turned right 270 degrees to ({waypoint_position_leftright}, {waypoint_position_updown})")

    if current_direction_need == forward:
        temp = 0
        while temp != current_number:
            print(current_number, temp)
            current_position_updown = current_position_updown + waypoint_position_updown
            current_position_leftright = current_position_leftright + waypoint_position_leftright
            temp = temp + 1
            print(f"Ship went forward to ({current_position_leftright}, {current_position_updown})")

    # If command is east
    if current_direction_need == "E":
        waypoint_position_leftright = waypoint_position_leftright + current_number
        print(f"Waypoint went East to {waypoint_position_leftright}")
    # If command is west
    elif current_direction_need == "W":
        waypoint_position_leftright = waypoint_position_leftright - current_number
        print(f"Waypoint went West to {waypoint_position_leftright}")
    # If command is north
    elif current_direction_need == "N":
        waypoint_position_updown = waypoint_position_updown + current_number
        print(f"Waypoint went North to {waypoint_position_updown}")
    # If command is south
    elif current_direction_need == "S":
        waypoint_position_updown = waypoint_position_updown - current_number
        print(f"Waypoint went South to {waypoint_position_updown}")

    line_no = line_no + 1

if current_position_leftright < 0:
    current_position_leftright = current_position_leftright * -1

if current_position_updown < 0:
    current_position_updown = current_position_updown * -1

manhattan_distance = current_position_updown + current_position_leftright

print(f"The final position is ({current_position_leftright}, {current_position_updown}).")
print(f"The ship's Manhattan distance is {manhattan_distance}")
