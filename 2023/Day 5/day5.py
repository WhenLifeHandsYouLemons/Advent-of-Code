"""
Advent of Code: Day 5
"""

all_lines = []

with open('2023/Day 5/data.txt', 'r') as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)
# print(all_lines)

def part1():
    class Map():
        def __init__(self) -> None:
            self.map_table = {}
            self.maps = []

        # Gives smallest destination val given source val
        def findClosestMappingValue(self, n) -> int:
            self.map_table = dict(sorted(self.map_table.items()))
            # Go through each item in dict
            prev_val = -1
            for src, dest in self.map_table.items():
                # If it is our current potential range
                if src > n:
                    src = prev_val
                    if src == -1:
                        return n
                    val = self.map_table[src]
                    # Check if different of range is in the length
                    if n - src <= val[1]:
                        return val[0] + n - src
                    else:
                        return n
                # Store previous val
                prev_val = src

            src = prev_val
            if src == -1:
                return n
            val = self.map_table[src]
            # Check if different of range is in the length
            if n - src <= val[1]:
                return val[0] + n - src
            else:
                return n

        # Adds the given items to the map table
        def addMaps(self, dest_range_start, source_range_start, length) -> None:
            self.maps.append([dest_range_start, source_range_start, length])
            self.map_table[source_range_start] = [dest_range_start, length]

    global all_lines
    line_no = 0

    seeds = [int(i) for i in all_lines[0].split(": ")[-1].split(" ")]

    seed_to_soil_map = Map()
    soil_to_fertilizer_map = Map()
    fertilizer_to_water_map = Map()
    water_to_light_map = Map()
    light_to_temperature_map = Map()
    temperature_to_humidity_map = Map()
    humidity_to_location_map = Map()

    seed_to_soil_line = 0
    soil_to_fertilizer_line = 0
    fertilizer_to_water_line = 0
    water_to_light_line = 0
    light_to_temperature_line = 0
    temperature_to_humidity_line = 0
    humidity_to_location_line = 0

    # Get where each map starts
    while line_no != len(all_lines):
        line = all_lines[line_no]
        if "seed-to-soil map" in line:
            seed_to_soil_line = line_no
        elif "soil-to-fertilizer map" in line:
            soil_to_fertilizer_line = line_no
        elif "fertilizer-to-water map" in line:
            fertilizer_to_water_line = line_no
        elif "water-to-light map" in line:
            water_to_light_line = line_no
        elif "light-to-temperature map" in line:
            light_to_temperature_line = line_no
        elif "temperature-to-humidity map" in line:
            temperature_to_humidity_line = line_no
        elif "humidity-to-location map" in line:
            humidity_to_location_line = line_no
        line_no += 1

    # Get the lines for the seed_to_soil map
    for pos, val in enumerate(all_lines):
        if pos > seed_to_soil_line:
            if val == "":
                break
            item = val.split(" ")
            seed_to_soil_map.addMaps(int(item[0]), int(item[1]), int(item[2]))

    # Get the lines for the soil_to_fertilizer map
    for pos, val in enumerate(all_lines):
        if pos > soil_to_fertilizer_line:
            if val == "":
                break
            item = val.split(" ")
            soil_to_fertilizer_map.addMaps(int(item[0]), int(item[1]), int(item[2]))

    # Get the lines for the fertilizer_to_water map
    for pos, val in enumerate(all_lines):
        if pos > fertilizer_to_water_line:
            if val == "":
                break
            item = val.split(" ")
            fertilizer_to_water_map.addMaps(int(item[0]), int(item[1]), int(item[2]))

    # Get the lines for the water_to_light map
    for pos, val in enumerate(all_lines):
        if pos > water_to_light_line:
            if val == "":
                break
            item = val.split(" ")
            water_to_light_map.addMaps(int(item[0]), int(item[1]), int(item[2]))

    # Get the lines for the light_to_temperature map
    for pos, val in enumerate(all_lines):
        if pos > light_to_temperature_line:
            if val == "":
                break
            item = val.split(" ")
            light_to_temperature_map.addMaps(int(item[0]), int(item[1]), int(item[2]))

    # Get the lines for the temperature_to_humidity map
    for pos, val in enumerate(all_lines):
        if pos > temperature_to_humidity_line:
            if val == "":
                break
            item = val.split(" ")
            temperature_to_humidity_map.addMaps(int(item[0]), int(item[1]), int(item[2]))

    # Get the lines for the humidity_to_location map
    for pos, val in enumerate(all_lines):
        if pos > humidity_to_location_line:
            if val == "":
                break
            item = val.split(" ")
            humidity_to_location_map.addMaps(int(item[0]), int(item[1]), int(item[2]))

    # Find closest locations
    locations = []
    for seed in seeds:
        # Get closest soil val
        soil = seed_to_soil_map.findClosestMappingValue(seed)
        # Get closest fert val
        fert = soil_to_fertilizer_map.findClosestMappingValue(soil)
        # Get closest water val
        water = fertilizer_to_water_map.findClosestMappingValue(fert)
        # Get closest light val
        light = water_to_light_map.findClosestMappingValue(water)
        # Get closest temp val
        temp = light_to_temperature_map.findClosestMappingValue(light)
        # Get closest humid val
        humid = temperature_to_humidity_map.findClosestMappingValue(temp)
        # Get closest location val
        location = humidity_to_location_map.findClosestMappingValue(humid)
        # Store location val
        locations.append(location)

    print(min(locations))

def part2():
    class Map():
        def __init__(self) -> None:
            self.map_table = {}
            self.maps = []

        # Gives smallest destination val given source val
        def findClosestMappingValue(self, n) -> int:
            self.map_table = dict(sorted(self.map_table.items()))
            # Go through each item in dict
            prev_val = -1
            for src, dest in self.map_table.items():
                # If it is our current potential range
                if src > n:
                    src = prev_val
                    if src == -1:
                        return n
                    val = self.map_table[src]
                    # Check if different of range is in the length
                    if n - src <= val[1]:
                        return val[0] + n - src
                    else:
                        return n
                # Store previous val
                prev_val = src

            src = prev_val
            if src == -1:
                return n
            val = self.map_table[src]
            # Check if different of range is in the length
            if n - src <= val[1]:
                return val[0] + n - src
            else:
                return n

        # Adds the given items to the map table
        def addMaps(self, dest_range_start, source_range_start, length) -> None:
            self.maps.append([dest_range_start, source_range_start, length])
            self.map_table[source_range_start] = [dest_range_start, length]

    global all_lines
    line_no = 0

    values = []
    for i in all_lines[0].split(": ")[-1].split(" "):
        values.append(int(i))

    seeds = []
    for i in range(0, len(values), 2):
        for j in range(values[i+1]):
            seeds.append(values[i]+j)

    seed_to_soil_map = Map()
    soil_to_fertilizer_map = Map()
    fertilizer_to_water_map = Map()
    water_to_light_map = Map()
    light_to_temperature_map = Map()
    temperature_to_humidity_map = Map()
    humidity_to_location_map = Map()

    seed_to_soil_line = 0
    soil_to_fertilizer_line = 0
    fertilizer_to_water_line = 0
    water_to_light_line = 0
    light_to_temperature_line = 0
    temperature_to_humidity_line = 0
    humidity_to_location_line = 0

    print("Storing mappings...")

    # Get where each map starts
    while line_no != len(all_lines):
        line = all_lines[line_no]
        if "seed-to-soil map" in line:
            seed_to_soil_line = line_no
        elif "soil-to-fertilizer map" in line:
            soil_to_fertilizer_line = line_no
        elif "fertilizer-to-water map" in line:
            fertilizer_to_water_line = line_no
        elif "water-to-light map" in line:
            water_to_light_line = line_no
        elif "light-to-temperature map" in line:
            light_to_temperature_line = line_no
        elif "temperature-to-humidity map" in line:
            temperature_to_humidity_line = line_no
        elif "humidity-to-location map" in line:
            humidity_to_location_line = line_no
        line_no += 1

    print("Found line starts.")

    # Get the lines for the seed_to_soil map
    for pos, val in enumerate(all_lines):
        if pos > seed_to_soil_line:
            if val == "":
                break
            item = val.split(" ")
            seed_to_soil_map.addMaps(int(item[0]), int(item[1]), int(item[2]))

    print("Mapped seeds to soil.")

    # Get the lines for the soil_to_fertilizer map
    for pos, val in enumerate(all_lines):
        if pos > soil_to_fertilizer_line:
            if val == "":
                break
            item = val.split(" ")
            soil_to_fertilizer_map.addMaps(int(item[0]), int(item[1]), int(item[2]))

    print("Mapped soil to fertiliser.")

    # Get the lines for the fertilizer_to_water map
    for pos, val in enumerate(all_lines):
        if pos > fertilizer_to_water_line:
            if val == "":
                break
            item = val.split(" ")
            fertilizer_to_water_map.addMaps(int(item[0]), int(item[1]), int(item[2]))

    print("Mapped fertiliser to water.")

    # Get the lines for the water_to_light map
    for pos, val in enumerate(all_lines):
        if pos > water_to_light_line:
            if val == "":
                break
            item = val.split(" ")
            water_to_light_map.addMaps(int(item[0]), int(item[1]), int(item[2]))

    print("Mapped water to light.")

    # Get the lines for the light_to_temperature map
    for pos, val in enumerate(all_lines):
        if pos > light_to_temperature_line:
            if val == "":
                break
            item = val.split(" ")
            light_to_temperature_map.addMaps(int(item[0]), int(item[1]), int(item[2]))

    print("Mapped light to temperature.")

    # Get the lines for the temperature_to_humidity map
    for pos, val in enumerate(all_lines):
        if pos > temperature_to_humidity_line:
            if val == "":
                break
            item = val.split(" ")
            temperature_to_humidity_map.addMaps(int(item[0]), int(item[1]), int(item[2]))

    print("Mapped temperature to humidity.")

    # Get the lines for the humidity_to_location map
    for pos, val in enumerate(all_lines):
        if pos > humidity_to_location_line:
            if val == "":
                break
            item = val.split(" ")
            humidity_to_location_map.addMaps(int(item[0]), int(item[1]), int(item[2]))

    print("Completed.\nFinding locations...")

    # Find closest locations
    locations = []
    for seed in seeds:
        # Get closest soil val
        soil = seed_to_soil_map.findClosestMappingValue(seed)
        # Get closest fert val
        fert = soil_to_fertilizer_map.findClosestMappingValue(soil)
        # Get closest water val
        water = fertilizer_to_water_map.findClosestMappingValue(fert)
        # Get closest light val
        light = water_to_light_map.findClosestMappingValue(water)
        # Get closest temp val
        temp = light_to_temperature_map.findClosestMappingValue(light)
        # Get closest humid val
        humid = temperature_to_humidity_map.findClosestMappingValue(temp)
        # Get closest location val
        location = humidity_to_location_map.findClosestMappingValue(humid)
        # Store location val
        locations.append(location)

    print(min(locations))

part1()
part2() # Doesn't work yet as it takes too long
