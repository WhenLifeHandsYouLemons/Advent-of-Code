"""
Advent of Code: Day 1
"""

all_lines = []
line_no = 0

with open('2023/Day 1/data.txt', 'r') as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)
# print(all_lines)

possible_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
consequent_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

nums = [[] for i in range(len(all_lines))]
while line_no != len(all_lines):
    line = all_lines[line_no]
    cur_word = ""
    end = False
    for char in line:
        if end:
            break
        cur_word += char
        if char.isdigit():
            nums[line_no].append(char)
            cur_word = ""
            end = True
        else:
            for word in possible_words:
                if word in cur_word:
                    nums[line_no].append(consequent_num[possible_words.index(word)])
                    cur_word = ""
                    end = True
                    break

    line = line[::-1]
    cur_word = ""
    end = False
    for char in line:
        if end:
            break
        cur_word = char + cur_word
        if char.isdigit():
            nums[line_no].append(char)
            cur_word = ""
            end = True
        else:
            for word in possible_words:
                if word in cur_word:
                    nums[line_no].append(consequent_num[possible_words.index(word)])
                    cur_word = ""
                    end = True
                    break

    line_no += 1

total = 0
for num in nums:
    total += int(str(num[0]) + str(num[1]))

print(total)