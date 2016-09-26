from tkinter import Tk, Canvas, PhotoImage, mainloop
from math import sin
from time import sleep
from sys import argv

def get_int_input():
    while True:
        try:
            return int(input('Please enter a whole number:  '))
        except ValueError:
            print('Invalid input.  Please try again.')

def get_float_input():
    while True:
        try:
            return float(input('Please enter a floating point number:  '))
        except ValueError:
            print('Invalid input.  Please try again.')

def generate_width(column, row, user):
    while column > 0:
        for pixel in generate_height(column, row, user):
            yield column, pixel
        column -= 1

def generate_height(column, row, user):
    while row > 0:
        x = user[0] + (user[2] * (column/100.0))
        y = user[1] + (user[2] * (row/100.0))
        z = x*x + y*y
        if int(z) % 2 == 0:
            yield row
        row -= 1

print('How wide would you like the output?')
WIDTH = get_int_input()
print('How tall would you like the output?')
HEIGHT = get_int_input()
print('The following two numbers should blah blah blah geometry.')
CORNA = get_int_input()
CORNB = get_int_input()
print("[I hope this isn't getting tedious...]")
SIDE = get_float_input()

user = [CORNA, CORNB, SIDE]

window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="#000000")
canvas.pack()
img = PhotoImage(width=WIDTH, height=HEIGHT)
canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")

for column, row in generate_width(WIDTH, HEIGHT, user):
    img.put("#ffffff", (column,row))

mainloop()
