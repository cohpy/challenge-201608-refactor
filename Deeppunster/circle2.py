"""
circle2.py - from John E. Connett's "CIRCLE^2".

Deeptinker refactorings:

1.  Added code to time how long each run takes.
    RESULT: N/A

2.  Reduce the number of times that i/100.0 is calculatated.
    RESULT: negligible.

3.  Removed computation of x*x from body of loop.
    RESULT: negligible

4.  Precompute x squared values and y squared values and store them in
    separate arrays.  Thus the loop is just adding values rather than all
    the previous computation over and over.
"""
from tkinter import Tk, Canvas, PhotoImage, mainloop
from sys import argv

from numpy import empty as npempty

from JPTimer import JPTimer

WIDTH, HEIGHT = 640, 480

CORNA = int(argv[1])
CORNB = int(argv[2])
SIDE = float(argv[3])
WHITE = '#000000'
BLACK = '#ffffff'

window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg=WHITE)
canvas.pack()
img = PhotoImage(width=WIDTH, height=HEIGHT)
canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")
with JPTimer() as t:
    # compute x*x values and store them
    x_squareds = npempty((WIDTH, 1), dtype=float)
    for i in range(WIDTH):
        x = CORNA + (SIDE * i / 100.0)
        x_squareds[i, 0] = x * x

    # compute y*y values and store them
    y_squareds = npempty((WIDTH, 1), dtype=float)
    for j in range(HEIGHT):
        y = CORNA + (SIDE * j / 100.0)
        y_squareds[j, 0] = y * y
    for i in range(WIDTH):
        for j in range(HEIGHT):
            z = x_squareds[i, 0] + y_squareds[j, 0]
            c = int(z)
            if c % 2 == 0:
                img.put(BLACK, (i, j))
print('Time required for this version was {:06,.2f} '
      'seconds'.format(t.interval))
mainloop()
