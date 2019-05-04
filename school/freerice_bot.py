import sys, time, ctypes
sys.setrecursionlimit(100000)
sys.path.append("C:/users/" + os.getlogin() + "modules")
from pyautogui import *
from keyboard import press_and_release as press, is_pressed
from tkinter import *
from pyperclip import pyperclip
tk = Tk()
locations = [350, 425, 500, 575]
def get_text(y):
    time.sleep(1)
    moveTo(700, y)
    mouseDown()
    moveTo(1300, y, duration=0.1)
    mouseUp()
    time.sleep(0.1)
    press("ctrl+c")
def get_question():
    time.sleep(1)
    moveTo(900, 285)
    mouseDown()
    moveTo(1000, 285, duration=0.1)
    mouseUp()
    time.sleep(0.1)
    press("ctrl+c")
def switch():
    ctypes.windll.user32.keybd_event(0x12, 0, 0, 0) #Alt
    time.sleep(0.1)
    ctypes.windll.user32.keybd_event(0x09, 0, 0, 0) #Tab
    time.sleep(0.5)
    ctypes.windll.user32.keybd_event(0x12, 0, 2, 0) #Alt
    time.sleep(0.1)
    ctypes.windll.user32.keybd_event(0x09, 0, 2, 0) #Tab
def run():
    #Puts the correct answer in q
    get_question()
    q = str(pyperclip.paste())
    q = eval(str(q.replace("x", "*")))
    print(q)
    #Checks if each answer is correct
    for i in range(0,4):
        get_text(locations[i])
        g = int(pyperclip.paste())
        print(i)
        print(q, g)
        print("\n")
        if q == g:
            click(1000, locations[i])
def repeat():
    while True:
        run()
        for i in range(1, 5000):
            if is_pressed("F4"):
                return 1

Button(tk, text="Start", command=repeat).grid(row=0)
mainloop()
