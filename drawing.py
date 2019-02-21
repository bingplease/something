from pygame import *
from math import *
init()
font.init()
w = display.set_mode([1500, 800])
w.fill((255, 255, 255))
objects = []
color = (0, 0, 0)
c1 = 0
c2 = 0
down = False
shape = 0
s1 = 0
s2 = 0
drawing = False
outline = False
o1 = False
o2 = False
d = True
while d:
    for e in event.get():
        if e.type == QUIT:
            d = False
        elif e.type == MOUSEBUTTONDOWN:
            down = True
            x1, y1 = mouse.get_pos()
            #shape select
            if x1 > 905 and y1 < 150:
                if 1005 < x1 < 1095 and 5 < y1 < 145:
                    s1 = 1 #line
                elif 1105 < x1 < 1195 and 5 < y1 < 145:
                    s1 = 2 #rect
                elif 1205 < x1 < 1295 and 5 < y1 < 145:
                    s1 = 3 #square
                elif 1305 < x1 < 1395 and 5 < y1 < 145:
                    s1 = 4 #elipse
                elif 1405 < x1 < 1495 and 5 < y1 < 145:
                    s1 = 5 #circle
                elif 905 < x1 < 995 and 5 < y1 < 145:
                    o1 = True #outline
            #color select
            elif x1 < 295 and y1 < 150:
                if 5 < x1 < 70 and 5 < y1 < 70:
                    c1 = 1
                elif 80 < x1 < 145 and 5 < y1 < 70:
                    c1 = 2
                elif 155 < x1 < 220 and 5 < y1 < 70:
                    c1 = 3
                elif 230 < x1 < 295 and 5 < y1 < 70:
                    c1 = 4
                elif 5 < x1 < 70 and 80 < y1 < 145:
                    c1 = 5
                elif 80 < x1 < 145 and 80 < y1 < 145:
                    c1 = 6
                elif 155 < x1 < 220 and 80 < y1 < 145:
                    c1 = 7
                elif 230 < x1 < 295 and 80 < y1 < 145:
                    c1 = 8
            #see if its not in the ribbon
            elif y1 > 150:
                drawing = True
        elif e.type == MOUSEBUTTONUP:
            down = False
            x2, y2 = mouse.get_pos()
            #Check if mouse up and down in same box
            if x2 > 905 and y1 < 150:
                if 1005 < x2 < 1095 and 5 < y2 < 145:
                    s2 = 1 #line
                elif 1105 < x2 < 1195 and 5 < y2 < 145:
                    s2 = 2 #rect
                elif 1205 < x2 < 1295 and 5 < y2 < 145:
                    s2 = 3 #square
                elif 1305 < x2 < 1395 and 5 < y2 < 145:
                    s2 = 4 #ellipse
                elif 1405 < x2 < 1495 and 5 < y2 < 145:
                    s2 = 5 #circle
                elif 905 < x2 < 995 and 5 < y2 < 145:
                    o2 = True
                if s1 == s2:
                    if s1 == 1:
                        shape = "line"
                    elif s1 == 2:
                        shape = "rect"
                    elif s1 == 3:
                        shape = "square"
                    elif s1 == 4:
                        shape = "ellipse"
                    elif s1 == 5:
                        shape = "circle"
                    print(shape)
                if o1 == o2 == True:
                    outline = not outline
            if o1 or o2:
                o1 = False
                o2 = False
            if s1 or s2:
                s1 = False
                s2 = False
                    
                

                
            
            elif x2 < 295 and y2 < 150:
                if 5 < x2 < 70 and 5 < y2 < 70:
                    c2 = 1
                elif 80 < x2 < 145 and 5 < y2 < 70:
                    c2 = 2
                elif 155 < x2 < 220 and 5 < y2 < 70:
                    c2 = 3
                elif 230 < x2 < 295 and 5 < y2 < 70:
                    c2 = 4
                elif 5 < x2 < 70 and 80 < y2 < 145:
                    c2 = 5
                elif 80 < x2 < 145 and 80 < y2 < 145:
                    c2 = 6
                elif 155 < x2 < 220 and 80 < y2 < 145:
                    c2 = 7
                elif 230 < x2 < 295 and 80 < y2 < 145:
                    c2 = 8
                if c1 == c2:
                    if c1 == 1:
                        color = (0, 0, 0)
                    elif c1 == 2:
                        color = (150, 75, 0)
                    elif c1 == 3:
                        color = (150, 150, 150)
                    elif c1 == 4:
                        color = (255, 255, 255)
                    elif c1 == 5:
                        color = (255, 0, 0)
                    elif c1 == 6:
                        color = (255, 255, 0)
                    elif c1 == 7:
                        color = (0, 255, 0)
                    elif c1 == 8:
                        color = (0, 0, 255)
                    
                    print(color)
                    break
            if c1 or c2:
                c1 = False
                c2 = False
            if drawing:
                drawing = False
            #if y2 < 150:
            #    if shape == "line":
            #        objects.append((w, color, (x1, y1), (x2, y2), 5))
            #        objects.append("line")
            #    elif shape == "rect":
            #        objects.append((w, color, Rect(x1, y1, x2 - x1, y2 - y1)))
            #        objects.append("rect")
    w.fill((255, 255, 255))
#Draw
    cx, cy = mouse.get_pos()
    #Draw previous objects
    #for i in range(0, int(len(objects)/2)):
    #    if objects[i + 1] == "line":
    #        draw.line(objects[i])
    #    elif objects[i + 1] == "rect":
    #        draw.rect(objects[i])
    if drawing:
        if outline:
            if shape == "line":
                draw.line(w, color, (x1, y1), (cx, cy), 1)
            elif shape == "rect":
                draw.rect(w, color, Rect(x1, y1, cx - x1, cy - y1), 1)
            elif shape == "square":
                #FIX THIS
                if cx < cy:
                    draw.rect(w, color, Rect(x1, y1, cx - x1, cx - x1), 1)
                else:
                    draw.rect(w, color, Rect(x1, y1, cy - y1, cy - y1), 1)
            elif shape == "ellipse":
                #FIX THIS
                print("x1", x1)
                print("y1", y1)
                print("cx", cx)
                print("cy", cy)
                print("cx - x1", abs(cx - x1))
                print("x1 - cx", abs(x1 - cx))
                print("cy - y1", abs(cy - y1))
                print("y1 - cy", abs(y1 - cy))
                if cx > x1 and cy > y1:
                    draw.ellipse(w, color, Rect(x1, y1, abs(cx - x1) + 1, abs(cy - y1) + 1), 1)
                elif cx > x1 and cy < y1:
                    draw.ellipse(w, color, Rect(x1, cy, abs(cx - x1) + 1, abs(y1 - cy) + 1), 1)
                elif cx < x1 and cy > y1:
                    draw.ellipse(w, color, Rect(cx, y1, abs(x1 - cx) + 1, abs(cy - y1) + 1), 1)
                elif cx < x1 and cy < y1:
                    draw.ellipse(w, color, Rect(cx, cy, abs(x1 - cx) + 1, abs(y1 - cy) + 1), 1)
            elif shape == "circle":
                #FIC THIs

                if cx > x1 and cy > y1:
                    draw.ellipse(w, color, Rect(x1, y1, abs(cx - x1) + 1, abs(cy - y1) + 1), 1)
                elif cx > x1 and cy < y1:
                    draw.ellipse(w, color, Rect(x1, cy, abs(cx - x1) + 1, abs(y1 - cy) + 1), 1)
                elif cx < x1 and cy > y1:
                    draw.ellipse(w, color, Rect(cx, y1, abs(x1 - cx) + 1, abs(cy - y1) + 1), 1)
                elif cx < x1 and cy < y1:
                    draw.ellipse(w, color, Rect(cx, cy, abs(x1 - cx) + 1, abs(y1 - cy) + 1), 1)

        else:
            if shape == "line":
                draw.line(w, color, (x1, y1), (cx, cy), 1)
            elif shape == "rect":
                draw.rect(w, color, Rect(x1, y1, cx - x1, cy - y1))
            elif shape == "square":
                if cx < cy:
                    draw.rect(w, color, Rect(x1, y1, cx - x1, cx - x1))
                else:
                    draw.rect(w, color, Rect(x1, y1, cy - y1, cy - y1))
            elif shape == "ellipse":
                draw.ellipse(w, color, Rect(x1, y1, cx - x1, cy - y1))
            elif shape == "circle":
                if cx < cy:
                    draw.ellipse(w, color, Rect(x1, y1, cx - x1, cx - x1))
                else:
                    draw.ellipse(w, color, Rect(x1, y1, cy - y1, cy - y1))
                

    
    #Ribbon rectangle
    draw.rect(w, (100, 100, 100), Rect(0, 0, 1500, 150))
    #Color selection
    draw.rect(w, (0, 0, 0), Rect(5, 5, 65, 65))
    draw.rect(w, (150, 75, 0), Rect(80, 5, 65, 65))
    draw.rect(w, (150, 150, 150), Rect(155, 5, 65, 65))
    draw.rect(w, (255, 255, 255), Rect(230, 5, 65, 65))

    draw.rect(w, (255, 0, 0), Rect(5, 80, 65, 65))
    draw.rect(w, (255, 255, 0), Rect(80, 80, 65, 65))
    draw.rect(w, (0, 255, 0), Rect(155, 80, 65, 65))
    draw.rect(w, (0, 0, 255), Rect(230, 80, 65, 65))

    draw.rect(w, color, Rect(300, 5, 140, 140))

    #Shape selection
    draw.rect(w, (150, 150, 150), Rect(905, 5, 90, 140))
    text = font.SysFont(None, 30)
    mytext = text.render("Outline", 1, (0, 0, 0))
    if outline:
        mytext2 = text.render("On", 1, (0, 0, 0))
    else:
        mytext2 = text.render("Off", 1, (0, 0, 0))
    w.blit(mytext, (910, 10))
    w.blit(mytext2, (910, 60))

    
    draw.rect(w, (200, 200, 200), Rect(1405, 5, 90, 140))
    draw.rect(w, (200, 200, 200), Rect(1305, 5, 90, 140))
    draw.rect(w, (200, 200, 200), Rect(1205, 5, 90, 140))
    draw.rect(w, (200, 200, 200), Rect(1105, 5, 90, 140))
    draw.rect(w, (200, 200, 200), Rect(1005, 5, 90, 140))
    if not outline:
        draw.line(w, color, (1010, 10), (1090, 135), 5)
        draw.rect(w, color, Rect(1110, 10, 80, 130))
        draw.rect(w, color, Rect(1215, 30, 70, 70))
        draw.ellipse(w, color, Rect(1310, 10, 80, 130))
        draw.circle(w, color, (1450, 75), 40)
    else:
        draw.line(w, color, (1010, 10), (1090, 135), 5)
        draw.rect(w, color, Rect(1110, 10, 80, 130), 5)
        draw.rect(w, color, Rect(1215, 30, 70, 70), 5)
        draw.ellipse(w, color, Rect(1310, 10, 80, 130), 5)
        draw.circle(w, color, (1450, 75), 40, 5)

        

    
    display.flip()
    
