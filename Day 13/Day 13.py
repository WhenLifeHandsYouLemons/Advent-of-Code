"""
Advent of Code: Day 13
"""

all_lines = []
line_no = 0
starting_time = 0

with open("C:/Users/2005s/Documents/Visual Studio Code/Advent-of-Code-2020/Day 13/Day 13 Resources.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)
print(all_lines)

# arrival_time = int(all_lines[0])
# all_bus_id = all_lines[1]
# all_bus_id = all_bus_id.split(",")
# print(arrival_time)
# print(all_bus_id)

completed = False

line_no = 100000000000000
line_no = 98538541621
# The answer is 807435693182510

five = []

line_no = 0
while completed == False:
    if line_no % 13 == 0:
        if (line_no+3) % 41 == 0:
            if (line_no+13) % 641 == 0:
                if (line_no+25) % 19 == 0:
                    if (line_no+30) % 17 == 0:
                        if (line_no+42) % 29 == 0:
                            if (line_no+67) % 23 == 0:
                                if (line_no+50) % 37 == 0:
                                    if (line_no+44) % 661 == 0:
                                        completed = True
                    print(line_no)
                    five.append(line_no)
    if len(five) == 5:
        completed = True
        print(five)
    line_no = line_no + 13

# line_no = 1000000
# while completed == False:
#     if line_no % 7 == 0:
#         if (line_no+1) % 13 == 0:
#             if (line_no+4) % 59 == 0:
#                 if (line_no+6) % 31 == 0:
#                     if (line_no+7) % 19 == 0:
#                         completed = True
#                 print(line_no)
#     line_no = line_no + 1

line_no = line_no - 1

print(line_no)
