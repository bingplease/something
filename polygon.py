from math import *
from pygame import *
from random import *
init()
w = display.set_mode([1920, 1080])
def polygon(x, y, length, sides):
    #Exterior angles float
    angle = float(360.0 / (sides * 1.0)) 
    points = []
    for i in range(0, sides):
        x = cos(radians(angle * i)) * length + x
        y = sin(radians(angle * i)) * length + y
        points.append((int(x), int(y)))
    draw.polygon(w, (randint(0, 255), randint(0, 255), randint(0, 255)), points)
    display.flip()
polygons = []
w.fill((255, 255, 255))
for i in range(1, 20):
    length = int(input("Length of side "))
    sides = int(input("Number of sides "))
    d = True
    while d:
        for e in event.get():
            if e.type == MOUSEBUTTONDOWN:
                down = True
            if e.type == MOUSEBUTTONUP and down:
                x, y = mouse.get_pos()
                d = False
    polygon(x, y, length, sides)

