"""
circle2.py - from John E. Connett's "CIRCLE^2".

Deeptinker refactorings:

1.  Added code to time how long each run takes.
    RESEULT: N/A

2.  Reduce the number of times that i/100.0 is calculatated.
    Result negligible.
"""
from tkinter import Tk, Canvas, PhotoImage, mainloop
from sys import argv

from JPTimer import JPTimer

WIDTH, HEIGHT = 640, 480

CORNA = int(argv[1])
CORNB = int(argv[2])
SIDE = float(argv[3])

window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#000000")
canvas.pack()
img = PhotoImage(width=WIDTH, height=HEIGHT)
canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")
with JPTimer() as t:
    for i in range(WIDTH):
        i_factor = i/100.0
        for j in range(HEIGHT):
            x = CORNA + (SIDE * i_factor)
            y = CORNB + (SIDE * (j/100.0))
            z = x*x + y*y
            c = int(z)
            if c % 2 == 0:
                img.put("#ffffff", (i,j))
print ('Time required for this version was {:06,.2f} '
       'seconds'.format(t.interval))
mainloop()
