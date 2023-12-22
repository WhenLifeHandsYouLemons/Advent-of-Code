"""
Advent of Code: Day 7
"""
all_lines = []

with open('2023/Day 7/data.txt', 'r') as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)

def part1():
    global all_lines

    card_rank = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    hand_ranks = []

    hands = {
        "High card": [],
        "One pair": [],
        "Two pair": [],
        "Three of a kind": [],
        "Full house": [],
        "Four of a kind": [],
        "Five of a kind": []
    }

    def isFiveOfAKind(hand) -> bool:
        card_count = {}
        for card in hand:
            if card in card_count:
                card_count[card] += 1
            else:
                card_count[card] = 1

        if 5 in list(card_count.values()):
            return True
        return False

    def isFourOfAKind(hand) -> bool:
        card_count = {}
        for card in hand:
            if card in card_count:
                card_count[card] += 1
            else:
                card_count[card] = 1

        if 4 in list(card_count.values()):
            return True
        return False

    def isFullHouse(hand) -> bool:
        card_count = {}
        for card in hand:
            if card in card_count:
                card_count[card] += 1
            else:
                card_count[card] = 1

        if 3 in list(card_count.values()) and 2 in list(card_count.values()):
            return True
        return False

    def isThreeOfAKind(hand) -> bool:
        card_count = {}
        for card in hand:
            if card in card_count:
                card_count[card] += 1
            else:
                card_count[card] = 1

        if 3 in list(card_count.values()):
            return True
        return False

    def isTwoPair(hand) -> bool:
        card_count = {}
        for card in hand:
            if card in card_count:
                card_count[card] += 1
            else:
                card_count[card] = 1

        counts = list(card_count.values())

        if counts.count(2) == 2:
            return True
        return False

    def isOnePair(hand) -> bool:
        card_count = {}
        for card in hand:
            if card in card_count:
                card_count[card] += 1
            else:
                card_count[card] = 1

        if list(card_count.values()).count(2) == 1:
            return True
        return False

    def getHighCard(hand) -> str:
        highest = -1

        for card in hand:
            if card_rank.index(card) > highest:
                highest = card_rank.index(card)

        return card_rank[highest]

    def convertNumToStr(hand) -> str:
        bets = [i[1] for i in hand]
        hands = [i[0] for i in hand]
        conversions = {
            "2": "2",
            "3": "3",
            "4": "4",
            "5": "5",
            "6": "6",
            "7": "7",
            "8": "8",
            "9": "9",
            "T": "A",
            "J": "B",
            "Q": "C",
            "K": "D",
            "A": "E"
        }
        return [["".join([conversions[card] for card in hand]), bets.pop(0)] for hand in hands]

    def sort(array):
        sorted_array = []
        for item in array:
            i = 0
            added = False

            while i < len(sorted_array):
                item2 = sorted_array[i]

                if sorted_array == []:
                    i = len(sorted_array)

                if item[0] < item2[0]:
                    sorted_array.insert(i, item)
                    i = len(sorted_array)
                    added = True

                i += 1

            if not added:
                sorted_array.append(item)

        return sorted_array

    line_no = 0
    while line_no != len(all_lines):
        line = all_lines[line_no]

        hand = line.split(" ")[0]
        bet = int(line.split(" ")[-1])

        if isFiveOfAKind(hand):
            hands["Five of a kind"].append([hand, bet])
        elif isFourOfAKind(hand):
            hands["Four of a kind"].append([hand, bet])
        elif isFullHouse(hand):
            hands["Full house"].append([hand, bet])
        elif isThreeOfAKind(hand):
            hands["Three of a kind"].append([hand, bet])
        elif isTwoPair(hand):
            hands["Two pair"].append([hand, bet])
        elif isOnePair(hand):
            hands["One pair"].append([hand, bet])
        else:
            hands["High card"].append([hand, bet])

        line_no += 1

    # Sort out each key in dict and append into hand_ranks
    for key, value in hands.items():
        if len(value) != 0:
            sorted_value = sort(convertNumToStr(value))
            hand_ranks.extend(sorted_value)

    total = 0
    pos = 0
    while pos < len(hand_ranks):
        total += (hand_ranks[pos][1] * (pos+1))
        pos += 1

    print(total)

def part2():
    global all_lines

    card_rank = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
    hand_ranks = []

    hands = {
        "High card": [],
        "One pair": [],
        "Two pair": [],
        "Three of a kind": [],
        "Full house": [],
        "Four of a kind": [],
        "Five of a kind": []
    }

    def isFiveOfAKind(hand) -> bool:
        card_count = {}
        for card in hand:
            if card in card_count:
                card_count[card] += 1
            else:
                card_count[card] = 1

        occurences = list(card_count.values())
        occurence_keys = list(card_count.items())

        # If the joker is there
        if "J" in card_count.keys() and hand != "JJJJJ":
            max_key = ()
            max_val = 0
            remove_key = ()
            # Go through occurence_keys
            for key in occurence_keys:
                # Find the maximum occurence
                # If it's a joker, don't count it
                if key[0] != "J" and key[1] > max_val:
                    max_key = key
                    max_val = key[1]
                if key[0] == "J":
                    remove_key = key

            max_pos = occurence_keys.index(max_key)
            remove_pos = occurence_keys.index(remove_key)

            # Add the amount from remove_key to max_key
            occurences[max_pos] += occurences[remove_pos]
            occurences.pop(remove_pos)

        if 5 in occurences:
            return True
        return False

    def isFourOfAKind(hand) -> bool:
        card_count = {}
        for card in hand:
            if card in card_count:
                card_count[card] += 1
            else:
                card_count[card] = 1

        occurences = list(card_count.values())
        occurence_keys = list(card_count.items())

        # If the joker is there
        if "J" in card_count.keys():
            max_key = ()
            max_val = 0
            remove_key = ()
            # Go through occurence_keys
            for key in occurence_keys:
                # Find the maximum occurence
                # If it's a joker, don't count it
                if key[0] != "J" and key[1] > max_val:
                    max_key = key
                    max_val = key[1]
                if key[0] == "J":
                    remove_key = key

            max_pos = occurence_keys.index(max_key)
            remove_pos = occurence_keys.index(remove_key)

            # Add the amount from remove_key to max_key
            occurences[max_pos] += occurences[remove_pos]
            occurences.pop(remove_pos)

        if 4 in occurences:
            return True
        return False

    def isFullHouse(hand) -> bool:
        card_count = {}
        for card in hand:
            if card in card_count:
                card_count[card] += 1
            else:
                card_count[card] = 1

        occurences = list(card_count.values())
        occurence_keys = list(card_count.items())

        # If the joker is there
        if "J" in card_count.keys():
            max_key = ()
            max_val = 0
            remove_key = ()
            # Go through occurence_keys
            for key in occurence_keys:
                # Find the maximum occurence
                # If it's a joker, don't count it
                if key[0] != "J" and key[1] > max_val:
                    max_key = key
                    max_val = key[1]
                if key[0] == "J":
                    remove_key = key

            max_pos = occurence_keys.index(max_key)
            remove_pos = occurence_keys.index(remove_key)

            # Add the amount from remove_key to max_key
            occurences[max_pos] += occurences[remove_pos]
            occurences.pop(remove_pos)

        if 3 in occurences and 2 in occurences:
            return True
        return False

    def isThreeOfAKind(hand) -> bool:
        card_count = {}
        for card in hand:
            if card in card_count:
                card_count[card] += 1
            else:
                card_count[card] = 1

        occurences = list(card_count.values())
        occurence_keys = list(card_count.items())

        # If the joker is there
        if "J" in card_count.keys():
            max_key = ()
            max_val = 0
            remove_key = ()
            # Go through occurence_keys
            for key in occurence_keys:
                # Find the maximum occurence
                # If it's a joker, don't count it
                if key[0] != "J" and key[1] > max_val:
                    max_key = key
                    max_val = key[1]
                if key[0] == "J":
                    remove_key = key

            max_pos = occurence_keys.index(max_key)
            remove_pos = occurence_keys.index(remove_key)

            # Add the amount from remove_key to max_key
            occurences[max_pos] += occurences[remove_pos]
            occurences.pop(remove_pos)

        if 3 in occurences:
            return True
        return False

    def isTwoPair(hand) -> bool:
        card_count = {}
        for card in hand:
            if card in card_count:
                card_count[card] += 1
            else:
                card_count[card] = 1

        occurences = list(card_count.values())
        occurence_keys = list(card_count.items())

        # If the joker is there
        if "J" in card_count.keys():
            max_key = ()
            max_val = 0
            remove_key = ()
            # Go through occurence_keys
            for key in occurence_keys:
                # Find the maximum occurence
                # If it's a joker, don't count it
                if key[0] != "J" and key[1] > max_val:
                    max_key = key
                    max_val = key[1]
                if key[0] == "J":
                    remove_key = key

            max_pos = occurence_keys.index(max_key)
            remove_pos = occurence_keys.index(remove_key)

            # Add the amount from remove_key to max_key
            occurences[max_pos] += occurences[remove_pos]
            occurences.pop(remove_pos)

        if occurences.count(2) == 2:
            return True
        return False

    def isOnePair(hand) -> bool:
        card_count = {}
        for card in hand:
            if card in card_count:
                card_count[card] += 1
            else:
                card_count[card] = 1

        occurences = list(card_count.values())
        occurence_keys = list(card_count.items())

        # If the joker is there
        if "J" in card_count.keys():
            max_key = ()
            max_val = 0
            remove_key = ()
            # Go through occurence_keys
            for key in occurence_keys:
                # Find the maximum occurence
                # If it's a joker, don't count it
                if key[0] != "J" and key[1] > max_val:
                    max_key = key
                    max_val = key[1]
                if key[0] == "J":
                    remove_key = key

            max_pos = occurence_keys.index(max_key)
            remove_pos = occurence_keys.index(remove_key)

            # Add the amount from remove_key to max_key
            occurences[max_pos] += occurences[remove_pos]
            occurences.pop(remove_pos)

        if occurences.count(2) == 1:
            return True
        return False

    def convertNumToStr(hand) -> str:
        bets = [i[1] for i in hand]
        hands = [i[0] for i in hand]
        conversions = {
            "J": "1",
            "2": "2",
            "3": "3",
            "4": "4",
            "5": "5",
            "6": "6",
            "7": "7",
            "8": "8",
            "9": "9",
            "T": "A",
            "Q": "B",
            "K": "C",
            "A": "D"
        }
        return [["".join([conversions[card] for card in hand]), bets.pop(0)] for hand in hands]

    def sort(array):
        sorted_array = []
        for item in array:
            i = 0
            added = False

            while i < len(sorted_array):
                item2 = sorted_array[i]

                if sorted_array == []:
                    i = len(sorted_array)

                if item[0] < item2[0]:
                    sorted_array.insert(i, item)
                    i = len(sorted_array)
                    added = True

                i += 1

            if not added:
                sorted_array.append(item)

        return sorted_array

    line_no = 0
    while line_no != len(all_lines):
        line = all_lines[line_no]

        hand = line.split(" ")[0]
        bet = int(line.split(" ")[-1])

        if isFiveOfAKind(hand):
            hands["Five of a kind"].append([hand, bet])
        elif isFourOfAKind(hand):
            hands["Four of a kind"].append([hand, bet])
        elif isFullHouse(hand):
            hands["Full house"].append([hand, bet])
        elif isThreeOfAKind(hand):
            hands["Three of a kind"].append([hand, bet])
        elif isTwoPair(hand):
            hands["Two pair"].append([hand, bet])
        elif isOnePair(hand):
            hands["One pair"].append([hand, bet])
        else:
            hands["High card"].append([hand, bet])

        line_no += 1

    # Sort out each key in dict and append into hand_ranks
    for key, value in hands.items():
        if len(value) != 0:
            sorted_value = sort(convertNumToStr(value))
            hand_ranks.extend(sorted_value)

    total = 0
    pos = 0
    while pos < len(hand_ranks):
        total += (hand_ranks[pos][1] * (pos+1))
        pos += 1

    print(total)

part1()
part2()
