"""
Advent of Code: Day 8
"""

all_lines = []

with open("C:/Users/2005s/Desktop/Advent-of-Code/2021/Day 8/Day 8 Resources.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)
input_displays = []
output_displays = []


def part_1():
    line_no = 0
    while line_no != len(all_lines):
        temp = all_lines[line_no].split(" | ")
        output_displays.append(temp[1])
        input_displays.append(temp[0])
        line_no = line_no + 1

    lining = 0
    total = 0
    while lining != len(output_displays):
        current_line = 0
        current_output = output_displays[lining].split(" ")
        while current_line != len(current_output):
            if len(current_output[current_line]) == 2 or len(current_output[current_line]) == 4 or len(current_output[current_line]) == 3 or len(current_output[current_line]) == 7:
                total = total + 1
            current_line = current_line + 1
        lining = lining + 1

    return total

def part_2():
    line_no = 0
    total = 0
    # Get each segment and output values
    while line_no != len(input_displays):
        zero_six_nine = []
        two_three_five = []
        zero = ""
        one = ""
        two = ""
        three = ""
        four = ""
        five = ""
        six = ""
        seven = ""
        eight = ""
        nine = ""
        current_line = input_displays[line_no].split(" ")
        # Get the numbers that we already know are true
        for digit in current_line:
            if len(digit) == 2:
                one = digit
            elif len(digit) == 4:
                four = digit
            elif len(digit) == 3:
                seven = digit
            elif len(digit) == 7:
                eight = digit

        # Get each digit and sort them out
        for digit in current_line:
            # This can equal a 0, 6, or 9
            if len(digit) == 6 and digit not in zero_six_nine:
                zero_six_nine.append(digit)
            # This can equal a 2, 3, or 5
            elif len(digit) == 5 and digit not in two_three_five:
                two_three_five.append(digit)

        # Find the first digit segment
        digit_order = []
        for letter in seven:
            if letter not in one and letter not in digit_order:
                digit_order.append(letter)

        # Find the second digit segment
        a_235 = 0
        b_235 = 0
        c_235 = 0
        d_235 = 0
        e_235 = 0
        f_235 = 0
        g_235 = 0
        for digit in two_three_five:
            for letter in digit:
                if letter == "a":
                    a_235 += 1
                elif letter == "b":
                    b_235 += 1
                elif letter == "c":
                    c_235 += 1
                elif letter == "d":
                    d_235 += 1
                elif letter == "e":
                    e_235 += 1
                elif letter == "f":
                    f_235 += 1
                elif letter == "g":
                    g_235 += 1

        a_069 = 0
        b_069 = 0
        c_069 = 0
        d_069 = 0
        e_069 = 0
        f_069 = 0
        g_069 = 0
        for digit in zero_six_nine:
            for letter in digit:
                if letter == "a":
                    a_069 += 1
                elif letter == "b":
                    b_069 += 1
                elif letter == "c":
                    c_069 += 1
                elif letter == "d":
                    d_069 += 1
                elif letter == "e":
                    e_069 += 1
                elif letter == "f":
                    f_069 += 1
                elif letter == "g":
                    g_069 += 1

        # Find the second segment letter
        if a_235 == 1 and a_069 == 3:
            digit_order.append("a")
        elif  b_235 == 1 and b_069 == 3:
            digit_order.append("b")
        elif c_235 == 1 and c_069 == 3:
            digit_order.append("c")
        elif d_235 == 1 and d_069 == 3:
            digit_order.append("d")
        elif e_235 == 1 and e_069 == 3:
            digit_order.append("e")
        elif f_235 == 1 and f_069 == 3:
            digit_order.append("f")
        elif g_235 == 1 and g_069 == 3:
            digit_order.append("g")

        # Find the third digit-segment
        a_235 = 0
        b_235 = 0
        c_235 = 0
        d_235 = 0
        e_235 = 0
        f_235 = 0
        g_235 = 0
        for digit in two_three_five:
            for letter in digit:
                if letter == "a":
                    a_235 += 1
                elif letter == "b":
                    b_235 += 1
                elif letter == "c":
                    c_235 += 1
                elif letter == "d":
                    d_235 += 1
                elif letter == "e":
                    e_235 += 1
                elif letter == "f":
                    f_235 += 1
                elif letter == "g":
                    g_235 += 1

        a_069 = 0
        b_069 = 0
        c_069 = 0
        d_069 = 0
        e_069 = 0
        f_069 = 0
        g_069 = 0
        for digit in zero_six_nine:
            for letter in digit:
                if letter == "a":
                    a_069 += 1
                elif letter == "b":
                    b_069 += 1
                elif letter == "c":
                    c_069 += 1
                elif letter == "d":
                    d_069 += 1
                elif letter == "e":
                    e_069 += 1
                elif letter == "f":
                    f_069 += 1
                elif letter == "g":
                    g_069 += 1

        # Find what segment it is
        if a_235 == 2 and a_069 == 2:
            digit_order.append("a")
        elif  b_235 == 2 and b_069 == 2:
            digit_order.append("b")
        elif c_235 == 2 and c_069 == 2:
            digit_order.append("c")
        elif d_235 == 2 and d_069 == 2:
            digit_order.append("d")
        elif e_235 == 2 and e_069 == 2:
            digit_order.append("e")
        elif f_235 == 2 and f_069 == 2:
            digit_order.append("f")
        elif g_235 == 2 and g_069 == 2:
            digit_order.append("g")

        # Find the fourth digit segment
        a_235 = 0
        b_235 = 0
        c_235 = 0
        d_235 = 0
        e_235 = 0
        f_235 = 0
        g_235 = 0
        for digit in two_three_five:
            for letter in digit:
                if letter == "a":
                    a_235 += 1
                elif letter == "b":
                    b_235 += 1
                elif letter == "c":
                    c_235 += 1
                elif letter == "d":
                    d_235 += 1
                elif letter == "e":
                    e_235 += 1
                elif letter == "f":
                    f_235 += 1
                elif letter == "g":
                    g_235 += 1

        a_069 = 0
        b_069 = 0
        c_069 = 0
        d_069 = 0
        e_069 = 0
        f_069 = 0
        g_069 = 0
        for digit in zero_six_nine:
            for letter in digit:
                if letter == "a":
                    a_069 += 1
                elif letter == "b":
                    b_069 += 1
                elif letter == "c":
                    c_069 += 1
                elif letter == "d":
                    d_069 += 1
                elif letter == "e":
                    e_069 += 1
                elif letter == "f":
                    f_069 += 1
                elif letter == "g":
                    g_069 += 1

        # Find what segment it is
        if a_235 == 3 and a_069 == 2:
            digit_order.append("a")
        elif  b_235 == 3 and b_069 == 2:
            digit_order.append("b")
        elif c_235 == 3 and c_069 == 2:
            digit_order.append("c")
        elif d_235 == 3 and d_069 == 2:
            digit_order.append("d")
        elif e_235 == 3 and e_069 == 2:
            digit_order.append("e")
        elif f_235 == 3 and f_069 == 2:
            digit_order.append("f")
        elif g_235 == 3 and g_069 == 2:
            digit_order.append("g")

        # Find the fifth digit segment
        a_235 = 0
        b_235 = 0
        c_235 = 0
        d_235 = 0
        e_235 = 0
        f_235 = 0
        g_235 = 0
        for digit in two_three_five:
            for letter in digit:
                if letter == "a":
                    a_235 += 1
                elif letter == "b":
                    b_235 += 1
                elif letter == "c":
                    c_235 += 1
                elif letter == "d":
                    d_235 += 1
                elif letter == "e":
                    e_235 += 1
                elif letter == "f":
                    f_235 += 1
                elif letter == "g":
                    g_235 += 1

        a_069 = 0
        b_069 = 0
        c_069 = 0
        d_069 = 0
        e_069 = 0
        f_069 = 0
        g_069 = 0
        for digit in zero_six_nine:
            for letter in digit:
                if letter == "a":
                    a_069 += 1
                elif letter == "b":
                    b_069 += 1
                elif letter == "c":
                    c_069 += 1
                elif letter == "d":
                    d_069 += 1
                elif letter == "e":
                    e_069 += 1
                elif letter == "f":
                    f_069 += 1
                elif letter == "g":
                    g_069 += 1

        # Find what segment it is
        if a_235 == 1 and a_069 == 2:
            digit_order.append("a")
        elif  b_235 == 1 and b_069 == 2:
            digit_order.append("b")
        elif c_235 == 1 and c_069 == 2:
            digit_order.append("c")
        elif d_235 == 1 and d_069 == 2:
            digit_order.append("d")
        elif e_235 == 1 and e_069 == 2:
            digit_order.append("e")
        elif f_235 == 1 and f_069 == 2:
            digit_order.append("f")
        elif g_235 == 1 and g_069 == 2:
            digit_order.append("g")

        # Find the sixth digit segment
        for letter in one:
            if letter not in digit_order:
                digit_order.append(letter)

        for letter in eight:
            if letter not in digit_order:
                digit_order.append(letter)

        # Find out what zero is
        assumed_zero = []
        assumed_zero.append(digit_order[0])
        assumed_zero.append(digit_order[1])
        assumed_zero.append(digit_order[2])
        assumed_zero.append(digit_order[4])
        assumed_zero.append(digit_order[5])
        assumed_zero.append(digit_order[6])
        for digit in zero_six_nine:
            all_correct = 0
            for letter in digit:
                if letter in assumed_zero:
                    all_correct += 1
            if all_correct >= len(assumed_zero):
                zero = digit

        # Find out what two is
        assumed_two = []
        assumed_two.append(digit_order[0])
        assumed_two.append(digit_order[2])
        assumed_two.append(digit_order[3])
        assumed_two.append(digit_order[4])
        assumed_two.append(digit_order[6])
        for digit in two_three_five:
            all_correct = 0
            for letter in digit:
                if letter in assumed_two:
                    all_correct += 1
            if all_correct == len(assumed_two):
                two = digit

        # Find out what three is
        assumed_three = []
        assumed_three.append(digit_order[0])
        assumed_three.append(digit_order[2])
        assumed_three.append(digit_order[3])
        assumed_three.append(digit_order[5])
        assumed_three.append(digit_order[6])
        for digit in two_three_five:
            all_correct = 0
            for letter in digit:
                if letter in assumed_three:
                    all_correct += 1
            if all_correct == len(assumed_three):
                three = digit

        # Find out what five is
        assumed_five = []
        assumed_five.append(digit_order[0])
        assumed_five.append(digit_order[1])
        assumed_five.append(digit_order[3])
        assumed_five.append(digit_order[5])
        assumed_five.append(digit_order[6])
        for digit in two_three_five:
            all_correct = 0
            for letter in digit:
                if letter in assumed_five:
                    all_correct += 1
            if all_correct == len(assumed_five):
                five = digit

        # Find out what six is
        assumed_six = []
        assumed_six.append(digit_order[0])
        assumed_six.append(digit_order[1])
        assumed_six.append(digit_order[3])
        assumed_six.append(digit_order[4])
        assumed_six.append(digit_order[5])
        assumed_six.append(digit_order[6])
        for digit in zero_six_nine:
            all_correct = 0
            for letter in digit:
                if letter in assumed_six:
                    all_correct += 1
            if all_correct == len(assumed_six):
                six = digit

        # Find out what nine is
        assumed_nine = []
        assumed_nine.append(digit_order[0])
        assumed_nine.append(digit_order[1])
        assumed_nine.append(digit_order[2])
        assumed_nine.append(digit_order[3])
        assumed_nine.append(digit_order[5])
        assumed_nine.append(digit_order[6])
        for digit in zero_six_nine:
            all_correct = 0
            for letter in digit:
                if letter in assumed_nine:
                    all_correct += 1
            if all_correct == len(assumed_nine):
                nine = digit

        # Find out the actualy digits of the output
        current_output = output_displays[line_no].split(" ")
        output = []
        for current_output_digit in current_output:
            # Check for zero
            check = 0
            for letter in zero:
                if letter in current_output_digit:
                    check = check + 1
                else:
                    check -= 1
            if check-len(current_output_digit) == 0:
                output.append(0)
            else:
                # Check for one
                check = 0
                for letter in one:
                    if letter in current_output_digit:
                        check += 1
                    else:
                        check -= 1
                if check-len(current_output_digit) == 0:
                    output.append(1)
                else:
                    # Check for two
                    check = 0
                    for letter in two:
                        if letter in current_output_digit:
                            check = check + 1
                        else:
                            check -= 1
                    if check-len(current_output_digit) == 0:
                        output.append(2)
                    else:
                        # Check for three
                        check = 0
                        for letter in three:
                            if letter in current_output_digit:
                                check = check + 1
                            else:
                                check -= 1
                        if check-len(current_output_digit) == 0:
                            output.append(3)
                        else:
                            # Check for four
                            check = 0
                            for letter in four:
                                if letter in current_output_digit:
                                    check = check + 1
                                else:
                                    check -= 1
                            if check-len(current_output_digit) == 0:
                                output.append(4)
                            else:
                                # Check for five
                                check = 0
                                for letter in five:
                                    if letter in current_output_digit:
                                        check = check + 1
                                    else:
                                        check -= 1
                                if check-len(current_output_digit) == 0:
                                    output.append(5)
                                else:
                                    # Check for six
                                    check = 0
                                    for letter in six:
                                        if letter in current_output_digit:
                                            check = check + 1
                                        else:
                                            check -= 1
                                    if check-len(current_output_digit) == 0:
                                        output.append(6)
                                    else:
                                        # Check for seven
                                        check = 0
                                        for letter in seven:
                                            if letter in current_output_digit:
                                                check = check + 1
                                            else:
                                                check -= 1
                                        if check-len(current_output_digit) == 0:
                                            output.append(7)
                                        else:
                                            # Check for eight
                                            check = 0
                                            for letter in eight:
                                                if letter in current_output_digit:
                                                    check = check + 1
                                                else:
                                                    check -= 1
                                            if check-len(current_output_digit) == 0:
                                                output.append(8)
                                            else:
                                                # Check for nine
                                                check = 0
                                                for letter in nine:
                                                    if letter in current_output_digit:
                                                        check = check + 1
                                                    else:
                                                        check -= 1
                                                if check-len(current_output_digit) == 0:
                                                    output.append(9)

        # Join the numbers together
        current_total = output[0]*1000 + output[1]*100 + output[2]*10 + output[3]
        total = total + current_total

        line_no = line_no + 1

    return total

print("Part 1 answer: ", part_1())
print("Part 2 answer: ", part_2())
