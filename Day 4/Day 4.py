"""
# Advent of Code: Day 4
"""

all_lines = []
seperated_line = []
valid_passports = 0
line_no = 0
full = ""
birth_year = ""
issue_year = ""
expire_year = ""
height = ""
hair_colour = ""
eye_colour = ""
passport_id = ""
country_id = ""
replacing = ""

with open("C:/Users/2005s/Documents/Visual Studio Code/Advent-of-Code-2020/Day 4/Day 4 Resources.txt", "r") as f:
    content = f.read()
    full = content
    all_lines = full.split("\n\n")

print(all_lines)
total = len(all_lines)
while line_no != total:
    replacing = all_lines[0].replace("\n", " ")
    all_lines.append(replacing)
    all_lines.pop(0)

    replacing = ""
    line_no = line_no + 1
print(all_lines)

lines = 0
while lines != len(all_lines):
    seperated_line = all_lines[lines].split(" ")
    print(seperated_line)

    line_no = 0
    line = 0

    while line != len(seperated_line):
        if "byr" in seperated_line[line]:
            birth_year = seperated_line[line]
        elif "iyr" in seperated_line[line]:
            issue_year = seperated_line[line]
        elif "eyr" in seperated_line[line]:
            expire_year = seperated_line[line]
        elif "hgt" in seperated_line[line]:
            height = seperated_line[line]
        elif "hcl" in seperated_line[line]:
            hair_colour = seperated_line[line]
        elif "ecl" in seperated_line[line]:
            eye_colour = seperated_line[line]
        elif "pid" in seperated_line[line]:
            passport_id = seperated_line[line]
        elif "cid" in seperated_line[line]:
            country_id = seperated_line[line]

        print(birth_year, issue_year, expire_year, height, hair_colour, eye_colour, passport_id, country_id)

        line = line + 1

    if birth_year != "":
        birth_year = birth_year.split(":")
        birth_year = birth_year[1]
        birth_year = int(birth_year)

    if issue_year != "":
        issue_year = issue_year.split(":")
        issue_year = issue_year[1]
        issue_year = int(issue_year)

    if birth_year != "" and birth_year >= 1920 and birth_year <= 2002 and len(birth_year) == 4 and issue_year != "" and issue_year >= 2010 and issue_year <= 2020 and len(issue_year) == 4 and expire_year >= 2020 and expire_year <= 2030 and len(expire_year) == 4 and expire_year != "" and height != "" and hair_colour != "" and eye_colour != "" and passport_id != "":
        valid_passports = valid_passports + 1
        print("Valid!")
    else:
        print("Invalid!")

    birth_year = ""
    issue_year = ""
    expire_year = ""
    height = ""
    hair_colour = ""
    eye_colour = ""
    passport_id = ""
    country_id = ""
    line = 0

    lines = lines + 1

print("")
print(f"There are {valid_passports} valid passports!")
