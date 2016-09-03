#!/usr/bin/env python3

from sys import argv
from tkinter import Tk, Canvas, PhotoImage, mainloop

BLACK = '#000000'
RED = '#ff0000'
GREEN = '#00ff00'
BLUE = '#0000ff'
WHITE = '#ffffff'

COLORS = (BLACK, RED, GREEN, BLUE, WHITE)

BACKGROUND_COLOR = BLACK
FOREGROUND_COLOR = WHITE


def color(xx, yy):
    z = xx + yy
    c = int(z)
    if True:
        return COLORS[c % len(COLORS)]
    else:
        if c % 2 == 0:
            return FOREGROUND_COLOR
        else:
            return BACKGROUND_COLOR


def main(argv):
    corna = int(argv[1])
    cornb = int(argv[2])
    side = float(argv[3])

    window = Tk()
    screen_size = window.winfo_screenwidth(), window.winfo_screenheight()
    width, height = screen_size
    # print(screen_size)
    canvas = Canvas(window, width=width, height=height, bg=BACKGROUND_COLOR)
    canvas.pack()
    img = PhotoImage(width=width, height=height)
    canvas.create_image((width/2, height/2), image=img, state="normal")

    x_squareds = [x*x for x in [
        corna + (side * (i/100.0))
        for i in range(width)]]

    y_squareds = [y*y for y in [
        cornb + (side * (j/100.0))
        for j in range(height)]]

    lines = []
    for yy in y_squareds:
        horizontal_line = '{' + ' '.join(
            color(xx, yy)
            for xx in x_squareds) + '}'
        lines.append(horizontal_line)
    img.put(' '.join(lines))

    mainloop()


if __name__ == '__main__':
    main(argv)
