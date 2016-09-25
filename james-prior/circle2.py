#!/usr/bin/env python3
'''
circle2.py [m [n_colors [corner_x [corner_y]]]]

    all arguments are optional
    default values
        m           1/min(width, height)
        n_colors    len(COLORS) (5)
        corner_x    0. (left edge)
        corner_y    0. (top edge)

    arguments may be expressions

        available values:
            width (unit is 1 pixel)
            height (unit is 1 pixel)
            pi
            e
            math.*

circle2.py
circle2.py '1/min(width, height)'
circle2.py '1/(min(width, height)/2)' width/2 height/2
circle2.py 1/width
circle2.py 1/height
circle2.py .001
circle2.py .003
circle2.py .01
circle2.py .17
circle2.py .34
circle2.py 4/9
circle2.py .45
circle2.py .8
circle2.py .81
circle2.py .801
circle2.py .8001
circle2.py .80001
circle2.py .9
circle2.py .99
circle2.py .999
circle2.py .9999
circle2.py .99999
circle2.py .999999
circle2.py 1
circle2.py 1.1
circle2.py 1.01
circle2.py 1.001
circle2.py 1.0001
circle2.py 1.00001
circle2.py 1.000001
circle2.py 1.0000001
circle2.py 1/3
circle2.py 1/pi
circle2.py 1/e
circle2.py 'math.sqrt(1/e)'
circle2.py 'math.sqrt(1/2)'
circle2.py 'math.sqrt(1/pi)'
circle2.py 'math.sqrt(1/5)'
circle2.py 'math.sqrt(2/5)'
circle2.py 'math.sqrt(3/5)'
circle2.py 'math.sqrt(4/5)'
circle2.py 'math.sqrt(6/5)'
circle2.py 'math.sqrt(7/5)'
circle2.py 'math.sqrt(1/7)'
circle2.py 'math.sqrt(1/7)' 1
circle2.py 'math.sqrt(1/7)' 2
circle2.py 'math.sqrt(1/7)' e
circle2.py 'math.sqrt(1/7)' 3
circle2.py 'math.sqrt(1/7)' pi
circle2.py 'math.sqrt(1/7)' 4
circle2.py 'math.sqrt(1/7)' 5
circle2.py 'math.sqrt(1/7)' 36
circle2.py 'math.sqrt(1/7)' -36
circle2.py 'math.sqrt(1/7)' 360
circle2.py 'math.sqrt(1/7)' 10000
circle2.py 'math.sqrt(2/7)'
circle2.py 'math.sqrt(3/7)'
circle2.py 'math.sqrt(4/7)'
circle2.py 'math.sqrt(5/7)'
circle2.py 'math.sqrt(6/7)'
circle2.py 'math.sqrt(8/7)'
circle2.py 'math.sqrt(88/7)'
circle2.py 'math.sqrt(888/7)'
circle2.py 'math.sqrt(8888/7)'
circle2.py 'math.sqrt(88888/7)'
circle2.py 'math.sqrt(.17)'
circle2.py 'math.sqrt(.17)' 1
circle2.py 'math.sqrt(.17)' 2
circle2.py 'math.sqrt(.17)' e
circle2.py 'math.sqrt(.17)' 3
circle2.py 'math.sqrt(.17)' pi
circle2.py 'math.sqrt(.17)' 4
circle2.py 'math.sqrt(.17)' 5
circle2.py 'e/(min(width, height)/2)' width/2 height/2
'''

'''
python3 -m venv env3
source env3/bin/activate
pip install colour
'''

from sys import argv
from tkinter import Tk, Canvas, PhotoImage, mainloop
from math import pi, e
import math

from colour import Color


def hex_24bit_color(color):
    color_256_rgb = tuple(int(0x100 * primary) for primary in color.rgb)
    color_255_rgb = tuple(min(0x100-1, primary) for primary in color_256_rgb)
    return '#%02x%02x%02x' % color_255_rgb


def make_color_func(n_colors):
    red = 0/3
    green = 1/3
    blue = 2/3
    colors = []
    if n_colors > 0:
        colors = [Color('black'), Color('white')][:n_colors]
    else:
        n_colors = -n_colors
    if n_colors > len(colors):
        n_colors -= len(colors)
        colors.extend(
            Color(hue=((red-i/n_colors)%1), saturation=1, luminance=0.5)
            for i in range(n_colors)
        )
    hex_colors = [hex_24bit_color(color) for color in colors]
    # print(repr(colors), repr(hex_colors))

    def get_color(xx, yy):
        z = xx + yy
        c = int(z)
        return hex_colors[int(c % len(hex_colors))]

    return get_color


def parse_args(screen_size, m=None, n_colors=2, corner_x=0., corner_y=0.):
    if m is None:
        m = 1/min(*screen_size)
    return m, n_colors, corner_x, corner_y


def main(argv):
    window = Tk()
    screen_size = window.winfo_screenwidth(), window.winfo_screenheight()
    # print(screen_size)
    width, height = screen_size
    arg_values = list(map(eval, argv[1:]))
    # print(repr(arg_values))
    m, n_colors, corner_x, corner_y = parse_args(screen_size, *arg_values)
    get_color = make_color_func(n_colors)
    canvas = Canvas(window, width=width, height=height)
    canvas.pack()
    img = PhotoImage(width=width, height=height)
    canvas.create_image((width/2, height/2), image=img, state="normal")

    x_squareds = [(m * (x-corner_x))**2 for x in range(width)]
    y_squareds = [(m * (y-corner_y))**2 for y in range(height)]

    lines = []
    for yy in y_squareds:
        horizontal_line = '{' + ' '.join(
            get_color(xx, yy)
            for xx in x_squareds) + '}'
        lines.append(horizontal_line)
    img.put(' '.join(lines))

    mainloop()


if __name__ == '__main__':
    main(argv)
