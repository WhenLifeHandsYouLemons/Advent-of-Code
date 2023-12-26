"""
Advent of Code: Day 11
"""
all_lines = []

with open('2023/Day 11/data.txt', 'r') as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)

def part1():
    global all_lines
    image = [[space for space in row] for row in all_lines]

    # Rotate the image to find columns with no galaxies
    rotated_iamge = list(zip(*image[::-1]))
    temp = []
    for line in rotated_iamge:
        temp.append(list(line))
    rotated_iamge = temp.copy()
    temp.clear()

    # Store positions of all rows and columns with no galaxies
    empty_rows = []
    empty_columns = []
    for row_no in range(len(image)):
        if "#" not in image[row_no]:
            empty_rows.append(row_no)

    for column_no in range(len(rotated_iamge)):
        if "#" not in rotated_iamge[column_no]:
            empty_columns.append(column_no)

    # Add an extra column to all the column which are only space
    expanded_image = []
    for row_no in range(len(image)):
        row = image[row_no]
        temp = []
        for column_no in range(len(row)):
            space = row[column_no]
            # Add an extra space to the place where it's an empty column
            if column_no in empty_columns:
                temp.append(space)
                temp.append(space)
            else:
                temp.append(space)
        expanded_image.append(temp)

    # Add an extra row to all empty rows
    adder = 0
    for empty_row in empty_rows:
        expanded_image.insert(empty_row+adder, expanded_image[empty_row+adder])
        adder += 1

    # Find every galaxy position
    galaxies = []
    for row in range(len(expanded_image)):
        for column in range(len(expanded_image[row])):
            if expanded_image[row][column] == "#":
                galaxies.append((column, row))

    distances = []
    i = 0
    while i < len(galaxies):
        j = i+1
        while j < len(galaxies):
            distance = abs(galaxies[j][0] - galaxies[i][0]) + abs(galaxies[j][1] - galaxies[i][1])
            distances.append(distance)

            j += 1
        i += 1

    print(sum(distances))

def part2():
    global all_lines
    image = [[space for space in row] for row in all_lines]

    # Rotate the image to find columns with no galaxies
    rotated_iamge = list(zip(*image[::-1]))
    temp = []
    for line in rotated_iamge:
        temp.append(list(line))
    rotated_iamge = temp.copy()
    temp.clear()

    # Store positions of all rows and columns with no galaxies
    empty_rows = []
    empty_columns = []
    for row_no in range(len(image)):
        if "#" not in image[row_no]:
            empty_rows.append(row_no)

    for column_no in range(len(rotated_iamge)):
        if "#" not in rotated_iamge[column_no]:
            empty_columns.append(column_no)

    expansion_factor = 1000000

    # Add an extra column to all the column which are only space
    expanded_image = []
    for row_no in range(len(image)):
        row = image[row_no]
        temp = []
        for column_no in range(len(row)):
            space = row[column_no]
            # Add an extra space to the place where it's an empty column
            if column_no in empty_columns:
                for i in range(expansion_factor):
                    temp.append(space)
            else:
                temp.append(space)
        expanded_image.append(temp)

    # Add an extra row to all empty rows
    adder = 0
    for empty_row in empty_rows:
        for i in range(expansion_factor-1):
            expanded_image.insert(empty_row+adder, expanded_image[empty_row+adder])
        adder += expansion_factor-1

    # Find every galaxy position
    galaxies = []
    for row in range(len(expanded_image)):
        for column in range(len(expanded_image[row])):
            if expanded_image[row][column] == "#":
                galaxies.append((column, row))

    distances = []
    i = 0
    while i < len(galaxies):
        j = i+1
        while j < len(galaxies):
            distance = abs(galaxies[j][0] - galaxies[i][0]) + abs(galaxies[j][1] - galaxies[i][1])
            distances.append(distance)

            j += 1
        i += 1

    print(sum(distances))

part1()
part2()
