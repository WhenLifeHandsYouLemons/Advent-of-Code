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

    for letter in current_group:
        if letter == "a":
            if letter_a == 0:
                letter_a = 1
        elif letter == "b":
            if letter_b == 0:
                letter_b = 1
        elif letter == "c":
            if letter_c == 0:
                letter_c = 1
        elif letter == "d":
            if letter_d == 0:
                letter_d = 1
        elif letter == "e":
            if letter_e == 0:
                letter_e = 1
        elif letter == "f":
            if letter_f == 0:
                letter_f = 1
        elif letter == "g":
            if letter_g == 0:
                letter_g = 1
        elif letter == "h":
            if letter_h == 0:
                letter_h = 1
        elif letter == "i":
            if letter_i == 0:
                letter_i = 1
        elif letter == "j":
            if letter_j == 0:
                letter_j = 1
        elif letter == "k":
            if letter_k == 0:
                letter_k = 1
        elif letter == "l":
            if letter_l == 0:
                letter_l = 1
        elif letter == "m":
            if letter_m == 0:
                letter_m = 1
        elif letter == "n":
            if letter_n == 0:
                letter_n = 1
        elif letter == "o":
            if letter_o == 0:
                letter_o = 1
        elif letter == "p":
            if letter_p == 0:
                letter_p = 1
        elif letter == "q":
            if letter_q == 0:
                letter_q = 1
        elif letter == "r":
            if letter_r == 0:
                letter_r = 1
        elif letter == "s":
            if letter_s == 0:
                letter_s = 1
        elif letter == "t":
            if letter_t == 0:
                letter_t = 1
        elif letter == "u":
            if letter_u == 0:
                letter_u = 1
        elif letter == "v":
            if letter_v == 0:
                letter_v = 1
        elif letter == "w":
            if letter_w == 0:
                letter_w = 1
        elif letter == "x":
            if letter_x == 0:
                letter_x = 1
        elif letter == "y":
            if letter_y == 0:
                letter_y = 1
        elif letter == "z":
            if letter_z == 0:
                letter_z = 1

    count = letter_a + letter_b + letter_c + letter_d + letter_e + letter_f + letter_g + letter_h + letter_i + letter_j + letter_k + letter_l + letter_m + letter_n + letter_o + letter_p + letter_q + letter_r + letter_s + letter_t + letter_u + letter_v + letter_w + letter_x + letter_y + letter_z
    total_count = total_count + count

    print(count)
    print(total_count)

    line_no = line_no + 1

print("")
print(f"The total count is {total_count}")
