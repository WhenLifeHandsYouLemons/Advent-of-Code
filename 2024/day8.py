'''
Advent of Code: Day 8
'''
from helper_methods import *

all_lines = readfile('2024/data.txt')

class Antenna:
    def __init__(self, x: int, y: int, antenna_symbol: str):
        self.x = x
        self.y = y
        self.symbol = antenna_symbol

    def __str__(self) -> str:
        return self.symbol

class AntennaGroup:
    def __init__(self, antenna_group_symbol: str, *antenna: Antenna):
        self.antennae = list(antenna)
        self.symbol = antenna_group_symbol

    def addToGroup(self, antenna: Antenna) -> None:
        if str(antenna) == str(self):
            self.antennae.append(antenna)

    def findAntinodes(self, part1: bool, upper_x: int, upper_y: int, lower_x: int = 0, lower_y: int = 0) -> list[tuple]:
        self.upper = (upper_x, upper_y)
        self.lower = (lower_x, lower_y)

        all_antinodes = []
        for i in range(len(self.antennae)):
            for j in range(i+1, len(self.antennae)):
                if part1:
                    for antinode in self.findAntinodePart1(self.antennae[i], self.antennae[j]):
                        all_antinodes.append(antinode)
                else:
                    for antinode in self.findAntinodePart2(self.antennae[i], self.antennae[j]):
                        all_antinodes.append(antinode)

        return all_antinodes

    def findAntinodePart1(self, antenna_1: Antenna, antenna_2: Antenna) -> list[tuple]:
        # Calculate horizontal and vertical distance between the two antennae
        d_distance = (antenna_1.x - antenna_2.x, antenna_1.y - antenna_2.y)

        # Subtract the distances from antenna_1 and add the distances to antenna_2
        antinode_1 = (antenna_1.x + d_distance[0], antenna_1.y + d_distance[1])
        antinode_2 = (antenna_2.x - d_distance[0], antenna_2.y - d_distance[1])

        # Check if they are in the bounds given
        valid_antinodes = []
        if antinode_1[0] >= self.lower[0] and antinode_1[0] < self.upper[0] and antinode_1[1] >= self.lower[1] and antinode_1[1] < self.upper[1]:
            valid_antinodes.append(antinode_1)
        if antinode_2[0] >= self.lower[0] and antinode_2[0] < self.upper[0] and antinode_2[1] >= self.lower[1] and antinode_2[1] < self.upper[1]:
            valid_antinodes.append(antinode_2)

        return valid_antinodes

    def findAntinodePart2(self, antenna_1: Antenna, antenna_2: Antenna) -> list[tuple]:
        # Calculate horizontal and vertical distance between the two antennae
        d_distance = (antenna_1.x - antenna_2.x, antenna_1.y - antenna_2.y)

        # Subtract the distances from antenna_2 and add the distances to antenna_1
        valid_antinodes = []

        cur_pos = (antenna_1.x - d_distance[0], antenna_1.y - d_distance[1])
        while cur_pos[0] >= self.lower[0] and cur_pos[0] < self.upper[0] and cur_pos[1] >= self.lower[1] and cur_pos[1] < self.upper[1]:
            valid_antinodes.append(cur_pos)
            cur_pos = (cur_pos[0] - d_distance[0], cur_pos[1] - d_distance[1])

        cur_pos = (antenna_2.x + d_distance[0], antenna_2.y + d_distance[1])
        while cur_pos[0] >= self.lower[0] and cur_pos[0] < self.upper[0] and cur_pos[1] >= self.lower[1] and cur_pos[1] < self.upper[1]:
            valid_antinodes.append(cur_pos)
            cur_pos = (cur_pos[0] + d_distance[0], cur_pos[1] + d_distance[1])

        return valid_antinodes

    def __str__(self) -> str:
        return self.symbol

def part1():
    global all_lines
    line_no = 0

    grid = []
    while line_no != len(all_lines):
        line = all_lines[line_no]

        grid.append([i for i in line])

        line_no += 1

    antenna_groups: list[AntennaGroup] = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            grid_symbol = grid[y][x]
            if grid_symbol != ".":
                new = True
                for i in range(len(antenna_groups)):
                    if grid_symbol == str(antenna_groups[i]):
                        antenna_groups[i].addToGroup(Antenna(x, y, grid_symbol))
                        new = False
                if new:
                    antenna_groups.append(AntennaGroup(grid_symbol, Antenna(x, y, grid_symbol)))

    all_antinodes = []
    for group in antenna_groups:
        for antinode in group.findAntinodes(True, len(grid), len(grid[0])):
            if antinode not in all_antinodes:
                all_antinodes.append(antinode)

    total_antinodes = len(all_antinodes)

    return total_antinodes

def part2():
    global all_lines
    line_no = 0

    grid = []
    while line_no != len(all_lines):
        line = all_lines[line_no]

        grid.append([i for i in line])

        line_no += 1

    antenna_groups: list[AntennaGroup] = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            grid_symbol = grid[y][x]
            if grid_symbol != ".":
                new = True
                for i in range(len(antenna_groups)):
                    if grid_symbol == str(antenna_groups[i]):
                        antenna_groups[i].addToGroup(Antenna(x, y, grid_symbol))
                        new = False
                if new:
                    antenna_groups.append(AntennaGroup(grid_symbol, Antenna(x, y, grid_symbol)))

    all_antinodes = []
    for group in antenna_groups:
        for antinode in group.findAntinodes(False, len(grid), len(grid[0])):
            if antinode not in all_antinodes:
                all_antinodes.append(antinode)

    total_antinodes = len(all_antinodes)

    return total_antinodes

print('Part 1 answer:', part1())
print('Part 2 answer:', part2())
