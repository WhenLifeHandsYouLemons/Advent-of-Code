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
        area = 1
        self.checked = True

        for i in self.neighbours:
            if i != None and i.plot_symbol == self.plot_symbol and not i.checked:
                area += i.findArea()

        return area

    def findPerimeterPart1(self) -> int:
        perimeter = 0
        self.checked = True

        for i in self.neighbours:
            if i == None or i.plot_symbol != self.plot_symbol:
                perimeter += 1
            elif i != None and i.plot_symbol == self.plot_symbol and not i.checked:
                perimeter += i.findPerimeterPart1()

        return perimeter

    def findPerimeterPart2(self) -> int:
        perimeter = 0
        # self.checked = True

        # for i in self.neighbours:
        #     if i == None or i.plot_symbol != self.plot_symbol:
        #         perimeter += 1
        #     elif i != None and i.plot_symbol == self.plot_symbol and not i.checked:
        #         perimeter += i.findPerimeterPart2()

        return perimeter

    def calculatePricePart1(self) -> int:
        price = 1

        price *= self.findArea()
        self.resetRegion()
        price *= self.findPerimeterPart1()

        return price

    def calculatePricePart2(self) -> int:
        price = 1

        price *= self.findArea()
        self.resetRegion()
        price *= self.findPerimeterPart2()

        return price

    def resetRegion(self) -> None:
        self.checked = False

        for i in self.neighbours:
            if i != None and i.plot_symbol == self.plot_symbol and i.checked:
                i.resetRegion()

    def propagateCheck(self) -> None:
        self.checked = True

        for i in self.neighbours:
            if i != None and i.plot_symbol == self.plot_symbol and not i.checked:
                i.propagateCheck()

    # Overriding printing
    def __str__(self) -> str:
        return str(self.plot_symbol)

    # Overriding representation in lists
    def __repr__(self) -> str:
        return str(self.plot_symbol)

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
        all_plots[plot_no].propagateCheck()

        remove_plot_no = plot_no+1
        while remove_plot_no < len(all_plots):
            if all_plots[remove_plot_no].checked:
                all_plots.pop(remove_plot_no)
            else:
                remove_plot_no += 1

        plot_no += 1

    for plot in all_plots:
        plot.resetRegion()

    # Go through each region and find the price
    total_price = 0
    for plot in all_plots:
        total_price += plot.calculatePricePart1()

    return total_price

def part2():
    global all_lines
    line_no = 0

    farm: list[list[Plot]] = []
    all_plots: list[Plot] = []

    # Get entire farm grid
    while line_no != len(all_lines):
        line = all_lines[line_no]

        farm.append([Plot(i, line_no, line[i]) for i in range(len(line))])

        line_no += 1

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
        all_plots[plot_no].propagateCheck()

        remove_plot_no = plot_no+1
        while remove_plot_no < len(all_plots):
            if all_plots[remove_plot_no].checked:
                all_plots.pop(remove_plot_no)
            else:
                remove_plot_no += 1

        plot_no += 1

    for plot in all_plots:
        plot.resetRegion()

    # Go through each region and find the price
    total_price = 0
    for plot in all_plots:
        total_price += plot.calculatePricePart2()

    return total_price

print('Part 1 answer:', part1())
print('Part 2 answer:', part2())
