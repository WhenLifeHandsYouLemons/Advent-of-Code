'''
Advent of Code: Day 11
'''
from helper_methods import *

all_lines = readfile('2024/data.txt')

def part1(blinks: int):
    global all_lines

    stones = [int(i) for i in all_lines[0].split(" ")]

    for i in range(blinks):
        new_stones: list[int] = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                new_stones.append(int(str(stone)[:int(len(str(stone)) / 2)]))
                new_stones.append(int(str(stone)[int((len(str(stone)) / 2)):]))
            else:
                new_stones.append(int(stone * 2024))

        stones = new_stones.copy()

    return len(stones)

def part2(blinks):
    global all_lines

    stones = [int(i) for i in all_lines[0].split(" ")]

    stone_num_to_blink_to_total_stone: dict[int, dict[int, int]] = {
        0: {
            1: 1,
            2: 1,
            3: 2,
            4: 4
        },
        10: {
            1: 2
        },
        7: {
            1: 1
        }
    }

    def computeTotalStones(stone_num: int, blink: int) -> int:
        if blink == 1:
            if stone_num == 0:
                if stone_num not in stone_num_to_blink_to_total_stone.keys():
                    stone_num_to_blink_to_total_stone[stone_num] = {}
                if blink not in stone_num_to_blink_to_total_stone[stone_num].keys():
                    stone_num_to_blink_to_total_stone[stone_num][blink] = 1

                return 1
            elif len(str(stone_num)) % 2 == 0:
                if stone_num not in stone_num_to_blink_to_total_stone.keys():
                    stone_num_to_blink_to_total_stone[stone_num] = {}
                if blink not in stone_num_to_blink_to_total_stone[stone_num].keys():
                    stone_num_to_blink_to_total_stone[stone_num][blink] = 2

                return 2
            else:
                if stone_num not in stone_num_to_blink_to_total_stone.keys():
                    stone_num_to_blink_to_total_stone[stone_num] = {}
                if blink not in stone_num_to_blink_to_total_stone[stone_num].keys():
                    stone_num_to_blink_to_total_stone[stone_num][blink] = 1

                return 1

        if stone_num == 0:
            if stone_num in stone_num_to_blink_to_total_stone.keys() and blink in stone_num_to_blink_to_total_stone[stone_num].keys():
                return stone_num_to_blink_to_total_stone[stone_num][blink]

            total_stones = computeTotalStones(1, blink - 1)

            if stone_num not in stone_num_to_blink_to_total_stone.keys():
                stone_num_to_blink_to_total_stone[stone_num] = {}
            if blink not in stone_num_to_blink_to_total_stone[stone_num].keys():
                stone_num_to_blink_to_total_stone[stone_num][blink] = total_stones
        elif len(str(stone_num)) % 2 == 0:
            if stone_num in stone_num_to_blink_to_total_stone.keys() and blink in stone_num_to_blink_to_total_stone[stone_num].keys():
                return stone_num_to_blink_to_total_stone[stone_num][blink]

            total_stones = computeTotalStones(int(str(stone_num)[:int((len(str(stone_num)) / 2))]), blink - 1) + computeTotalStones(int(str(stone_num)[int(len(str(stone_num)) / 2):]), blink - 1)

            if stone_num not in stone_num_to_blink_to_total_stone.keys():
                stone_num_to_blink_to_total_stone[stone_num] = {}
            if blink not in stone_num_to_blink_to_total_stone[stone_num].keys():
                stone_num_to_blink_to_total_stone[stone_num][blink] = total_stones
        else:
            if stone_num in stone_num_to_blink_to_total_stone.keys() and blink in stone_num_to_blink_to_total_stone[stone_num].keys():
                return stone_num_to_blink_to_total_stone[stone_num][blink]

            total_stones = computeTotalStones(stone_num * 2024, blink - 1)

            if stone_num not in stone_num_to_blink_to_total_stone.keys():
                stone_num_to_blink_to_total_stone[stone_num] = {}
            if blink not in stone_num_to_blink_to_total_stone[stone_num].keys():
                stone_num_to_blink_to_total_stone[stone_num][blink] = total_stones

        return total_stones

    total = 0
    for stone in stones:
        new_stones = computeTotalStones(stone, blinks)
        total += new_stones

    return total

print('Part 1 answer:', part1(25))
print('Part 2 answer:', part2(75))
