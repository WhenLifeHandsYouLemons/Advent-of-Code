'''
Advent of Code: Day 12
'''
from helper_methods import *

all_lines = readfile('2024/data.txt')

class Plot():
    def __init__(self, x: int, y: int, symbol: str):
        self.pos: tuple[int, int] = (x, y)
        self.plot_symbol: str = symbol
        #                              Up    Right Down  Left
        self.neighbours: list[Plot] = [None, None, None, None]
        self.checked = False

    def addNeighbours(self, neighbour, side: int) -> None:
        self.neighbours[side] = neighbour

    def findArea(self) -> int:
        area = 0

        return area

    def findPerimeter(self) -> int:
        perimeter = 0

        return perimeter

    def calculatePrice(self) -> int:
        price = 1

        price *= self.findArea()
        self.reset()
        price *= self.findPerimeter()

        return price

    def reset(self) -> None:
        for i in self.neighbours:
            if i != None and i.checked:
                i.reset()

    def propagateCheck(self, start) -> None:
        self.checked = True

        for i in self.neighbours:
            if i != None and self != start and i.plot_symbol == self.plot_symbol:
                i.propagateCheck(start)

    # Overriding printing
    def __str__(self) -> str:
        return self.plot_symbol

    # Overriding representation in lists
    def __repr__(self) -> str:
        return self.plot_symbol

    # Overriding equality check
    def __eq__(self, value) -> bool:
        return f"{self.plot_symbol}{self.pos}" == value

def part1():
    global all_lines
    line_no = 0

    farm: list[list[Plot]] = []
    all_plots: list[Plot] = []

    # Get entire farm grid
    while line_no != len(all_lines):
        line = all_lines[line_no]

        farm.append([Plot(i, line_no, line[i]) for i in range(len(line))])

        line_no += 1

    gridPrint(farm)

    # Get all plots
    for row in range(len(farm)):
        for col in range(len(farm[row])):
            if row != 0:
                farm[row][col].addNeighbours(farm[row-1][col], 0)
            if row != len(farm) - 1:
                farm[row][col].addNeighbours(farm[row+1][col], 2)
            if col != 0:
                farm[row][col].addNeighbours(farm[row][col-1], 3)
            if col != len(farm[row]) - 1:
                farm[row][col].addNeighbours(farm[row][col+1], 1)

            all_plots.append(farm[row][col])

    # Find all regions by propagating check through each region and removing all but one plot per region
    plot_no = 0
    while plot_no < len(all_plots):
        # Propagate plot check
        all_plots[plot_no].propagateCheck(all_plots[plot_no])

        remove_plot_no = plot_no
        while remove_plot_no < len(all_plots):
            if all_plots[remove_plot_no].checked:
                all_plots.pop(remove_plot_no)

            remove_plot_no += 1

        plot_no += 1

    arrayPrint(all_plots, spacing=" ")

    # Go through each region and find

    return ""

def part2():
    global all_lines
    line_no = 0

    while line_no != len(all_lines):
        line = all_lines[line_no]

        line_no += 1

    return ""

print('Part 1 answer:', part1())
print('Part 2 answer:', part2())
