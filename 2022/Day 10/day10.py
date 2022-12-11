"""
Advent of Code: Day 10
"""

from math import floor


all_lines = []
with open("2022/Day 10/data.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)

screen = []
X_reg = []
cycle_reg = []
x = 1
cycle = 1
line_no = 0
while line_no != len(all_lines):
    if "noop" in all_lines[line_no]:
        X_reg.append(x)
        cycle_reg.append(cycle)
        if x == ((cycle-1) % 40) or x == ((cycle-1) % 40) - 1 or x == ((cycle-1) % 40) + 1:
            screen.append("#")
        else:
            screen.append(".")
        cycle += 1
    else:
        for i in range(2):
            X_reg.append(x)
            cycle_reg.append(cycle)
            if x == ((cycle-1) % 40) or x == ((cycle-1) % 40) - 1 or x == ((cycle-1) % 40) + 1:
                screen.append("#")
            else:
                screen.append(".")
            cycle += 1
        x += int(all_lines[line_no].split(" ")[1])
    line_no += 1

twenty = cycle_reg[19] * X_reg[19]
sixty = cycle_reg[59] * X_reg[59]
hundred = cycle_reg[99] * X_reg[99]
hundred_forty = cycle_reg[139] * X_reg[139]
hundred_eighty = cycle_reg[179] * X_reg[179]
two_hundred_twenty = cycle_reg[219] * X_reg[219]

print(twenty + sixty + hundred + hundred_forty + hundred_eighty + two_hundred_twenty)

for i in range(1, 7):
    print("".join(screen[40*(i-1):40*i]))

# ZKGRKGRK