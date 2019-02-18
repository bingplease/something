from pygame import *
from math import *
init()

w = display.set_mode([500, 500])
w.fill((255, 255, 255))
def outlinecircle(u):
    for x in range(250-u, 2*u):
        for y in range(250-u, 2*u):
            if u*u-u < floor((x-250)*(x-250) + (y-250)*(y-250)) < u*u+u:
                draw.line(w, (0, 0, 0), (x, y), (x, y), 1)
                display.flip()
                print(x, y)
    display.flip()
def solidcircle():
    for x in range(0, 500):
        for y in range(0, 500):
            if floor((x-250)*(x-250) + (y-250)*(y-250)) <= 62500:
                draw.line(w, (0, 0, 0), (x, y), (x, y), 1)
                display.flip()
                print(x, y)
    display.flip()
    time.wait(3000)
def nestedcircle():
    for i in range(0, 50):
        outlinecircle(i)
        display.flip()
    time.wait(3000)

nestedcircle()
