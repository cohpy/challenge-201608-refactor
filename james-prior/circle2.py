#!/usr/bin/env python3

from sys import argv
from tkinter import Tk, Canvas, PhotoImage, mainloop

WIDTH, HEIGHT = 640, 480


def main(argv):
    corna = int(argv[1])
    cornb = int(argv[2])
    side = float(argv[3])

    window = Tk()
    canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#000000")
    canvas.pack()
    img = PhotoImage(width=WIDTH, height=HEIGHT)
    canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")

    for i in range(WIDTH):
        for j in range(HEIGHT):
            x = corna + (side * (i/100.0))
            y = cornb + (side * (j/100.0))
            z = x*x + y*y
            c = int(z)
            if c % 2 == 0:
                img.put("#ffffff", (i,j))

    mainloop()


if __name__ == '__main__':
    main(argv)
