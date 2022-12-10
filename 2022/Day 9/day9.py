"""
Advent of Code: Day 9
"""

all_lines = []
line_no = 0

grid = []
grid_size = 1000
for i in range(grid_size):
    temp_array = []
    for ii in range(grid_size):
        temp_array.append(".")
    grid.append(temp_array)
grid[len(grid)//2][len(grid[0])//2] = "H"

with open("2022/Day 9/data.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)

while line_no != len(all_lines):
    # If it's the first move
    if line_no == 0:
        # Check how many it moves by
        amount = int(all_lines[line_no].split(" ")[1])
        # Check which direction it moves in
        direction = all_lines[line_no].split(" ")[0]
        moved_once = False
        # If direction is up
        if direction == "U":
            # For each amount of moves upwards
            for i in range(amount):
                # If moved_once = False
                if moved_once == False:
                    # Find where the head is
                    h_row = -1
                    breaker = False
                    for i_row in grid:
                        h_column = 0
                        h_row += 1
                        for i_column in i_row:
                            if "H" in i_column:
                                breaker = True
                                break
                            else:
                                h_column += 1
                        if breaker is True:
                            break

                    # move it up
                    type = grid[h_row-1][h_column]
                    grid[h_row-1][h_column] = f"H {type}"
                    moved_once = True
                    # make the starting position into the tail
                    grid[h_row][h_column] = "T"
                else:
                    # store position of head (row and column)
                    h_row = -1
                    breaker = False
                    for i_row in grid:
                        h_column = 0
                        h_row += 1
                        for i_column in i_row:
                            if "H" in i_column:
                                breaker = True
                                break
                            else:
                                h_column += 1
                        if breaker is True:
                            break

                    # Find the tail
                    t_row = -1
                    breaker = False
                    found = False
                    for i_row in grid:
                        t_column = 0
                        t_row += 1
                        for i_column in i_row:
                            if i_column == "T":
                                breaker = True
                                found = True
                                break
                            else:
                                t_column += 1
                        if breaker is True:
                            break
                    if found is False:
                        t_column = h_column
                        t_row = h_row

                    # move up
                    type = grid[h_row-1][h_column]
                    grid[h_row-1][h_column] = f"H {type}"
                    if t_column == h_column and t_row == h_row:
                        grid[h_row][h_column] = "T"
                    else:
                        prev_type = grid[h_row][h_column].split(" ")[1]
                        grid[h_row][h_column] = f"{prev_type}"
                    directly_around = False

                    try:
                        # if head == up
                        if "H" in grid[t_row-1][t_column]:
                            directly_around = True
                        else:
                            raise NameError
                    except:
                        try:
                            # if head == down
                            if "H" in grid[t_row+1][t_column]:
                                directly_around = True
                            else:
                                raise NameError
                        except:
                            try:
                                # if head == right
                                if "H" in grid[t_row][t_column+1]:
                                    directly_around = True
                                else:
                                    raise NameError
                            except:
                                try:
                                    # if head == up right
                                    if "H" in grid[t_row-1][t_column+1]:
                                        directly_around = True
                                    else:
                                        raise NameError
                                except:
                                    try:
                                        # if head == down right
                                        if "H" in grid[t_row+1][t_column+1]:
                                            directly_around = True
                                        else:
                                            raise NameError
                                    except:
                                        try:
                                            # if head == inside
                                            if t_column == h_column and t_row == h_row-1:
                                                directly_around = True
                                            else:
                                                raise NameError
                                        except:
                                            if directly_around == False:
                                                # move tail to stored position
                                                grid[h_row][h_column] = "T"
                                                grid[t_row][t_column] = "#"
                    if directly_around == False:
                        # move tail to stored position
                        grid[h_row][h_column] = "T"
                        grid[t_row][t_column] = "#"
        # else if direction is right
        elif direction == "R":
            # For each amount of moves upwards
            for i in range(amount):
                # If moved_once = False
                if moved_once == False:
                    # Find where the head is
                    h_row = -1
                    breaker = False
                    for i_row in grid:
                        h_column = 0
                        h_row += 1
                        for i_column in i_row:
                            if "H" in i_column:
                                breaker = True
                                break
                            else:
                                h_column += 1
                        if breaker is True:
                            break

                    # move it right
                    type = grid[h_row][h_column+1]
                    grid[h_row][h_column+1] = f"H {type}"
                    moved_once = True
                    # make the starting position into the tail
                    grid[h_row][h_column] = "T"
                else:
                    # store position of head (row and column)
                    h_row = -1
                    breaker = False
                    for i_row in grid:
                        h_column = 0
                        h_row += 1
                        for i_column in i_row:
                            if "H" in i_column:
                                breaker = True
                                break
                            else:
                                h_column += 1
                        if breaker is True:
                            break

                    # Find the tail
                    t_row = -1
                    breaker = False
                    found = False
                    for i_row in grid:
                        t_column = 0
                        t_row += 1
                        for i_column in i_row:
                            if i_column == "T":
                                found = True
                                breaker = True
                                break
                            else:
                                t_column += 1
                        if breaker is True:
                            break
                    if found is False:
                        t_column = h_column
                        t_row = h_row

                    # move right
                    type = grid[h_row][h_column+1]
                    grid[h_row][h_column+1] = f"H {type}"
                    if t_column == h_column and t_row == h_row:
                        grid[h_row][h_column] = "T"
                    else:
                        prev_type = grid[h_row][h_column].split(" ")[1]
                        grid[h_row][h_column] = f"{prev_type}"
                    directly_around = False

                    # Check surrounding the tail
                    try:
                        # if head == left
                        if "H" in grid[t_row][t_column-1]:
                            directly_around = True
                        else:
                            raise NameError
                    except:
                        try:
                            # if head == up left
                            if "H" in grid[t_row-1][t_column-1]:
                                directly_around = True
                            else:
                                raise NameError
                        except:
                            try:
                                # if head == up
                                if "H" in grid[t_row-1][t_column]:
                                    directly_around = True
                                else:
                                    raise NameError
                            except:
                                try:
                                    # if head == right
                                    if "H" in grid[t_row][t_column+1]:
                                        directly_around = True
                                    else:
                                        raise NameError
                                except:
                                    try:
                                        # if head == up right
                                        if "H" in grid[t_row-1][t_column+1]:
                                            directly_around = True
                                        else:
                                            raise NameError
                                    except:
                                        try:
                                            # if head == inside
                                            if t_column == h_column+1 and t_row == h_row:
                                                directly_around = True
                                            else:
                                                raise NameError
                                        except:
                                            if directly_around == False:
                                                # move tail to stored position
                                                grid[h_row][h_column] = "T"
                                                grid[t_row][t_column] = "#"

                    if directly_around == False:
                        # move tail to stored position
                        grid[h_row][h_column] = "T"
                        grid[t_row][t_column] = "#"
    # If it's not the first move
    else:
        # Check how many it moves by
        amount = int(all_lines[line_no].split(" ")[1])
        # Check which direction it moves in
        direction = all_lines[line_no].split(" ")[0]
        # If direction is up
        if direction == "U":
            # For each amount of moves upwards
            for i in range(amount):
                # store position of head (row and column)
                h_row = -1
                breaker = False
                for i_row in grid:
                    h_column = 0
                    h_row += 1
                    for i_column in i_row:
                        if "H" in i_column:
                            breaker = True
                            break
                        else:
                            h_column += 1
                    if breaker is True:
                        break

                # Find the tail
                t_row = -1
                breaker = False
                found = False
                for i_row in grid:
                    t_column = 0
                    t_row += 1
                    for i_column in i_row:
                        if i_column == "T":
                            found = True
                            breaker = True
                            break
                        else:
                            t_column += 1
                    if breaker is True:
                        break
                if found is False:
                    t_column = h_column
                    t_row = h_row

                # move up
                type = grid[h_row-1][h_column]
                grid[h_row-1][h_column] = f"H {type}"
                if t_column == h_column and t_row == h_row:
                    grid[h_row][h_column] = "T"
                else:
                    prev_type = grid[h_row][h_column].split(" ")[1]
                    grid[h_row][h_column] = f"{prev_type}"
                directly_around = False


                try:
                    # if head == left
                    if "H" in grid[t_row][t_column-1]:
                        directly_around = True
                    else:
                        raise NameError
                except:
                    try:
                        # if head == down left
                        if "H" in grid[t_row+1][t_column-1]:
                            directly_around = True
                        else:
                            raise NameError
                    except:
                        try:
                            # if head == up left
                            if "H" in grid[t_row-1][t_column-1]:
                                directly_around = True
                            else:
                                raise NameError
                        except:
                            try:
                                # if head == up
                                if "H" in grid[t_row-1][t_column]:
                                    directly_around = True
                                else:
                                    raise NameError
                            except:
                                try:
                                    # if head == down
                                    if "H" in grid[t_row+1][t_column]:
                                        directly_around = True
                                    else:
                                        raise NameError
                                except:
                                    try:
                                        # if head == right
                                        if "H" in grid[t_row][t_column+1]:
                                            directly_around = True
                                        else:
                                            raise NameError
                                    except:
                                        try:
                                            # if head == up right
                                            if "H" in grid[t_row-1][t_column+1]:
                                                directly_around = True
                                            else:
                                                raise NameError
                                        except:
                                            try:
                                                # if head == down right
                                                if "H" in grid[t_row+1][t_column+1]:
                                                    directly_around = True
                                                else:
                                                    raise NameError
                                            except:
                                                try:
                                                    # if head == inside
                                                    if t_column == h_column and t_row == h_row-1:
                                                        directly_around = True
                                                    else:
                                                        raise NameError
                                                except:
                                                    if directly_around == False:
                                                        # move tail to stored position
                                                        grid[h_row][h_column] = "T"
                                                        grid[t_row][t_column] = "#"

                if directly_around == False:
                    # move tail to stored position
                    grid[h_row][h_column] = "T"
                    grid[t_row][t_column] = "#"
        # If direction is down
        elif direction == "D":
            # For each amount of moves downwards
            for i in range(amount):
                # store position of head (row and column)
                h_row = -1
                breaker = False
                for i_row in grid:
                    h_column = 0
                    h_row += 1
                    for i_column in i_row:
                        if "H" in i_column:
                            breaker = True
                            break
                        else:
                            h_column += 1
                    if breaker is True:
                        break

                # Find the tail
                t_row = -1
                found = False
                breaker = False
                for i_row in grid:
                    t_column = 0
                    t_row += 1
                    for i_column in i_row:
                        if i_column == "T":
                            found = True
                            breaker = True
                            break
                        else:
                            t_column += 1
                    if breaker is True:
                        break
                if found is False:
                    t_column = h_column
                    t_row = h_row

                # move down
                type = grid[h_row+1][h_column]
                grid[h_row+1][h_column] = f"H {type}"
                if t_column == h_column and t_row == h_row:
                    grid[h_row][h_column] = "T"
                else:
                    prev_type = grid[h_row][h_column].split(" ")[1]
                    grid[h_row][h_column] = f"{prev_type}"
                directly_around = False


                try:
                    # if head == left
                    if "H" in grid[t_row][t_column-1]:
                        directly_around = True
                    else:
                        raise NameError
                except:
                    try:
                        # if head == down left
                        if "H" in grid[t_row+1][t_column-1]:
                            directly_around = True
                        else:
                            raise NameError
                    except:
                        try:
                            # if head == up left
                            if "H" in grid[t_row-1][t_column-1]:
                                directly_around = True
                            else:
                                raise NameError
                        except:
                            try:
                                # if head == up
                                if "H" in grid[t_row-1][t_column]:
                                    directly_around = True
                                else:
                                    raise NameError
                            except:
                                try:
                                    # if head == down
                                    if "H" in grid[t_row+1][t_column]:
                                        directly_around = True
                                    else:
                                        raise NameError
                                except:
                                    try:
                                        # if head == right
                                        if "H" in grid[t_row][t_column+1]:
                                            directly_around = True
                                        else:
                                            raise NameError
                                    except:
                                        try:
                                            # if head == up right
                                            if "H" in grid[t_row-1][t_column+1]:
                                                directly_around = True
                                            else:
                                                raise NameError
                                        except:
                                            try:
                                                # if head == down right
                                                if "H" in grid[t_row+1][t_column+1]:
                                                    directly_around = True
                                                else:
                                                    raise NameError
                                            except:
                                                try:
                                                    # if head == inside
                                                    if t_column == h_column and t_row == h_row+1:
                                                        directly_around = True
                                                    else:
                                                        raise NameError
                                                except:
                                                    if directly_around == False:
                                                        # move tail to stored position
                                                        grid[h_row][h_column] = "T"
                                                        grid[t_row][t_column] = "#"

                if directly_around == False:
                    # move tail to stored position
                    grid[h_row][h_column] = "T"
                    grid[t_row][t_column] = "#"
        # If direction is left
        elif direction == "L":
            # For each amount of moves left
            for i in range(amount):
                # store position of head (row and column)
                h_row = -1
                breaker = False
                for i_row in grid:
                    h_column = 0
                    h_row += 1
                    for i_column in i_row:
                        if "H" in i_column:
                            breaker = True
                            break
                        else:
                            h_column += 1
                    if breaker is True:
                        break

                # Find the tail
                t_row = -1
                breaker = False
                found = False
                for i_row in grid:
                    t_column = 0
                    t_row += 1
                    for i_column in i_row:
                        if i_column == "T":
                            breaker = True
                            found = True
                            break
                        else:
                            t_column += 1
                    if breaker is True:
                        break
                if found is False:
                    t_column = h_column
                    t_row = h_row

                # move left
                type = grid[h_row][h_column-1]
                grid[h_row][h_column-1] = f"H {type}"
                if t_column == h_column and t_row == h_row:
                    grid[h_row][h_column] = "T"
                else:
                    prev_type = grid[h_row][h_column].split(" ")[1]
                    grid[h_row][h_column] = f"{prev_type}"
                directly_around = False


                try:
                    # if head == left
                    if "H" in grid[t_row][t_column-1]:
                        directly_around = True
                    else:
                        raise NameError
                except:
                    try:
                        # if head == down left
                        if "H" in grid[t_row+1][t_column-1]:
                            directly_around = True
                        else:
                            raise NameError
                    except:
                        try:
                            # if head == up left
                            if "H" in grid[t_row-1][t_column-1]:
                                directly_around = True
                            else:
                                raise NameError
                        except:
                            try:
                                # if head == up
                                if "H" in grid[t_row-1][t_column]:
                                    directly_around = True
                                else:
                                    raise NameError
                            except:
                                try:
                                    # if head == down
                                    if "H" in grid[t_row+1][t_column]:
                                        directly_around = True
                                    else:
                                        raise NameError
                                except:
                                    try:
                                        # if head == right
                                        if "H" in grid[t_row][t_column+1]:
                                            directly_around = True
                                        else:
                                            raise NameError
                                    except:
                                        try:
                                            # if head == up right
                                            if "H" in grid[t_row-1][t_column+1]:
                                                directly_around = True
                                            else:
                                                raise NameError
                                        except:
                                            try:
                                                # if head == down right
                                                if "H" in grid[t_row+1][t_column+1]:
                                                    directly_around = True
                                                else:
                                                    raise NameError
                                            except:
                                                try:
                                                    # if head == inside
                                                    if t_column == h_column-1 and t_row == h_row:
                                                        directly_around = True
                                                    else:
                                                        raise NameError
                                                except:
                                                    if directly_around == False:
                                                        # move tail to stored position
                                                        grid[h_row][h_column] = "T"
                                                        grid[t_row][t_column] = "#"

                if directly_around == False:
                    # move tail to stored position
                    grid[h_row][h_column] = "T"
                    grid[t_row][t_column] = "#"
        # If direction is right
        elif direction == "R":
            # For each amount of moves right
            for i in range(amount):
                # store position of head (row and column)
                h_row = -1
                breaker = False
                for i_row in grid:
                    h_column = 0
                    h_row += 1
                    for i_column in i_row:
                        if "H" in i_column:
                            breaker = True
                            break
                        else:
                            h_column += 1
                    if breaker is True:
                        break

                # Find the tail
                t_row = -1
                breaker = False
                found = False
                for i_row in grid:
                    t_column = 0
                    t_row += 1
                    for i_column in i_row:
                        if i_column == "T":
                            found = True
                            breaker = True
                            break
                        else:
                            t_column += 1
                    if breaker is True:
                        break
                if found is False:
                    t_column = h_column
                    t_row = h_row

                # move right
                type = grid[h_row][h_column+1]
                grid[h_row][h_column+1] = f"H {type}"
                if t_column == h_column and t_row == h_row:
                    grid[h_row][h_column] = "T"
                else:
                    prev_type = grid[h_row][h_column].split(" ")[1]
                    grid[h_row][h_column] = f"{prev_type}"
                directly_around = False


                try:
                    # if head == left
                    if "H" in grid[t_row][t_column-1]:
                        directly_around = True
                    else:
                        raise NameError
                except:
                    try:
                        # if head == down left
                        if "H" in grid[t_row+1][t_column-1]:
                            directly_around = True
                        else:
                            raise NameError
                    except:
                        try:
                            # if head == up left
                            if "H" in grid[t_row-1][t_column-1]:
                                directly_around = True
                            else:
                                raise NameError
                        except:
                            try:
                                # if head == up
                                if "H" in grid[t_row-1][t_column]:
                                    directly_around = True
                                else:
                                    raise NameError
                            except:
                                try:
                                    # if head == down
                                    if "H" in grid[t_row+1][t_column]:
                                        directly_around = True
                                    else:
                                        raise NameError
                                except:
                                    try:
                                        # if head == right
                                        if "H" in grid[t_row][t_column+1]:
                                            directly_around = True
                                        else:
                                            raise NameError
                                    except:
                                        try:
                                            # if head == up right
                                            if "H" in grid[t_row-1][t_column+1]:
                                                directly_around = True
                                            else:
                                                raise NameError
                                        except:
                                            try:
                                                # if head == down right
                                                if "H" in grid[t_row+1][t_column+1]:
                                                    directly_around = True
                                                else:
                                                    raise NameError
                                            except:
                                                try:
                                                    # if head == inside
                                                    if t_column == h_column+1 and t_row == h_row:
                                                        directly_around = True
                                                    else:
                                                        raise NameError
                                                except:
                                                    if directly_around == False:
                                                        # move tail to stored position
                                                        grid[h_row][h_column] = "T"
                                                        grid[t_row][t_column] = "#"

                if directly_around == False:
                    # move tail to stored position
                    grid[h_row][h_column] = "T"
                    grid[t_row][t_column] = "#"

    line_no += 1
    print(line_no, len(all_lines))

for row in grid:
    print(row)

total = 0
for row in grid:
    for column in row:
        if "#" in column or "T" in column:
            total += 1

print(total)
