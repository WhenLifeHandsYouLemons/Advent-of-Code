"""
Advent of Code: Day 15
"""

starting_numbers = [5, 2, 8, 16, 18, 0, 1]
all_lines = [5, 2, 8, 16, 18, 0, 1]
turn_no = len(starting_numbers) + 1
current_number = 0
temp = 0
#print(all_lines[0], all_lines[1], all_lines[2])

while turn_no-1 != 2020:
#    print(f"It's turn number {turn_no}.")
    current_number = int(all_lines[len(all_lines)-1])
#    print(current_number)
#    print(all_lines)
    all_lines.pop(len(all_lines)-1)
#    print(turn_no)
#    print(f"I've removed {len(all_lines)-1}.")
    if current_number in all_lines:
#        print("This number is already on the list.")
        all_lines.append(current_number)
        matched_indexes = []
        length = len(all_lines)
        i = 0
        while i < length:
            if current_number == all_lines[i]:
                matched_indexes.append(i)
            i = i + 1
#        print(matched_indexes)

        total = matched_indexes[-1] - matched_indexes[-2]
#        print(all_lines)
#        print(total)
        all_lines.append(total)
        if temp >= 10000:
            print(all_lines)
            print(f"It's turn number {turn_no}.")
            temp = 0
    else:
        all_lines.append(current_number)
        all_lines.append(0)
#        print("This number was not in the list!")
#    print(f"The number spoken on the {turn_no}th turn is {all_lines[len(all_lines)-1]}.")
    turn_no = turn_no + 1
    temp = temp + 1

turn_no = turn_no - 1
print(f"The number spoken on turn {turn_no} is {all_lines[len(all_lines)-1]}.")
