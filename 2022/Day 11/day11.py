"""
Advent of Code: Day 11
"""
from math import floor
from Monkey import Monkey
from Item import Item

all_lines = []
line_no = 0

with open("2022/Day 11/data.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)

# Create monkeys
monkeys = [
    Monkey([85, 77, 77], "*", 7, 19, 6, 7),
    Monkey([80, 99], "*", 11, 3, 3, 5),
    Monkey([74, 60, 74, 62, 86, 92, 80], "+", 8, 13, 0, 6),
    Monkey([71, 58, 93, 65, 80, 68, 54, 71], "+", 7, 7, 2, 4),
    Monkey([97,56, 79, 65, 58], "+", 5, 5, 2, 0),
    Monkey([77], "+", 4, 11, 4, 3),
    Monkey([99, 90, 84, 50], "*", "old", 17, 7, 1),
    Monkey([50, 66, 61, 92, 64, 78], "+", 3, 2, 5, 1)
]

rounds = 20
for round in range(rounds):
    for monkey in monkeys:
        while len(monkey.items) != 0:
            # Change worry level
            if monkey.operation == "*":
                try:
                    amount = int(monkey.operation_amount)
                    item_worry_level = monkey.removeItem() * amount
                except ValueError:
                    item_worry_level = monkey.removeItem() ** 2
            elif monkey.operation == "+":
                try:
                    amount = int(monkey.operation_amount)
                    item_worry_level = monkey.removeItem() + amount
                except ValueError:
                    item_worry_level = monkey.removeItem() * 2
            elif monkey.operation == "/":
                try:
                    amount = int(monkey.operation_amount)
                    item_worry_level = monkey.removeItem() / amount
                except ValueError:
                    item_worry_level = 1
            elif monkey.operation == "-":
                try:
                    amount = int(monkey.operation_amount)
                    item_worry_level = monkey.removeItem() - amount
                except ValueError:
                    item_worry_level = 0

            item_worry_level = floor(item_worry_level / 3)

            # Check if test passes and pass item
            if item_worry_level % monkey.test == 0:
                monkeys[monkey.test_true].addItem(item_worry_level)
            else:
                monkeys[monkey.test_false].addItem(item_worry_level)

            monkey.count += 1

# for monkey in monkeys:
#     print(monkey.items)

counts = []
for monkey in monkeys:
    counts.append(monkey.count)

max_val = max(counts)
counts.remove(max(counts))
max_val *= max(counts)
print(max_val)
