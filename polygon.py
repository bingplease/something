from math import *
from pygame import *
init()
w = display.set_mode([600, 600])
def polygon(length, sides):
    #Exterior angles float
    angle = float(360.0 / (sides * 1.0)) 
    points = []
    for i in range(0, sides):
        x = cos(radians(angle * i)) * length + 300
        y = sin(radians(angle * i)) * length + 300
        points.append((int(y), int(x)))
    w.fill((255, 255, 255))
    draw.polygon(w, (0, 0, 0), points)
    display.flip()
polygon(300, 36001)
time.wait(5000)