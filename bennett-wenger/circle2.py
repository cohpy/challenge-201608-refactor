# refactoring of circle2.py
# cohpy challenge for August 2016
#
# Bennett Wenger
# using Debian 8.5
# Python 3.4.2

# imports
from tkinter import Tk, Canvas, PhotoImage, mainloop
from math import sin
from time import sleep

# sys.argv produces 'index out of range' error
# going a different direction
#from sys import argv

# default window dimensions
WIDTH, HEIGHT = 640, 480

# image parameters
CORNA = int(1)
CORNB = int(2)
SIDE = float(4)

window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#000000")
canvas.pack()
img = PhotoImage(width=WIDTH, height=HEIGHT)
canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")

for i in range(WIDTH):
    for j in range(HEIGHT):
        x = CORNA + (SIDE * (i/100.0))
        y = CORNB + (SIDE * (j/100.0))
        z = x*x + y*y
        c = int(z)
        if c % 2 == 0:
            img.put("#ffffff", (i,j))

mainloop()
