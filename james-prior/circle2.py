#!/usr/bin/env python3
'''
arguments may be expressions

    available values:
        width (unit is 1 pixel)
        height (unit is 1 pixel)
        pi
        e
        math.*

circle2.py 0 0 .001
circle2.py 0 0 .003
circle2.py 0 0 .01
circle2.py 0 0 .17
circle2.py 0 0 .34
circle2.py 0 0 4/9
circle2.py 0 0 .45
circle2.py 0 0 .8
circle2.py 0 0 .81
circle2.py 0 0 .801
circle2.py 0 0 .8001
circle2.py 0 0 .80001
circle2.py 0 0 .9
circle2.py 0 0 .99
circle2.py 0 0 .999
circle2.py 0 0 .9999
circle2.py 0 0 .99999
circle2.py 0 0 .999999
circle2.py 0 0 1
circle2.py 0 0 1.1
circle2.py 0 0 1.01
circle2.py 0 0 1.001
circle2.py 0 0 1.0001
circle2.py 0 0 1.00001
circle2.py 0 0 1.000001
circle2.py 0 0 1.0000001
circle2.py 0 0 1/3
circle2.py 0 0 1/width
circle2.py 0 0 1/pi
circle2.py 0 0 1/e
circle2.py 0 0 'math.sqrt(1/e)'
circle2.py 0 0 'math.sqrt(1/2)'
circle2.py 0 0 'math.sqrt(1/pi)'
circle2.py 0 0 'math.sqrt(1/5)'
circle2.py 0 0 'math.sqrt(2/5)'
circle2.py 0 0 'math.sqrt(3/5)'
circle2.py 0 0 'math.sqrt(4/5)'
circle2.py 0 0 'math.sqrt(6/5)'
circle2.py 0 0 'math.sqrt(7/5)'
circle2.py 0 0 'math.sqrt(1/7)'
circle2.py 0 0 'math.sqrt(2/7)'
circle2.py 0 0 'math.sqrt(3/7)'
circle2.py 0 0 'math.sqrt(4/7)'
circle2.py 0 0 'math.sqrt(5/7)'
circle2.py 0 0 'math.sqrt(6/7)'
circle2.py 0 0 'math.sqrt(8/7)'
circle2.py 0 0 'math.sqrt(88/7)'
circle2.py 0 0 'math.sqrt(888/7)'
circle2.py 0 0 'math.sqrt(8888/7)'
circle2.py 0 0 'math.sqrt(88888/7)'
circle2.py 0 0 'math.sqrt(.17)'
circle2.py width/2 height/2  'e/(min(width, height)/2)'
'''

from sys import argv
from tkinter import Tk, Canvas, PhotoImage, mainloop
from math import pi, e
import math

BLACK = '#000000'
RED = '#ff0000'
GREEN = '#00ff00'
BLUE = '#0000ff'
WHITE = '#ffffff'

COLORS = (WHITE, BLACK)
COLORS = (BLACK, RED, GREEN, BLUE, WHITE)


def color(xx, yy):
    z = xx + yy
    c = int(z)
    return COLORS[c % len(COLORS)]


def main(argv):
    window = Tk()
    screen_size = window.winfo_screenwidth(), window.winfo_screenheight()
    width, height = screen_size
    corner_x, corner_y, m = map(eval, argv[1:])
    # print(screen_size)
    canvas = Canvas(window, width=width, height=height)
    canvas.pack()
    img = PhotoImage(width=width, height=height)
    canvas.create_image((width/2, height/2), image=img, state="normal")

    x_squareds = [(m * (x-corner_x))**2 for x in range(width)]
    y_squareds = [(m * (y-corner_y))**2 for y in range(height)]

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
