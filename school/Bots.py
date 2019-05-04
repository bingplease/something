import sys, datetime, time, random, webbrowser, os
sys.path.append('C:/users/' + os.getlogin() + '/modules')
from pyautogui import *
from keyboard import press_and_release as press, is_pressed, write
from tkinter import *
tk = Tk()

#Click is made from a mouse down and a mouse up
#If the teacher is using ClassPolicy, it will update the last_used variable. Otherwise, it will display the last used time.
#How ClassPolicy works:
#If the teacher is using ClassPolicy, then ClassPolicyAutoUpdate.exe will take a screenshot of your screen. It will be saved as C:/ClassPolicy/<YOUR USERNAME>.jpeg.
#OTherwise, if they are not using ClassPolicy, then no image will appear.
def classpolicy():
    using = False
    c = True
    last_used = 0
    while c:
        try:
            os.remove("C:\ClassPolicy\s-feio.jpeg")
        except:
            pass
        for i in range(1, 10000):
            if is_pressed('`'):
                c = False
                break
        try:
            open("C:\ClassPolicy\s-feio.jpeg")
            last_used = datetime.datetime.now().time()
            using = True
        except:
            using = False                
        finally:
            try:
                label1.destroy()
                label2.destroy()
            except:
                pass
            finally:
##                    label1 = Text(tk)
##                    label2 = Text(tk)
##                    label1.insert(INSERT, "Last Used ClassPolicy    " + str(last_used))
##                    label2.insert(INSERT, "Current Time Is    " + str(datetime.datetime.now().time()))
##                    label1.grid(row=3, column=0)
##                    label2.grid(row=4, column=0)
                print("Last Used ClassPolicy    " + str(last_used))
                print("Current Time Is    " + str(datetime.datetime.now().time()))
#Clicks repeadetly, depending on how fast your computer is.
def autoclick():
    while True:
        click()
        if is_pressed('`'):
            break
#Spams this text in the location of your mouse
def start_typing():
        while True:
            write(e2.get())
            if is_pressed('`'):
                break
def quit_autotyper():
    e2.destroy()
    type_it.destroy()
    q.destroy()
def autotype():
    e2 = Entry(tk)
    e2.grid(row=0, column=2)
    print("Entey")
    type_it = Button(tk, text="Spam this text", command = bots.start_typing)
    type_it.grid(row=1, column=2)
    print("Button")
    q = Button(tk, text="Quit autotyper", command = bots.quit_autotyper())
    q.grid(row=2, column=2)

#Does 30 bing searches on Chrome. 
def search():
    webbrowser.open("https://www.bing.com")
    #30 being searches
    press(chr(random.randint(97, 122)))
    press('enter')
    end = False
    for i in range(0, 30):
        for i in range(1, 10000):
            if is_pressed('`'):
                end = True
        moveTo(500, 160)
        click()
        press(chr(random.randint(97, 122)))
        press('enter')
        if end:
            break
    time.sleep(3)
    press('ctrl+w')
#Does 30 bing searches on Edge. (Edge's top bar is slight|y larger than Chrome's).
def searchedge():
    #30 being searches
    press("windows")
    write("edge")
    press("enter")
    press('a')
    press('enter')
    end = False
    for i in range(0, 30):
        for i in range(1, 30000):
            if is_pressed('`'):
                end = True
        moveTo(500, 180)
        click()
        press('a')
        press('enter')
        if end:
            break
    time.sleep(3)
    press('ctrl+w')
def membean():
    g = ['a', 'b', 'c']
    end = False
    while not end:
        #Presses a, b, c in a random order
        random.shuffle(g)
        press(g[0])
        time.sleep(1)
        press(g[1])
        time.sleep(1)
        press(g[2])
        time.sleep(1)
        #Presses n to advance from a incorrect answer
        press('n')
        for i in range(1, 10000):
            if is_pressed('`'):
                end = True
                break
    #End the session
    time.sleep(3)
    press('x')
    time.sleep(5)
    press('ctrl+w')
f = Frame(tk, height = 500, width = 300)
def functions():
    Label(tk, text="Auto Clicker\nMembean\nBing\nClassPolicy").grid(row=3)

##b1 = Button(f, text = "Membean log in", state = DISABLED)
##b2 = Button(f, text = "Auto clicker - Press ` to end", command = bots.autoclick)
##b3 = Button(f, text = "Membean bot - Press ` to end", command = bots.membean)
##b5 = Button(f, text = "Bing Searches - Press ` to end", command = bots.search)
##b4 = Button(f, text = "Bing Dashboard", state = DISABLED)
##b6 = Button(f, text = "ClassPolicy - Press ` to end\nYOU WILL NEED TO LOOK\nAT THE TERMINAL", command = bots.classpolicy)

def run():
    function = ""
    for i in range(0, len(e1.get())):
        function += e1.get()[i].capitalize()
    if function == "AUTO CLICKER":
        print("Running Auto Clicker")
        autoclick()
    elif function == "MEMBEAN":
        print("Running Membean")
        membean()
    elif function == "BING" or function == "BING SEARCHES":
        print("Running Bing Searches")
        search()
    elif function == "CLASSPOLICY":
        print("Running ClassPolicy")
        classpolicy()
    elif function == "AUTO TYPER":
        print("Running Autotype")
        autotype()
    elif function == "FUNCTIONS":
        functions()
    else:
        print("That function does not exist")
Label(tk, text="Enter function to run").grid(row=0)
e1 = Entry(tk)
e1.grid(row=0, column=1)
##Label(tk, text="Type \"functions\" to see a\nlist of available functions").grid(row=0, column=2)
Button(tk, text='List of functions', command=functions, fg="white", bg="red").grid(row=1, column=0, sticky=W, pady=4)
Button(tk, text='Run', command=run, fg="white", bg="green").grid(row=1, column=1, sticky=W, pady=4)
##quit_button.grid(row=1, column=0, sticky=W, pady=4)
##run_button.grid(row=1, column=1, sticky=W, pady=4)


##b1.grid(row = 1, column = 2, sticky = E)
##b2.grid(row = 1, column = 1, sticky = W)
##b3.grid(row = 2, column = 1, sticky = W)
##b4.grid(row = 2, column = 2, sticky = E)
##b5.grid(row = 3, column = 1, sticky = W)
##b6.grid(row = 4, column = 1, sticky = W)
mainloop()
