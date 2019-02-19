from pygame import *
from math import *
init()
width, height = 1000, 1000
w = display.set_mode([width, height])
factor = 100
w.fill((255, 255, 255))
def sinwave():
    for i in range(1, width):
        draw.line(w, (255, 0, 0), (i, -sin(radians(i)) * factor + height/2), (i, -sin(radians(i)) * factor + height/2), 3)
        display.flip()
        print(i)
def coswave():
    for i in range(1, width):
        draw.line(w, (0, 255, 0), (i, -cos(radians(i)) * factor + height/2), (i, -cos(radians(i)) * factor + height/2), 3)
        display.flip()
        print(i)
def tanwave():
    for x in range(1, int(ceil(width/90))):
        for i in range(1, 90):
            draw.line(w, (0, 0, 255), (i + 90*x, -tan(radians(i)) * factor + height/2), (i + 90*x, -tan(radians(i)) * factor + height/2), 3)
            display.flip()
            print(i)
        for i in range(1, 90):
            draw.line(w, (0, 0, 255), (i + 90*x + 90, -tan(radians(-90+i)) * factor + height/2), (i + 90*x + 90, -tan(radians(-90+i)) * factor + height/2), 3)
            display.flip()
            print(i)
def tansinwave():
    for x in range(1, int(ceil(width/90))):
        for i in range(1, 90):
            draw.line(w, (0, 0, 0), (i + 90*x, -tan(sin(radians(i))) * factor + height/2), (i + 90*x, -tan(sin(radians(i))) * factor + height/2), 3)
            display.flip()
            print(i)
        for i in range(1, 90):
            draw.line(w, (0, 0, 0), (i + 90*x + 90, tan(sin(radians(90-i))) * factor + height/2), (i + 90*x+90, tan(sin(radians(90-i))) * factor + height/2), 3)
            display.flip()
            print(i)

draw.line(w, (0, 0, 0), (0, height/2), (width, height/2), 3)
#sinwave()
#coswave()
#tanwave()
tansinwave()
time.wait(30000)
