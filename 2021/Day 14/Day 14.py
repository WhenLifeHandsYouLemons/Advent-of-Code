"""
Advent of Code: Day 14
"""

all_lines = []

with open("C:/Users/2005s/Desktop/Advent-of-Code/2021/Day 14/Day 14 Resources.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)

def part_1():
    n = 0
    b = 0
    c = 0
    h = 0
    p = 0
    f = 0
    k = 0
    s = 0
    v = 0
    o = 0

    line_no = 2
    polymer = []
    new_polymer = []
    for element in all_lines[0]:
        polymer.append(element)

    new_polymer = polymer.copy()

    joins = []
    inserter = []

    while line_no != len(all_lines):
        current_line = all_lines[line_no]
        current_line = current_line.split(" -> ")
        joins.append(current_line[0])
        inserter.append(current_line[1])
        line_no = line_no + 1

    iteration = 0
    max_iterations = 40
    while iteration != max_iterations:
        # Go through the polymers list and see if any match
        polymer_no = len(polymer)-1
        while polymer_no != 0:
            # Go through the joins list and add any elements
            joins_no = 0
            while joins_no != len(joins):
                temp = joins[joins_no]
                current_join = []
                for element in temp:
                    current_join.append(element)
                # print(current_join)

                if polymer[polymer_no] == current_join[1] and polymer[polymer_no-1] == current_join[0]:
                    new_polymer.insert(polymer_no, inserter[joins_no])
                joins_no += 1
            polymer_no -= 1

        polymer = new_polymer.copy()
        iteration += 1

    # Go through and count which has the most
    for element in polymer:
        if element == "N":
            n += 1
        elif element == "B":
            b += 1
        elif element == "C":
            c += 1
        elif element == "H":
            h += 1
        elif element == "P":
            p += 1
        elif element == "F":
            f += 1
        elif element == "K":
            k += 1
        elif element == "S":
            s += 1
        elif element == "V":
            v += 1
        elif element == "O":
            o += 1

    all_element_values = []
    all_element_values.append(n)
    all_element_values.append(b)
    all_element_values.append(c)
    all_element_values.append(h)
    all_element_values.append(p)
    all_element_values.append(f)
    all_element_values.append(k)
    all_element_values.append(s)
    all_element_values.append(v)
    all_element_values.append(o)
    print(all_element_values)
    return (max(all_element_values) - min(all_element_values))

print("Part 1:", part_1())