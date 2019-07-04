from pygame import *
from math import *
init()
height = 1000
w = display.set_mode([height, height])
halfheight = height / 2

w.fill((255, 255, 255))
def outlinecircle(u):
    for x in range(halfheight-u, 2*u):
        for y in range(halfheight-u, 2*u):
            if u*u-u < floor((x-halfheight)*(x-halfheight) + (y-halfheight)*(y-halfheight)) < u*u+u:
                draw.line(w, (0, 0, 0), (x, y), (x, y), 1)
                display.flip()
                print(x, y)
    display.flip()
def solidcircle():
    for x in range(0, height):
        for y in range(0, height):
            if floor((x-halfheight)*(x-halfheight) + (y-halfheight)*(y-halfheight)) <= halfheight:
                draw.line(w, (0, 0, 0), (x, y), (x, y), 1)
                display.flip()
                print(x, y)
    display.flip()
    time.wait(3000)
def nestedcircle():
    for i in range(0, halfheight):
        outlinecircle(i)
        display.flip()
    time.wait(3000)
def sinwave():
    for i in range(1, height):
        draw.line(w, (255, 0, 0), (i, -sin(radians(i)) * factor + height/2), (i, -sin(radians(i)) * factor + height/2), 3)
        display.flip()
        print(i)
def coswave():
    for i in range(1, height):
        draw.line(w, (0, 255, 0), (i, -cos(radians(i)) * factor + height/2), (i, -cos(radians(i)) * factor + height/2), 3)
        display.flip()
        print(i)
def tanwave():
    for x in range(1, int(ceil(height/90))):
        for i in range(1, 90):
            draw.line(w, (0, 0, 255), (i + 90*x, -tan(radians(i)) * factor + height/2), (i + 90*x, -tan(radians(i)) * factor + height/2), 3)
            display.flip()
            print(i)
        for i in range(1, 90):
            draw.line(w, (0, 0, 255), (i + 90*x + 90, -tan(radians(-90+i)) * factor + height/2), (i + 90*x + 90, -tan(radians(-90+i)) * factor + height/2), 3)
            display.flip()
            print(i)
def tansinwave():
    for x in range(1, int(ceil(height/90))):
        for i in range(1, 90):
            draw.line(w, (0, 0, 0), (i + 90*x, -tan(sin(radians(i))) * factor + height/2), (i + 90*x, -tan(sin(radians(i))) * factor + height/2), 3)
            display.flip()
            print(i)
        for i in range(1, 90):
            draw.line(w, (0, 0, 0), (i + 90*x + 90, tan(sin(radians(90-i))) * factor + height/2), (i + 90*x+90, tan(sin(radians(90-i))) * factor + height/2), 3)
            display.flip()
            print(i)
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
def circlewave(x, y, length, sides):
    angle = float(360.0 / (sides * 1.0))
    points = []
    sign = 1
    c = 0
    for i in range(0, sides):
        x = cos(radians(angle * i)) * length + x
        y = sin(radians(angle * i)) * length + y
        points.append((int(x), int(y)))
        for i in range(0, len(points)):
            draw.line(w, (0, 0, 0), points[i], points[i], 1)

        display.flip()
        if c % 90 == 0:
            sign = -sign
            c = 0
        c += 1
        draw.line(w, (0, 0, 0), (i + 90*x + 90, sign * tan(sin(radians(90-i))) * factor + height/2), sign * (i + 90*x+90, tan(sin(radians(90-i))) * factor + height/2), 3)
        display.flip()

circlewave(500, 200, 5, 100)