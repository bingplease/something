#Made the program more user friendly.
#You can now enter the email address, the subject line, the text, and how many emails to send.
#Only works on Windows Mail. Will add support for Outlook as well.
import sys, os
sys.path.append("C:/users/" + os.getlogin() + "modules")
from pyautogui import *
from keyboard import press_and_release as press, write
from tkinter import *
import time, random

tk = Tk()
Label(tk, text="Enter the email address of this person").grid(row=0, column=0)
Label(tk, text="Enter the subject line of each email").grid(row=1, column=0)
Label(tk, text="Enter the text content of each email").grid(row=2, column=0)
Label(tk, text="Enter how many emails you want to send").grid(row=3, column=0)
address = Entry(tk)
address.grid(row=0, column=1)
subject=Entry(tk)
subject.grid(row=1, column=1)
text=Entry(tk)
text.grid(row=2, column=1)
number = Entry(tk)
number.grid(row=3, column=1)




def callback():
    moveTo(100, 120)
    mouseDown()
    mouseUp()
    time.sleep(1)
    moveTo(1500, 225)
    mouseDown()
    mouseUp()
    write(address.get())
    moveTo(1500, 275)
    mouseDown()
    mouseUp()
    write(subject.get())
    time.sleep(0.3)
    moveTo(1500, 400)
    mouseDown()
    mouseUp()
    write(text.get())
    moveTo(1850, 75)
    mouseDown()
    mouseUp()
    time.sleep(1)
def repeat_callback():
    for i in range(0, int(number.get())):
        callback()
Button(tk, text="Send One Email", command=callback).grid(row=4)
Button(tk, text="Send Many Emails", command=repeat_callback).grid(row=5)

mainloop()
