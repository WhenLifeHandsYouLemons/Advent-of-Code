"""
Advent of Code: Day 6
"""

all_lines = []

with open('2023/Day 6/data.txt', 'r') as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)
# print(all_lines)

def part1():
    global all_lines

    # Get just the specific values needed
    times = [item for item in all_lines[0].split(":")[-1].split(" ") if item != ""]
    distances = [item for item in all_lines[1].split(":")[-1].split(" ") if item != ""]

    # Go through each race
    total_wins = 1
    race = 0
    while race < len(times):
        total_time = int(times[race])
        record_distance = int(distances[race])

        race_wins = 0
        for button_hold_time in range(total_time+1):
            distance_travelled = -((button_hold_time - (total_time / 2))**2) + ((total_time / 2)**2)
            if distance_travelled > record_distance:
                race_wins += 1

        total_wins *= race_wins

        race += 1

    print(total_wins)

def part2():
    global all_lines

    # Get the time and distance of the single race
    time = int("".join([item for item in all_lines[0].split(":")[-1].split(" ") if item != ""]))
    distance = int("".join([item for item in all_lines[1].split(":")[-1].split(" ") if item != ""]))

    # - Going through each button_press_time possible takes the longest time of the
    #   whole program
    race_wins = 0
    for button_hold_time in range(time+1):
        # - Using the function, calculate the distance for the current time of holding
        #   the button
        # - If the distance was further, then that counts as a win
        # - Used Desmos to figure out the relationship between the total time of the
        #   race and the distance that the toy boat travels
        # - The relationship would be:
        #   distance_travelled = -(button_press_time - (total_time / 2))^2 + ((total_time / 2))^2
        distance_travelled = -((button_hold_time - (time / 2))**2) + ((time / 2)**2)
        if distance_travelled > distance:
            race_wins += 1

    print(race_wins)

part1()
part2() # Takes ~10 seconds to compute
