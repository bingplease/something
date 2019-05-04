#Up to 5 email addresses.

import sys, os
sys.path.append("C:/users/" + os.getlogin() + "modules")
from pyautogui import *
from keyboard import press_and_release as press, write
from tkinter import *
import time, random
day = time.strfttime("%d")
month = time.strfttime("%m")
year = time.strfttime("%Y")
if month > 4 or year > 2019:
    raise SyntaxError("Free trial has expired.")
tk = Tk()
Label(tk, text="Welcome to the email spam interface!", fg="red", font=("Comic Sans", 16)).grid(row=0)
Label(tk, text="Enter the email address of this person (s)").grid(row=1, column=0)
Label(tk, text="Enter the subject line of each email").grid(row=2, column=0)
Label(tk, text="Enter the text content of each email").grid(row=3, column=0)
Label(tk, text="Enter how many emails you want to send").grid(row=4, column=0)
address = Entry(tk)
address.grid(row=1, column=1)
address2 = Entry(tk)
address2.grid(row=1, column=2)
address3 = Entry(tk)
address3.grid(row=1, column=3)
address4 = Entry(tk)
address4.grid(row=1, column=4)
address5 = Entry(tk)
address5.grid(row=1, column=5)
subject=Entry(tk)
subject.grid(row=2, column=1)
text=Entry(tk)
text.grid(row=3, column=1)
number = Entry(tk)
number.grid(row=4, column=1)

def callback(wait_time, ad):
    time.sleep(wait_time)
    press("ctrl+n")
    time.sleep(0.2)
    if ad == 1:
        write(address.get())
    elif ad == 2:
        write(address2.get())
    elif ad == 3:
        write(address3.get())
    elif ad == 4:
        write(address4.get())
    elif ad == 5:
        write(address5.get())
    press("alt+s")
    press("tab")
    press("enter")
def repeat_outlook_callback():
    time.sleep(2)
    for i in range(0, int(number.get())):
        if address.get() != "":
            callback(0.5, 1)
        if address2.get() != "":
            callback(0.5, 2)
        if address3.get() != "":
            callback(0.5, 3)
        if address4.get() != "":
            callback(0.5, 4)
        if address5.get() != "":
            callback(0.5, 5)
            
#Label(tk, text="Red buttons - Mail").grid(row=5, column=0)
#Button(tk, text="Send One Email", command=outlook_callback(2), fg="white", bg="green").grid(row=5, column=1)
Button(tk, text="Send Emails", command=repeat_outlook_callback, fg="white", bg="green").grid(row=6, column=1)
Label(tk, text="You have to have the mail app open and click on it right after").grid(row=7)


mainloop()
