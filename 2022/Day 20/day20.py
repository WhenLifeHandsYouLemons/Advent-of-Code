"""
Advent of Code: Day 20
"""

all_lines = []
i = "$"
with open("2022/Day 20/data.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        app = int(line) * 811589153
        if str(app) in all_lines:
            all_lines.append(f"{app}{i}")
        else:
            all_lines.append(str(app))
        i += "$"

print("Finished loading array")

arrangment = all_lines.copy()

for a in range(10):
    line_no = 0
    while line_no != len(all_lines):
        cur_pos = arrangment.index(all_lines[line_no])
        temp_val = arrangment[cur_pos]

        if "$" in temp_val:
            new_pos = cur_pos + int(temp_val.split("$")[0])
        else:
            new_pos = cur_pos + int(temp_val)

        if abs(new_pos) >= len(arrangment):
            if new_pos > 0:
                new_pos %= len(arrangment) - 1
            else:
                new_pos = -1 * (abs(new_pos) % (len(arrangment) - 1))

        arrangment.pop(cur_pos)
        if new_pos != 0:
            arrangment.insert(new_pos, temp_val)
        else:
            arrangment.append(temp_val)

        line_no += 1

    print(f"Finished {a} mixes")

# Get 1000th, 2000th, 3000th item
print(int(arrangment[(1000 + arrangment.index("0") ) % len(arrangment)].split("$")[0]) + int(arrangment[(2000 + arrangment.index("0") ) % len(arrangment)].split("$")[0]) + int(arrangment[(3000 + arrangment.index("0") ) % len(arrangment)].split("$")[0]))
