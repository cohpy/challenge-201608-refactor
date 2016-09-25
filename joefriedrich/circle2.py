from tkinter import Tk, Canvas, PhotoImage, mainloop
from math import sin
from time import sleep
from sys import argv

WIDTH, HEIGHT = 640, 480

CORNA = int(argv[1])
CORNB = int(argv[2])
SIDE = float(argv[3])

window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#000000")
canvas.pack()
img = PhotoImage(width=WIDTH, height=HEIGHT)
canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")

for column in range(WIDTH):
    for row in range(HEIGHT):
        x = CORNA + (SIDE * (column/100.0))
        y = CORNB + (SIDE * (row/100.0))
        z = x*x + y*y
        if int(z) % 2 == 0:
            img.put("#ffffff", (column,row))

mainloop()
