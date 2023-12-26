"""
Advent of Code: Day 12
"""
import time


all_lines = []

with open('2023/Day 12/data.txt', 'r') as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)

def part1():
    global all_lines

    total_arrangements = 0

    line_no = 0
    while line_no != len(all_lines):
        line = all_lines[line_no]

        record = [spring for spring in line.split(" ")[0]]

        counts = [int(count) for count in line.split(" ")[1].split(",")]

        print(record)
        print(counts)

        springs = []
        for spring in record:
            if spring == "?":
                springs.append("0")
        total_springs = len(springs)

        while "0" in springs:
            #! Do something here
            springs_to_replace = [("#" if i=="1" else ".") for i in springs]

            record_copy = []
            current_replace = 0
            for rec in record:
                if rec == "?":
                    record_copy.append(springs_to_replace[current_replace])
                    current_replace += 1
                else:
                    record_copy.append(rec)

            print(record_copy)
            count_no = 0
            broken = 0
            streak = False
            for spring in record_copy:
                if spring == "#":
                    broken += 1
                    streak = True
                elif spring == "." and streak:
                    streak = False
                    if broken == counts[count_no]:
                        count_no += 1
                    else:
                        break
                    broken = 0
                if count_no == len(counts):
                    total_arrangements += 1
                    count_no = len(counts) - 1

            if spring == "#":
                if broken == counts[count_no]:
                    count_no += 1
                    broken = 0
                if count_no == len(counts):
                    total_arrangements += 1

            # Increment val to next possibility
            val = "".join(springs).lstrip("0") or "0"
            val = int(val, base=2) + 1
            val = bin(val).split("b")[-1]
            val = val.zfill(total_springs)
            val = [i for i in val]

            springs = val.copy()

        print(total_arrangements)

        #! Do same something here
        springs_to_replace = [("#" if i=="1" else ".") for i in springs]

        record_copy = []
        current_replace = 0
        for rec in record:
            if rec == "?":
                record_copy.append(springs_to_replace[current_replace])
                current_replace += 1
            else:
                record_copy.append(rec)

        print(record_copy)
        count_no = 0
        broken = 0
        streak = False
        for spring in record_copy:
            if spring == "#":
                broken += 1
                streak = True
            elif spring == "." and streak:
                streak = False
                if broken == counts[count_no]:
                    count_no += 1
                else:
                    break
                broken = 0
            if count_no == len(counts):
                total_arrangements += 1
                count_no = len(counts) - 1

        if spring == "#":
            if broken == counts[count_no]:
                count_no += 1
                broken = 0
            if count_no == len(counts):
                total_arrangements += 1

        line_no += 1

    print(total_arrangements)

part1() # Not working yet
