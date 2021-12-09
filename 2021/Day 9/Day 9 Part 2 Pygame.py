"""
Made by - Sooraj.S
GitHub - https://github.com/WhenLifeHandsYouLemons
Twitter - https://twitter.com/LemonsHandYou
Instagram - https://www.instagram.com/whenlifehandsyoulemons1/
Latest Release - https://github.com/WhenLifeHandsYouLemons/What is the repository name?/releases
"""

"""
IMPORTS
"""
import os
import sys
import pygame

"""
FILE SEARCHING USED IN '.exe' FORMAT
"""
def get_true_filename(filename):
    try:
        base = sys._MEIPASS
    except Exception:
        base = os.path.abspath('.')
    return os.path.join(base, filename)

"""
APP WINDOW
"""
bg_colour = 255, 0, 0
window_height = 500
window_width = 500
WIN = pygame.display.set_mode((window_width, window_height))
WIN.fill(bg_colour)

"""
VARIABLES
"""
threshold = 9
scale = 5
shift_x = 0
shift_y = 0
all_lines = []
line_no = 0

with open("2021/Day 9/Day 9 Resources.txt", "r") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        all_lines.append(line)

"""
SETS FPS
"""
clock = pygame.time.Clock()

"""
MAIN LOOP
"""
RUNNING_WINDOW = True

while RUNNING_WINDOW == True:
    clock.tick(30)

    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pos()
    print(mouse[0], mouse[1])

    row_no = 0
    while row_no < len(all_lines):
        row_chose = all_lines[row_no]
        row = []

        # Organise the row
        for number in row_chose:
            row.append(number)

        column_no = 0
        while column_no < len(row):
            current_no = int(row[column_no])
            if current_no >= threshold:
                current_no = 9
            pygame.draw.rect(WIN, (current_no*28, current_no*28, 255), ((column_no+shift_x)*scale, (row_no+shift_y)*scale, scale, scale))
            column_no += 1

        row_no += 1

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING_WINDOW = False
            pygame.quit()
            sys.exit()

sys.exit()
