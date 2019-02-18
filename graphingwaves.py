from pygame import *
from math import *
init()
w = display.set_mode([1000, 1000])
w.fill((255, 255, 255))
def sinwave():
    for i in range(1, 1000):
        draw.line(w, (255, 0, 0), (i, -sin(radians(i)) * 100 + 500), (i, -sin(radians(i)) * 100 + 500), 3)
        display.flip()
        print(i)
def coswave():
    for i in range(1, 1000):
        draw.line(w, (0, 255, 0), (i, -cos(radians(i)) * 100 + 500), (i, -cos(radians(i)) * 100 + 500), 3)
        display.flip()
        print(i)
def tanwave():
    for i in range(1, 1000):
        draw.line(w, (0, 0, 255), (i, -tan(radians(i % 90)) * 100 + 500), (i, -tan(radians(i % 90)) * 100 + 500), 3)
        display.flip()
        print(i)
draw.line(w, (0, 0, 0), (0, 500), (1000, 500), 3)
sinwave()
coswave()
tanwave()
time.wait(100000)
