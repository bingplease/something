from tkinter import *
import os, time, shutil
tk = Tk()
def hide():
    os.system("attrib -s +h \"" + folder.get() + "\"")
def super_hide():
    os.system("attrib +s +h \"" + folder.get() + "\"")
def show():
    os.system("attrib -s -h \"" + folder.get() + "\"")
def delete():
    global x
    try:
        x.destroy()
    except:
        pass
    try:
        shutil.rmtree(folder.get())
    except:
        try:
            os.unlink(folder.get())
        except:
            print("File or folder does not exist")
            
            x = Label(tk, text="File or folder does not exist")
            
            x.grid(row=5)
def repeat_super_hide():
    for i in range(1, int(times.get())):
        super_hide()
        time.sleep(1)
        show()
        time.sleep(1)
def rename():
    os.system("ren " + folder.get() + " " + rename.get())
    print("ren " + folder.get() + " " + rename.get())
    print(folder.get())
    print(rename.get())
def destroy():
    tk.destroy()
Label(tk, text="Normal functions").grid(row=0, column=0)
Label(tk, text="Troll functions").grid(row=0, column=1)
Label(tk, text="Super troll functions").grid(row=0, column=2)
Button(tk, text="Show this file/folder", command=show, width=20, height=0, fg="green", font=("Comic Sans MS", 12)).grid(row=1, column=0)
Button(tk, text="Hide this file/folder", command=hide, width=20, height=0, font=("Comic Sans MS", 12)).grid(row=1, column=1)
Button(tk, text="Rename this file/folder", command=rename, width=20, height=0, font=("Comic Sans MS", 12)).grid(row=3, column=0)
Button(tk, text="Delete this file/folder", command=delete, width=20, height=0, fg="red", font=("Comic Sans MS", 12)).grid(row=2, column=0)
Button(tk, text="Super hide this file/folder", command=super_hide, width=20, height=0, font=("Comic Sans MS", 12)).grid(row=2, column=1)
Button(tk, text="Super hide/Unhide repeat", command=repeat_super_hide, width=20, height=0, font=("Comic Sans MS", 12)).grid(row=1, column=2)

Label(tk, text="").grid(row=3, column=0)
Label(tk, text="Enter file/folder name here", font=("Comic Sans MS", 12)).grid(row=4, column=0)
Label(tk, text="Enter how many times here\n(only for super troll)", font=("Comic Sans MS", 12)).grid(row=4, column=2)
Label(tk, text="Enter what the new name should be", font=("Comic Sans MS", 12)).grid(row=4, column=1)
folder = Entry(tk, width=30)
folder.grid(row=5, column=0)
rename = Entry(tk, width=30)
rename.grid(row=5, column=1)
times = Entry(tk, width=30)
times.grid(row=5, column=2)
##menubar = Menu(tk)
##def hello():
##    print("hello")
##w = ""
##def directory():
##    global w
##    w = "c:/users/" + os.getlogin()
##def documents():
##    global w
##    w = "c:/users/" + os.getlogin() + "/documents"
##def desktop():
##    global w
##    w = "c:/users/" + os.getlogin() + "/desktop"
##def downloads():
##    global w
##    w = "c:/users/" + os.getlogin() + "/dowmloads"
##def pictures():
##    global w
##    w = "c:/users/" + os.getlogin() + "/pictures"
##def printw():
##    print(w)
##filemenu = Menu(menubar, tearoff=0)
##filemenu.add_command(label=os.getlogin(), command=directory)
##filemenu.add_command(label="Desktop", command=desktop)
##filemenu.add_command(label="Documents", command=documents)
##filemenu.add_command(label="Downloads", command=downloads)
##filemenu.add_command(label="Pictures", command=pictures)
##filemenu.add_separator()
##filemenu.add_command(label="Exit", command=destroy)
##menubar.add_cascade(label="Doesn't work yet", menu=filemenu)
##Button(tk, text="A useless button that dosen't work yet", command=printw).grid(row=5)
### display the menu
##tk.config(menu=menubar)
mainloop()
