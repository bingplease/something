#Mail will not be used because it is way too slow.
#Added support for 2 email addresses.
import sys, os
sys.path.append("C:/users/" = os.getlogin() ")
from pyautogui import *
from keyboard import press_and_release as press, write
from tkinter import *
import time, random

tk = Tk()
Label(tk, text="Enter the email address of this person (s)").grid(row=0, column=0)
Label(tk, text="Enter the subject line of each email").grid(row=1, column=0)
Label(tk, text="Enter the text content of each email").grid(row=2, column=0)
Label(tk, text="Enter how many emails you want to send").grid(row=3, column=0)
address = Entry(tk)
address.grid(row=0, column=1)
address2 = Entry(tk)
address2.grid(row=0, column=2)
subject=Entry(tk)
subject.grid(row=1, column=1)
text=Entry(tk)
text.grid(row=2, column=1)
number = Entry(tk)
number.grid(row=3, column=1)

##def callback(wait_time):
##    time.sleep(wait_time)
##    moveTo(100, 120)
##    click()
##    time.sleep(0.5)
##    write(address.get())
##    moveTo(1500, 275)
##    click()
##def repeat_callback():
##    time.sleep(2)
##    for i in range(0, int(number.get())):
##        callback(1)
def outlook_callback(wait_time):
    time.sleep(wait_time)
    press("ctrl+n")
    time.sleep(0.5)
    write(address.get())
    press("alt+s")
    press("tab")
    press("enter")
def outlook_callback2(wait_time):
    time.sleep(wait_time)
    press("ctrl+n")
    time.sleep(0.5)
    write(address2.get())
    press("alt+s")
    press("tab")
    press("enter")
def repeat_outlook_callback():
    time.sleep(2)
    for i in range(0, int(number.get())):
        outlook_callback(0.5)
        if address2.get() != "":
            outlook_callback2(0.5)
            
Label(tk, text="Red buttons - Mail").grid(row=4, column=0)
Label(tk, text="Green buttons - Outlook").grid(row=4, column=1)
##Button(tk, text="Send One Email", command=callback(2), fg="white", bg="red").grid(row=5)
##Button(tk, text="Send Many Emails", command=repeat_callback, fg="white", bg="red").grid(row=6)
Button(tk, text="Send One Email", command=outlook_callback(2), fg="white", bg="green").grid(row=5, column=1)
Button(tk, text="Send Many Emails", command=repeat_outlook_callback, fg="white", bg="green").grid(row=6, column=1)
Label(tk, text="You have to have the mail app open and click on it right after").grid(row=7)


mainloop()
