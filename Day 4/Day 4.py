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

    if expire_year != "":
        expire_year = expire_year.split(":")
        expire_year = expire_year[1]
        expire_year = int(expire_year)

    if eye_colour != "":
        eye_colour = eye_colour.split(":")
        eye_colour = eye_colour[1]
        if eye_colour != "amb" and eye_colour != "blu" and eye_colour != "brn" and eye_colour != "gry" and eye_colour != "grn" and eye_colour != "hzl" and eye_colour != "oth":
            eye_colour = ""
        else:
            print("Eye colour valid")

    if "#" in hair_colour:
        hair_colour = hair_colour.split("#")
        hair_colour = hair_colour[1]
        for char in hair_colour:
            if char.isalpha():
                if char > "f":
                    hair_colour = ""
            elif char.isnumeric():
                char = int(char)
                if char > 9 or char < 0:
                    hair_colour = ""
        if hair_colour != "":
            print("Hair colour valid")
    else:
        hair_colour = ""

    if expire_year != "":
        if expire_year >= 2020 and expire_year <= 2030:
            expire_year = str(expire_year)
            if len(expire_year) != 4:
                expire_year = ""
            else:
                print("Expire year valid")
        else:
            expire_year = ""

    if birth_year != "":
        if birth_year >= 1920 and birth_year <= 2002:
            birth_year = str(birth_year)
            if len(birth_year) != 4:
                birth_year = ""
            else:
                print("Birth year valid")
        else:
            birth_year = ""

    if issue_year != "":
        if issue_year >= 2010 and issue_year <= 2020:
            issue_year = str(issue_year)
            if len(issue_year) != 4:
                issue_year = ""
            else:
                print("Issue year valid")
        else:
            issue_year = ""

    if height != "":
        height = height.split(":")
        height = height[1]
        if "cm" in height:
            height = height.split("cm")
            height = int(height[0])
            if height > 193 or height < 150:
                height = ""
            else:
                print("Height valid")
        elif "in" in height:
            height = height.split("in")
            height = int(height[0])
            if height > 76 or height < 59:
                height = ""
            else:
                print("Height valid")
        else:
            height = ""

    if passport_id != "":
        passport_id = passport_id.split(":")
        passport_id = str(passport_id[1])
        if len(passport_id) != 9:
            passport_id = ""
        else:
            print("Passport ID valid")

    if birth_year != "" and issue_year != "" and expire_year != "" and height != "" and hair_colour != "" and eye_colour != "" and passport_id != "":
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
