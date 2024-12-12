"""
Advent of Code: Day 11
"""
from math import floor

class Monkey:
    def __init__(self, items, operation, operation_amount, test, test_true, test_false):
        self.items = []
        for i in items:
            self.items.append(i)
        self.operation = operation
        self.operation_amount = operation_amount
        self.test = test
        self.test_true = test_true
        self.test_false = test_false
        self.count = 0

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self):
        return self.items.pop(0)


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

# Example data
# monkeys = [
#     Monkey([79, 98], "*", 19, 23, 2, 3),
#     Monkey([54, 65, 75, 74], "+", 6, 19, 2, 0),
#     Monkey([79, 60, 97], "*", "old", 13, 1, 3),
#     Monkey([74], "+", 3, 17, 0, 1)
# ]

modulus = 1
for i in monkeys:
    modulus *= i.test

rounds = 10000
seperate = 1
for round in range(rounds):
    for monkey in monkeys:
        while len(monkey.items) != 0:
            # Change worry level
            try:
                amount = int(monkey.operation_amount)
                item_worry_level = eval(f"{monkey.removeItem()} {monkey.operation} {amount}")
            except ValueError:
                amount = monkey.removeItem()
                item_worry_level = eval(f"{amount} {monkey.operation} {amount}")

            # Check if test passes and pass item
            if item_worry_level % monkey.test == 0:
                monkeys[monkey.test_true].addItem(item_worry_level % modulus)
            else:
                monkeys[monkey.test_false].addItem(item_worry_level % modulus)

            monkey.count += 1

counts = []
for monkey in monkeys:
    counts.append(monkey.count)
    # print(monkey.count)

max_val = max(counts)
counts.remove(max(counts))
max_val *= max(counts)
print(max_val)
