import sys, time, os
sys.path.append("C:/users/" + os.getlogin() + "modules")
from pyautogui import *
from keyboard import *
from tkinter import *
tk = Tk()
def spam():
    for i in range(0, int(times.get())):
        time.sleep(int(delay.get()))
        click()
        write(text.get())
        press_and_release("enter")
Label(tk, text="Enter the text").grid(row=0)
Label(tk, text="Enter the delay in seconds").grid(row=0, column=1)
Label(tk, text="Enter how many times").grid(row=0, column=2)
text = Entry(tk)
delay = Entry(tk)
times = Entry(tk)
text.grid(row=1)
delay.grid(row=1, column=1)
times.grid(row=1, column=2)
Button(tk, text="Start Spamming", command=spam).grid(row=2)
mainloop()
