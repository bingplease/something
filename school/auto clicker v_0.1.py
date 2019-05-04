#v 0.1
#5/1/2019
#Autoclicker
#Added UI, click number, CPS, button, 1 sec delay between button press and start clicks
import sys, time
sys.path.append("c:/users/s-feio/modules")
from pyautogui import *
from keyboard import *
from tkinter import *
def clicking():
    if check.get() == 0: f = 1
    else: f = int(check.get())
    if number.get() == "": g = 1
    else: g = int(number.get())
    if between.get() == "": h = 0
    else: h = 1/float(between.get())
    time.sleep(1)
    for i in range(0, g + 1):
        click(button=f)
        time.sleep(h)
        if is_pressed("F4"):
            break
tk = Tk()
Label(tk, width=30).grid(row=0, column=1)
tk.title("Auto clicker - by Owen Fei")
check = IntVar()
Label(tk, text="Number of clicks").grid(row=0)
number = Entry(tk)
number.grid(row=1)
Label(tk, text="CPS (please keep it under 10)").grid(row=2)
between = Entry(tk)
between.grid(row=3)
pos = Text(tk, height=0, width=13, font=("Calibri, 14"))
pos.grid(row=10)
Radiobutton(tk, text="Left", variable=check,  value=1).grid(row=4)
Radiobutton(tk, text="Middle", variable=check,  value=2).grid(row=5)
Radiobutton(tk, text="Right", variable=check,  value=3).grid(row=6)
Button(tk, text="Start Clicking\nFN+F4 to stop", command=clicking, font=("Calibri, 12")).grid(row=7)
#Label(tk, text="Queued mouse positions").grid(row=0, column=1)



while True:
    pos.delete(1.0, END)
    pos.insert(END, (str(position())[6:])[:-1])
    tk.update()
