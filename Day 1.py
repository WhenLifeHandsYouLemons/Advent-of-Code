"""
Advent of Code: Day 1
"""
all_numbers = []
total = 0
multiply_total = 0
num1 = 0
num2 = 0
pos1 = 0
pos2 = 0

with open("C:/Users/2005s/Documents/Visual Studio Code/Advent-of-Code-2020/Day 1 Resources.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        line = int(line)
        all_numbers.append(line)
print(all_numbers)

while total != 2020:
    while pos1 != len(all_numbers):
        while pos2 != len(all_numbers):
            total = all_numbers[pos1] + all_numbers[pos2]

            if total == 2020:
                print(f"The two numbers are {all_numbers[pos1]}, and {all_numbers[pos2]}!")
                num1 = all_numbers[pos1]
                num2 = all_numbers[pos2]
                pos2 = len(all_numbers)
            elif pos2 == len(all_numbers):
                pos2 = len(all_numbers)
            else:
                pos2 = pos2 + 1
        
        if total == 2020:
            pos1 = len(all_numbers)
        else:
            pos1 = pos1 + 1
            pos2 = 0

multiply_total = num1 * num2
print(f"The product of those two numbers is {multiply_total}")
