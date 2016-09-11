"""
circle2.py - from John E. Connett's "CIRCLE^2".

Deeptinker refactorings:

1.  Added code to time how long each run takes.
    RESULT: N/A

2.  Reduce the number of times that i/100.0 is calculatated.
    RESULT: negligible difference

3.  Removed computation of x*x from body of loop.
    RESULT: negligible difference

4.  Precompute x squared values and y squared values and store them in
    separate arrays.  Thus the loop is just adding values rather than all
    the previous computation over and over.
    RESULT: negligable difference

5.  Added Jim Prior's code to set the bits as one call to tkinter rather
    than a  call per bit.
    Results: Cut the time from about 2 minutes to less than half a second.

Requirements: numpy, JPTimer (separate module)
"""
from tkinter import Tk, Canvas, PhotoImage, mainloop
from sys import argv

from numpy import empty as npempty

from JPTimer import JPTimer

# label some "magic" numbers with names that help to understand their meaning
WIDTH,  = 640
HEIGHT = 480
CORNA = int(argv[1])
CORNB = int(argv[2])
SIDE = float(argv[3])
WHITE = '#000000'
BLACK = '#ffffff'


def color(xx:float, yy:float) -> str:
    """
    Compute innermost computation that sets the bit to white or black.

    :param xx: the "x squared" value
    :param yy:  the "y squared" value
    :return:
    """
    z = xx + yy
    c = int(z)
    if c % 2 == 0:
        return BLACK
    else:
        return WHITE


def main(argv):
    """
    Main part of program.

    :param argv:
    :return:
    """
    window = Tk()
    canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg=WHITE)
    canvas.pack()
    img = PhotoImage(width=WIDTH, height=HEIGHT)
    canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")
    with JPTimer() as t:
        # compute x*x values and store them in a numpy array
        x_squareds = npempty((WIDTH, 1), dtype=float)
        for i in range(WIDTH):
            x = CORNA + (SIDE * i / 100.0)
            x_squareds[i, 0] = x * x

        # compute y*y values and store them in a numpy array
        y_squareds = npempty((HEIGHT, 1), dtype=float)
        for j in range(HEIGHT):
            y = CORNA + (SIDE * j / 100.0)
            y_squareds[j, 0] = y * y

        # compute the bits and store them in a character array
        lines = []
        for j in range(HEIGHT):
            horizontal_line = '{'
            for i in range(WIDTH):
                colorbit = color(x_squareds[i, 0], y_squareds[j, 0])
                horizontal_line += (' ' + colorbit)
            horizontal_line += '}'
            lines.append(horizontal_line)
        img.put(' '.join(lines))



    print('Time required for this version was {:06,.2f} '
          'seconds'.format(t.interval))
    mainloop()

if __name__ == '__main__':
    main(argv)
