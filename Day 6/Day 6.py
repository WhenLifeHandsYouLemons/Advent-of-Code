"""
# Advent of Code: Day 6
"""

all_groups = []
current_group = ""
line_no = 0
letter_a = 0
letter_b = 0
letter_c = 0
letter_d = 0
letter_e = 0
letter_f = 0
letter_g = 0
letter_h = 0
letter_i = 0
letter_j = 0
letter_k = 0
letter_l = 0
letter_m = 0
letter_n = 0
letter_o = 0
letter_p = 0
letter_q = 0
letter_r = 0
letter_s = 0
letter_t = 0
letter_u = 0
letter_v = 0
letter_w = 0
letter_x = 0
letter_y = 0
letter_z = 0
count = 0
total_count = 0

with open("C:/Users/2005s/Documents/Visual Studio Code/Advent-of-Code-2020/Day 6/Day 6 Resources.txt", "r") as f:
    content = f.read()
    full = content
    all_groups = full.split("\n\n")

print(all_groups)
total = len(all_groups)
while line_no != total:
    replacing = all_groups[0].replace("\n", " ")
    all_groups.append(replacing)
    all_groups.pop(0)

    replacing = ""
    line_no = line_no + 1
print(all_groups)

line_no = 0
while line_no != len(all_groups):
    current_group = all_groups[line_no]
    
    letter_a = 0
    letter_b = 0
    letter_c = 0
    letter_d = 0
    letter_e = 0
    letter_f = 0
    letter_g = 0
    letter_h = 0
    letter_i = 0
    letter_j = 0
    letter_k = 0
    letter_l = 0
    letter_m = 0
    letter_n = 0
    letter_o = 0
    letter_p = 0
    letter_q = 0
    letter_r = 0
    letter_s = 0
    letter_t = 0
    letter_u = 0
    letter_v = 0
    letter_w = 0
    letter_x = 0
    letter_y = 0
    letter_z = 0
    count = 0
    number_of_spaces = 0

    for letter in current_group:
        if letter == "a":
            letter_a = letter_a + 1
        elif letter == "b":
            letter_b = letter_b + 1
        elif letter == "c":
            letter_c = letter_c + 1
        elif letter == "d":
            letter_d = letter_d + 1
        elif letter == "e":
            letter_e = letter_e + 1
        elif letter == "f":
            letter_f = letter_f + 1
        elif letter == "g":
            letter_g = letter_g + 1
        elif letter == "h":
            letter_h = letter_h + 1
        elif letter == "i":
            letter_i = letter_i + 1
        elif letter == "j":
            letter_j = letter_j + 1
        elif letter == "k":
            letter_k = letter_k + 1
        elif letter == "l":
            letter_l = letter_l + 1
        elif letter == "m":
            letter_m = letter_m + 1
        elif letter == "n":
            letter_n = letter_n + 1
        elif letter == "o":
            letter_o = letter_o + 1
        elif letter == "p":
            letter_p = letter_p + 1
        elif letter == "q":
            letter_q = letter_q + 1
        elif letter == "r":
            letter_r = letter_r + 1
        elif letter == "s":
            letter_s = letter_s + 1
        elif letter == "t":
            letter_t = letter_t + 1
        elif letter == "u":
            letter_u = letter_u + 1
        elif letter == "v":
            letter_v = letter_v + 1
        elif letter == "w":
            letter_w = letter_w + 1
        elif letter == "x":
            letter_x = letter_x + 1
        elif letter == "y":
            letter_y = letter_y + 1
        elif letter == "z":
            letter_z = letter_z + 1
        elif letter == " ":
            number_of_spaces = number_of_spaces + 1

    number_of_spaces = number_of_spaces + 1
    print(f"Number of spaces: {number_of_spaces}")

    if letter_a != number_of_spaces:
        letter_a = 0
    else:
        letter_a = 1

    if letter_b != number_of_spaces:
        letter_b = 0
    else:
        letter_b = 1

    if letter_c != number_of_spaces:
        letter_c = 0
    else:
        letter_c = 1

    if letter_d != number_of_spaces:
        letter_d = 0
    else:
        letter_d = 1

    if letter_e != number_of_spaces:
        letter_e = 0
    else:
        letter_e = 1

    if letter_f != number_of_spaces:
        letter_f = 0
    else:
        letter_f = 1

    if letter_g != number_of_spaces:
        letter_g = 0
    else:
        letter_g = 1

    if letter_h != number_of_spaces:
        letter_h = 0
    else:
        letter_h = 1

    if letter_i != number_of_spaces:
        letter_i = 0
    else:
        letter_i = 1

    if letter_j != number_of_spaces:
        letter_j = 0
    else:
        letter_j = 1

    if letter_k != number_of_spaces:
        letter_k = 0
    else:
        letter_k = 1

    if letter_l != number_of_spaces:
        letter_l = 0
    else:
        letter_l = 1

    if letter_m != number_of_spaces:
        letter_m = 0
    else:
        letter_m = 1

    if letter_n != number_of_spaces:
        letter_n = 0
    else:
        letter_n = 1

    if letter_o != number_of_spaces:
        letter_o = 0
    else:
        letter_o = 1

    if letter_p != number_of_spaces:
        letter_p = 0
    else:
        letter_p = 1

    if letter_q != number_of_spaces:
        letter_q = 0
    else:
        letter_q = 1

    if letter_r != number_of_spaces:
        letter_r = 0
    else:
        letter_r = 1

    if letter_s != number_of_spaces:
        letter_s = 0
    else:
        letter_s = 1

    if letter_t != number_of_spaces:
        letter_t = 0
    else:
        letter_t = 1

    if letter_u != number_of_spaces:
        letter_u = 0
    else:
        letter_u = 1

    if letter_v != number_of_spaces:
        letter_v = 0
    else:
        letter_v = 1

    if letter_w != number_of_spaces:
        letter_w = 0
    else:
        letter_w = 1

    if letter_x != number_of_spaces:
        letter_x = 0
    else:
        letter_x = 1

    if letter_y != number_of_spaces:
        letter_y = 0
    else:
        letter_y = 1

    if letter_z != number_of_spaces:
        letter_z = 0
    else:
        letter_z = 1

    count = letter_a + letter_b + letter_c + letter_d + letter_e + letter_f + letter_g + letter_h + letter_i + letter_j + letter_k + letter_l + letter_m + letter_n + letter_o + letter_p + letter_q + letter_r + letter_s + letter_t + letter_u + letter_v + letter_w + letter_x + letter_y + letter_z
    total_count = total_count + count

    print(count)
    print(total_count)

    line_no = line_no + 1

print("")
print(f"The total count is {total_count}")
