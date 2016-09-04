# Bennett Wenger
# Python 3.4

# refactoring of circle2.py
# cohpy challenge for August 2016

# added comments
# general bugfixes
# simplified variable names
# lower > UPPER
# '' > ""
# * imports
# 4:3 aspect ratio
# randomized parameters
# easy color names
# window name

# imports
from tkinter import *
from math import *
from random import *

# default dimensions
w = 400
h = 300

# image parameters
a = randrange(1, 8, 1)
b = randrange(1, 8, 1)
s = randrange(1, 8, 1)

# create
window = Tk()
window.wm_title('fun image')
canvas = Canvas(window, width=w, height=h, bg='black')
canvas.pack()
img = PhotoImage(width=w, height=h)
canvas.create_image((w/2, h/2), image=img, state='normal')

# draw
for i in range(w):
    for j in range(h):
        x = a + (s * (i/100.0))
        y = b + (s * (j/100.0))
        z = x*x + y*y
        c = int(z)
        if c % 2 == 0:
            img.put('white', (i,j))
            
# main
mainloop()

# end of file
