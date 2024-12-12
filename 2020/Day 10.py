"""
Advent of Code: Day 10
"""

all_jolts = []
line_no = 0
one_difference = 0
three_difference = 0

with open("C:/Users/2005s/Documents/Visual Studio Code/Advent-of-Code-2020/Day 10/Day 10 Resources.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_jolts.append(int(line))
print(all_jolts)

length = len(all_jolts)

all_jolts.sort()

print(all_jolts)

while line_no != len(all_jolts):
    if line_no != len(all_jolts)-1:
        if all_jolts[line_no]+1 == all_jolts[line_no+1]:
            one_difference = one_difference + 1
            print("One difference")
        elif all_jolts[line_no]+3 == all_jolts[line_no+1]:
            three_difference = three_difference + 1
            print("Three difference")
    line_no = line_no + 1

one_difference = one_difference + 1
three_difference = three_difference + 1

product = one_difference * three_difference

print(len(all_jolts))
print("")
print(f"The 1-jolt difference is {one_difference}, the 3-jolt difference is {three_difference}.")
print(f"The product of 1-jolt and 3-jolt difference is {product}")

print(all_jolts)
line_no = 0
while line_no != length:
    all_jolts.append(str(all_jolts[0]))
    all_jolts.pop(0)
    line_no = line_no + 1
save = "\n".join(all_jolts)
with open("C:/Users/2005s/Documents/Visual Studio Code/Advent-of-Code-2020/Day 10/Day 10 Resources.txt", "w") as f:
    f.write(save)
