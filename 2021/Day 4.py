"""
Advent of Code: Day 4
"""

all_lines = []
line_no = 0

with open("2021/Day 4/Day 4 Resources.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)

calling_numbers = ""
calling_numbers = all_lines[0]

bingo_cards_list = []
bingo_cards_list = all_lines.copy()
bingo_cards_list.pop(0)
bingo_cards_list.pop(0)

creating_all_bingo_cards = True
creating_bingo_card = True
i = 0
card = []
row = []
bingo_cards = []

# Sorting bingo cards
while creating_all_bingo_cards == True:
    creating_bingo_card = True
    i = 0
    while creating_bingo_card == True:
        row = bingo_cards_list[i].split(" ")
        a = 0
        while a != len(row):
            if row[a] == "":
                row.pop(a)
                a = 0
            else:
                temp = int(row[a])
                row.pop(a)
                row.insert(a, temp)
                a = a + 1

        card.append(row)
        row = []

        i = i + 1

        if i == 5:
            creating_bingo_card = False

    bingo_cards.append(card)
    card = []

    n = 0
    while n != 6 and len(bingo_cards_list) != 0:
        bingo_cards_list.pop(0)
        n = n + 1

    if len(bingo_cards_list) == 0:
        creating_all_bingo_cards = False

# This is how the bingo_cards list looks like
example_bingo_cards = [[[22, 13, 17, 11, 0], [8, 2, 23, 4, 24], [21, 9, 14, 16, 7], [6, 10, 3, 18, 5], [1, 12, 20, 15, 19]], [[3, 15, 0, 2, 22], [9, 18, 13, 17, 5], [19, 8, 7, 25, 23], [20, 11, 10, 24, 4], [14, 21, 16, 12, 6]], [[14, 21, 17, 24, 4], [10, 16, 15, 9, 19], [18, 8, 23, 26, 20], [22, 11, 13, 6, 5], [2, 0, 12, 3, 7]]]

# Convert calling numbers to an int list
calling_numbers = calling_numbers.split(",")
b = 0
while b != len(calling_numbers):
    temp = int(calling_numbers[b])
    calling_numbers.pop(b)
    calling_numbers.insert(b, temp)
    b = b + 1

# The actual useful part
winning = False
card_no = 0
called_numbers = []
called_numbers.append(calling_numbers[0])
called_numbers.append(calling_numbers[1])
called_numbers.append(calling_numbers[2])
called_numbers.append(calling_numbers[3])
called_numbers.append(calling_numbers[4])

current_call_position = 5
while len(bingo_cards) != 1:
    winning = False
    current_call_position = 5
    called_numbers = []
    called_numbers.append(calling_numbers[0])
    called_numbers.append(calling_numbers[1])
    called_numbers.append(calling_numbers[2])
    called_numbers.append(calling_numbers[3])
    called_numbers.append(calling_numbers[4])

    while current_call_position != len(calling_numbers) and winning == False:
        card_no = 0
        while card_no != len(bingo_cards) and winning == False:
            current_card = bingo_cards[card_no]

            # Row check
            row_no = 0
            while row_no != len(current_card) and winning == False:
                current_row = current_card[row_no]
                if current_row[0] in called_numbers:
                    if current_row[1] in called_numbers:
                        if current_row[2] in called_numbers:
                            if current_row[3] in called_numbers:
                                if current_row[4] in called_numbers:
                                    winning = True
                                    winning_card = card_no
                row_no = row_no + 1

            # Column check
            column_no = 0
            while column_no != len(current_card[0]) and winning == False:
                number_no_0 = current_card[0]
                number_no_1 = current_card[1]
                number_no_2 = current_card[2]
                number_no_3 = current_card[3]
                number_no_4 = current_card[4]
                if number_no_0[column_no] in called_numbers:
                    if number_no_1[column_no] in called_numbers:
                        if number_no_2[column_no] in called_numbers:
                            if number_no_3[column_no] in called_numbers:
                                if number_no_4[column_no] in called_numbers:
                                    winning = True
                                    winning_card = card_no
                column_no = column_no + 1

            card_no = card_no + 1
        called_numbers.append(calling_numbers[current_call_position])
        current_call_position = current_call_position + 1
    bingo_cards.pop(winning_card)

print(bingo_cards)

# Remove last added number that wasn't used
# called_numbers.pop()

if winning == True:
    print(f"The losing card is: Card {winning_card}")
    # print(bingo_cards[winning_card])

    won_card = bingo_cards[0]
    print(won_card)
    d = 0
    total = 0
    while d != len(won_card):
        current_won_row = won_card[d]
        print(current_won_row)
        print(called_numbers)
        if current_won_row[0] not in called_numbers:
            total = total + current_won_row[0]
        if current_won_row[1] not in called_numbers:
            total = total + current_won_row[1]
        if current_won_row[2] not in called_numbers:
            total = total + current_won_row[2]
        if current_won_row[3] not in called_numbers:
            total = total + current_won_row[3]
        if current_won_row[4] not in called_numbers:
            total = total + current_won_row[4]
        d = d + 1

    print(total)
        
    final_total = total * called_numbers[-1]

    print(final_total)
else:
    print("There are no losers!")
    print(called_numbers)
