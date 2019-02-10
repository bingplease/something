import os
import Tkinter
import tkMessageBox

top = Tkinter.Tk()

def helloCallBack():
   tkMessageBox.showinfo( "Haha your computer will shut down anyways")
   os.system('shutdown /s /t 1')

B = Tkinter.Button(top, text ="Don't shut down", command = helloCallBack)

B.pack()
top.mainloop()