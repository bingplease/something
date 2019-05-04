import sys, time, webbrowser, random, os
sys.path.append("C:/users/" + os.getlogin() + "modules")
from pyautogui import *
from keyboard import press_and_release as press, write
from tkinter import *
tk = Tk()
##game_pin = input("Enter the game pin: ")
###name = input("Enter the username you want: ")
##times = int(input("Enter how many bots you want to send: "))
##for i in range(0, times):
##    webbrowser.open("http://www.kahoot.it")
##    time.sleep(3)
##    moveTo(1000, 600)
##    click()
##    write(game_pin)
##    press("enter")
##    time.sleep(2)
##    click()
##    write((chr(random.randint(97, 122)) + chr(random.randint(97, 122))) + (chr(random.randint(97, 122)) + chr(random.randint(97, 122))))
##    press('enter')
    
Label(tk, text="Game pin").grid(row=1)
Label(tk, text="Name").grid(row=1, column=1)
x = IntVar()
Checkbutton(tk, text="Random names", variable=x).grid(row=0, column=1)
