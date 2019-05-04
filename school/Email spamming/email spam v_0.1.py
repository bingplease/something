import sys, os
sys.path.append("C:/users/" + os.getlogin() + "modules")
from pyautogui import *
from keyboard import press_and_release as press, write
from tkinter import *
import time, random
import pygame
pygame.init()
c = pygame.time.Clock()
def email():
    moveTo(100, 120)
    mouseDown()
    mouseUp()
    time.sleep(1)
    moveTo(1500, 225)
    mouseDown()
    mouseUp()
    write("s-domingosd@bsd405.org")
    moveTo(1500, 275)
    mouseDown()
    mouseUp()
    write("Important Email - Do Not Ignore!")
    time.sleep(0.5)
    moveTo(1500, 400)
    mouseDown()
    mouseUp()
    s = ""
    for i in range(1, 10):
        s += chr(random.randint(97, 122))
    write(s)
    moveTo(1850, 75)
    mouseDown()
    mouseUp()
    time.sleep(1)
for i in range(1, 1000):
    email()
