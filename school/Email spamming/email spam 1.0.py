#Official Release: You can stop the spam by holding down F4
#which is located in the top left corner of your keyboard.
#However, it still has to get through a cycle of emails (everyone in the boxes.)
import sys, os
sys.path.append("C:/users/" + os.getlogin() + "/modules")
from pyautogui import *
from keyboard import press_and_release as press, write, is_pressed
from tkinter import *
import time, random
tk = Tk()
Label(tk, text="Welcome to the email spam interface!", fg="red", font=("Comic Sans", 16)).grid(row=0)
Label(tk, text="Enter the email address of this person (s)").grid(row=1, column=0)
Label(tk, text="Enter the subject line of each email (OPTIONAL)").grid(row=2, column=0)
Label(tk, text="Enter the text content of each email (OPTIONAL)").grid(row=3, column=0)
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
text = Entry(tk)
text.grid(row=3, column=1)
number = Entry(tk)
number.grid(row=4, column=1)

def email(wait_time, ad):
    time.sleep(wait_time)
    press("ctrl+n")
    time.sleep(0.1)
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
def repeat_email():
    time.sleep(2)
    d = True
    for i in range(0, int(number.get())):
        if address.get() != "":
            email(0.5, 1)
        if address2.get() != "":
            email(0.5, 2)
        if address3.get() != "":
            email(0.5, 3)
        if address4.get() != "":
            email(0.5, 4)
        if address5.get() != "":
            email(0.5, 5)
        for i in range(1, 100):
            if is_pressed("F4"):
                d = False
        if not d:
            break
        
def quit():
    tk.destroy()
#Label(tk, text="Red buttons - Mail").grid(row=5, column=0)
#Button(tk, text="Send One Email", command=outlook_callback(2), fg="white", bg="green").grid(row=5, column=1)
Button(tk, text="Send Emails", command=repeat_email, fg="white", bg="green").grid(row=6, column=1)
Button(tk, text="Quit", command=quit, fg="white", bg="red").grid(row=6, column=0)
Label(tk, text="You have to have the mail app open and click on it right after").grid(row=7)
mainloop()

