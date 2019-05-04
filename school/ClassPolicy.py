#ClassPolicy blocker: V 1.0
#Automatically checks for the user
#You can put in a file of you doing work in your pictures folder.
import os, datetime, filecmp, shutil
from tkinter import *
from keyboard import *
def classpolicy():
    x = False
    v = False
    using = False
    c = True
    last_used = 0

##        #Remove the file
##        try:
##            os.remove("C:/ClassPolicy/" + os.getlogin() + ".jpeg")
##        except:
##            pass
    #Place in the file of you doing work
    shutil.copy("c:/users/" + os.getlogin() + "/pictures/s-feio.jpeg", "c:/classpolicy")
    #Press ` to end the program
    for i in range(1, 20000):
        if is_pressed('`'):
            c = False
            break
    try:
        v = filecmp.cmp("c:/users/" + os.getlogin() + "/pictures/" + os.getlogin() + ".jpeg", "C:/ClassPolicy/" + os.getlogin() + ".jpeg")
    except:
        v = True
    #If the teacher is using classpolicy, there will be a different file. Otherwise, your file will still be there.
    if not v:
        #If not the same
        last_used = datetime.datetime.now().time()
        using = True
    else:
        #If the same
        using = False
    #Tell user if is using or not
    print("Last Used ClassPolicy    " + str(last_used))
    print("Current Time Is    " +str(datetime.datetime.now().time()))
def delete():
    try:
        os.remove("c:/classpolicy/" + os.getlogin() + ".jpeg")
    except:
        pass

while True:
    delete()
