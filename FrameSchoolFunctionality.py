'''
Apps for school.

-For Anyone
Calculators
Clocks/Stopwatches (NOT IMPLEMENTED)
Web shortcuts
File walker
Auto clicker (100+ CPS max)

-For BSD Computers
ClassPolicy blockers
EXE runner (NOT IMPLEMENTED)
'''

import sys
import math
import os
import datetime
import time
import filecmp
import shutil
import ctypes
import webbrowser
from tkinter import (Tk, Button, Checkbutton, Entry, Frame, Listbox, Label,
                     PhotoImage, Radiobutton, Text, Canvas, Menu,
                     BooleanVar, IntVar, StringVar, messagebox as msg, ttk,
                     filedialog, TclError, N, S, E, W, EW, SE, END, DISABLED)
for i in os.listdir(f'c:\\users\\{os.getlogin()}'):
    #As long as your modules are in any folder directly under the user,
    #it can be imported.
    sys.path.append(i)

try:
    import keyboard
    CAN_STOP = True
except:
    msg.showinfo(title='Error', message='FN+F4 to stop does not work.')
    CAN_STOP = False

#PREFERENCES is a file that stores the custon image path for CLassPolicy.
PREFERENCES = f'c:\\users\\{os.getlogin()}\\preferences.txt'
if not os.path.exists(PREFERENCES):
    open(PREFERENCES, 'w+').close()
    os.system('attrib +s +h ' + PREFERENCES)

#A group of function that simulate clicks.
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
MOUSEEVENTF_LEFTCLICK = MOUSEEVENTF_LEFTDOWN + MOUSEEVENTF_LEFTUP
MOUSEEVENTF_RIGHTDOWN = 0x0008
MOUSEEVENTF_RIGHTUP = 0x0010
MOUSEEVENTF_RIGHTCLICK = MOUSEEVENTF_RIGHTDOWN + MOUSEEVENTF_RIGHTUP
MOUSEEVENTF_MIDDLEDOWN = 0x0020
MOUSEEVENTF_MIDDLEUP = 0x0040
MOUSEEVENTF_MIDDLECLICK = MOUSEEVENTF_MIDDLEDOWN + MOUSEEVENTF_MIDDLEUP

def _size():
    '''
    Returns the size of the window.
    '''
    return (ctypes.windll.user32.GetSystemMetrics(0),
            ctypes.windll.user32.GetSystemMetrics(1))

class POINT(ctypes.Structure):
    '''
    HElper for clicks.
    '''
    _fields_ = [("x", ctypes.c_long),
                ("y", ctypes.c_long)]

def position():
    '''
    Gets the current position of the mouse.
    '''
    cursor = POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(cursor))
    return (cursor.x, cursor.y)

def _sendMouseEvent(ev, x, y, dwData=0):
    '''
    Uses ctypes to simulate mouse event.
    '''
    width, height = _size()
    convertedX = 65536 * x // width + 1
    convertedY = 65536 * y // height + 1
    ctypes.windll.user32.mouse_event(ev, ctypes.c_long(convertedX),
                                     ctypes.c_long(convertedY), dwData, 0)

def click(x=position()[0], y=position()[1], button='left'):
    '''
    Clicks.
    '''
    if button == 1:
        try:
            _sendMouseEvent(MOUSEEVENTF_LEFTCLICK, x, y)
        except (PermissionError, OSError): 
            pass
    elif button == 2:
        try:
            _sendMouseEvent(MOUSEEVENTF_MIDDLECLICK, x, y)
        except (PermissionError, OSError): 
            pass
    elif button == 3:
        try:
            _sendMouseEvent(MOUSEEVENTF_RIGHTCLICK, x, y)
        except (PermissionError, OSError): 
            pass
    else:
        assert False, "button argument not in ('left', 'middle', 'right')"


class CalcFrame(Frame):
    '''
    Standard calculator with a LineO display.
    '''
    def __init__(self, master, title):
        '''
        Creates the display.
        '''
        Frame.__init__(self, master)
        self.grid()

        self.buttons = []
        self.title = title

        self.text = Text(self, font = ('Helvetica', 15), height = 1,
                         width = 27, bg = '#AFEEEE')
        self.text.grid(row = 0, column = 0, columnspan = 4)
        def createbutton(number, name, commandname, gridx, gridy):
            '''
            Makes it easier to create buttons.
            '''
            if str(number) == '0':
                columnspan = 2
                sticky = EW
            else:
                columnspan = 1
                sticky = None
            def commandname():
                '''
                Inserts a character into the text box.
                '''
                if self.text.get(1.0, END).strip() == 'Error':
                    self.text.delete(1.0, END)
                self.text.insert(END, number)
            name = Button(self, command = commandname, text = number,
                          width = 8, height = 1, bg = 'light blue',
                          font = ('Calibri', 12))
            name.grid(row = gridx, column = gridy, columnspan = columnspan,
                      sticky=sticky)
            
        createbutton('0', 'button0', 'command0', 5, 0)
        createbutton('1', 'button1', 'command1', 2, 0)
        createbutton('2', 'button2', 'command2', 2, 1)

        createbutton('3', 'button3', 'command3', 2, 2)
        createbutton('4', 'button4', 'command4', 3, 0)
        createbutton('5', 'button5', 'command5', 3, 1)

        createbutton('6', 'button6', 'command6', 3, 2)
        createbutton('7', 'button7', 'command7', 4, 0)
        createbutton('8', 'button8', 'command8', 4, 1)

        createbutton('9', 'button9', 'command9', 4, 2)

        createbutton('+', 'additionbutton', 'additioncommand', 2, 3)
        createbutton('-', 'subtractionbutton', 'subtractioncommand', 3, 3)

        createbutton('*', 'multiplicationbutton', 'multiplicationcommand', 4, 3)
        createbutton('/', 'divisionbutton', 'divisioncommand', 5, 3)
        createbutton('(', 'abutton', 'acommand', 6, 0)
        createbutton(')', 'bbutton', 'bcommand', 6, 1)
        createbutton('.', 'meh', 'aaaargh', 5, 2)

        erasebutton = Button(self, font = ('Calibri', 12), command = self.
                             erase,
                             text = 'AC', width = 8, height = 1,
                             bg = 'light blue')
        erasebutton.grid(row = 1, column = 0, columnspan=2, sticky=EW)

        equalbutton = Button(self, command = self.equals, font = ('Calibri', 12),
                             text = '=', width = 8, height = 1,
                             bg = 'light blue')
        equalbutton.grid(row = 6, column = 2, columnspan = 2, sticky=EW)
        deletebutton = Button(self, text='<--', font=('Calibri', 12),
                              bg = 'light blue', state = DISABLED,
                              command = lambda: self.text.delete(END, END))
        deletebutton.grid(row=1, column=2, columnspan=2, sticky=EW)

    def erase(self):
        '''
        Clears the text box.
        '''
        self.text.delete(1.0, END)

    def equals(self):
        '''
        Evaluates the text box result and prints it in.
        '''
        global evaluate
        if self.text.get(1.0, END).strip() == '':
            return
        try:
            evaluate = eval(self.text.get('1.0', END))
            self.text.delete(1.0, END)
            self.text.insert(END, str(evaluate))
        except:
            self.text.delete(1.0, END)
            self.text.insert(END, 'Error')


class SciCalcFrame(Frame):
    '''
    Scientific calculator with a LineO display.
    '''
    def __init__(self, master, title):
        Frame.__init__(self, master)
        self.grid()

        self.title = title


class DigitalClockFrame(Frame):
    '''
    Digital clock with red numbers and a 12/24 hour display. 
    '''
    def __init__(self, master, title):
        'Creates the display.'
        Frame.__init__(self, master)
        self.grid()

        self.title = title

        self.canvas = Canvas(self, height=190, width=665, bg='black')
        self.canvas.grid()

    def update_time(self):
        'Inserts the current time imto the canvas.'
        now = datetime.datetime.now().time()
        self.canvas.delete('all')
        self.canvas.create_text(335, 70, font = ('Courier', 50),
                                text = now, fill = '#D4AF37')
        self.canvas.create_text(335, 125, font = ('Courier', 50),
                                text = datetime.datetime.now().date(),
                                fill = '#D4AF37')


class BrowserFrame(Frame):
    'Shortcuts to websites.'
    def __init__(self, master, title):
        Frame.__init__(self, master)
        self.grid()

        self.title = title

        self.b_membean = Button(self, text='Membean', command=self.membean)
        self.b_discovery = Button(self, text='Discovery', command=self.discover)
        self.b_synergy = Button(self, text='StudentVUE', command=self.synergy)
        self.b_membean.grid()
        self.b_discovery.grid(row=0, column=1)
        self.b_synergy.grid(row=0, column=2)

        self.custom_url = Text(self, height=1, width=30)
        self.custom_url.grid(row=1, column=0, columnspan=3)

        self.b_custom = Button(self, text='Custom URL', command=self.custom)
        self.b_custom.grid(row=2, column=0, sticky=W)

    def membean(self):
        'Opens Membean.'
        webbrowser.open('www.membean.com/dashboard')

    def discover(self):
        'Opens Discovery.'
        webbrowser.open('app.discoveryeducation.com/learn/students')

    def synergy(self):
        'Opens StudentVUE.'
        webbrowser.open('https://wa-bsd405-psv.edupoint.com/\
PXP2_Login_Student.aspx?regenerateSessionId=True')

    def custom(self):
        'Opens the custom URL.'
        webbrowser.open(END, self.custom_url.get())


class WalkerFrame(Frame):
    '''
    File walker.
    '''
    def __init__(self, master, title):
        'Creates the display.'
        Frame.__init__(self, master)
        self.grid()

        self.title = title

        self.current_extensions = set({})

        Label(self, text='Extension').grid()
        Label(self, text='Extensions\nto find').grid(row=1)


        self.extension = Entry(self)
        self.extension.grid(row=0, column=1)

        self.extension.bind('<Return>', self.add_extension)

        self.extensions = Listbox(self)
        self.extensions.grid(row=1, column=1)

        Button(self, text='Add', command=lambda: self.add_extension(2))\
                     .grid(row=0, column=1, sticky=E)
        Button(self, text='Clear', command=self.clear).grid(row=1, column=1,
                                                            sticky=SE)
    def add_extension(self, ev):
        'Adds a file extension to the listbox.'
        if not self.extension.get().isalnum():
            msg.showinfo(title='You can\'t do that',
                         message='Extension ' + self.extension.get() + \
                         ' is not alphanumeric.\nDo not include the period.')
            return
        if self.extension.get() in self.current_extensions:
            msg.showinfo(title='You can\'t do that',
                         message='Extension ' + self.extension.get() + \
                         ' is already in the list.')
            return

        self.current_extensions.add(self.extension.get())
        self.extensions.insert(END, self.extension.get())
        self.extension.delete(0, END)

    def delete_selection(self, ev):
        'Deletes the selected item from the listbox.'
        pass

    def clear(self):
        'Clears the listbox.'
        for i in range(int(len(self.extensions.get('@1,0', END)) / 10) + 1):
            self.extensions.delete('@1,0', END)

    def walk(self, root, endings):
        'Not finished'
        current_dir = os.listdir(root)

        for file in current_dir:

            current_name = root + '\\' + file

            if '.' in file:
                #This is a file, and not a folder.
                for ending in endings:
                    pass

            else:
                self.walk(current_name)

        
        
class ClickerFrame(Frame):
    '''
    Auto clicker with one location.
    '''
    def __init__(self, master, title):
        'Creates the display.'
        Frame.__init__(self, master)
        self.grid()

        self.title = title
        self.check = StringVar()
        Label(self, text='Number of clicks').grid(row=0)
        self.number = Entry(self)
        self.number.grid(row=1)
        Button(self, text='?', command=self.chelp, width=1).grid(row=1, column=1)
        Label(self, text='CPS').grid(row=2)
        self.between = Entry(self)
        self.between.grid(row=3)
        Button(self, text='?', command=self.shelp, width=1).grid(row=3, column=1)

        
        self.location = Entry(self, width=10)
        self.location.grid(row=7, sticky=W)
        self.locationy = Entry(self, width=10)
        self.locationy.grid(row=7, sticky=E)
        Button(self, text='?', command=self.lhelp, width=1).grid(row=7, column=1)
        Label(self, text='Current mouse location').grid(row=11)
        self.pos = Text(self, height=0, width=11, font=('Calibri, 14'))
        self.pos.grid(row=12)
        Radiobutton(self, text='Left', variable=self.check,
                    value='left').grid(row=4)
        Radiobutton(self, text='Middle', variable=self.check,
                    value='middle').grid(row=5)
        Radiobutton(self, text='Right', variable=self.check,
                    value='right').grid(row=6)
        if CAN_STOP:
            Button(self, text='Start Clicking\nFN+F4 to stop',
                   command=self.clicking).grid(row=0, column=2, rowspan=3)
        else:
            Button(self, text='Start Clicking',
                   command=self.clicking).grid(row=0, column=2, rowspan=3)
        Label(self, text='Clicks so far').grid(column=2, row=9)
        self.clicks = Text(self, height=1, width=7, font=('Calibri', 20))
        self.clicks.grid(row=10, column=2, rowspan=3)
    
    def clicking(self):
        '''
        Starts clicking.
        '''

        if self.check.get() == '': f = 1
        else: f = int(self.check.get())
        if self.number.get() == '': g = 'q'
        else: g = int(self.number.get())
        if self.between.get() == '': h = 0
        else: h = 1/float(self.between.get())
        for i in range(1, 1000):
            self.pos.delete(1.0, END)
            self.update_position()
            self.update()
        amount = 0
        if g == 'q':
            i = 0
            while True:
                if self.location.get() == '': click(button=f)
                else: click(x=int(self.location.get()),
                            y=(self.locationy.get()), button=f)
                try:
                    self.clicks.delete(1.0, END)
                except:
                    pass
                i += 1
                self.clicks.insert(END, str(i))
                self.pos.delete(1.0, END)

                self.update_position()
                self.update()
                time.sleep(h)
                if CAN_STOP:
                    if keyboard.is_pressed('F4'):
                        return
        else:
            for i in range(0, g + 1):
                if self.location.get() == '': click(button=f)
                else: click(x=int(self.location.get()),
                            y=(self.locationy.get()), button=f)
                try:
                    self.clicks.delete(1.0, END)
                except:
                    pass
                self.clicks.insert(END, str(i))
                self.pos.delete(1.0, END)

                self.update_position()
                self.update()
                time.sleep(h)
                if CAN_STOP:
                    if keyboard.is_pressed('F4'):
                        return



    def lhelp(self):
        msg.showinfo(title='Coordinates help', message='''
    X in the left box, Y in the right box.
    Leave blank to click at your mouse position.
    Otherwise, it will click at the position you have entered.''')
    def chelp(self):
        msg.showinfo(title='Clicks help', message='''
    Leave blank to click until F4.
    Otherwise, it will click the number of times you have entered.''')
    def shelp(self):
        msg.showinfo(title='CPS help', message='''
    Leave blank to click as fast as possible.
    Otherwise, it will click at the speed you entered.''')
    def update_position(self):
            self.pos.delete(1.0, END)
            self.pos.insert(END, str(position()[0]) + ', ' + str(position()[1]))
        

def main():
    root = Tk()
    root.title

    f = Label(root,
              text='School Functionality Reimagined', font=('Calibri', 24))
    f.grid()
    note = ttk.Notebook(root)
    note.grid(row=1)

    std_calc = CalcFrame(note, 'Standard Calculator')
    sci_calc = SciCalcFrame(note, 'Scientific Calculator')
    dig_clock = DigitalClockFrame(note, 'Digital Clock')
    browse = BrowserFrame(note, 'Browser')
    walker = WalkerFrame(note, 'File Walker')
    clicker = ClickerFrame(note, 'Auto Clicker')

    frames = {'Standard Calculator': std_calc,
              'Scientific Calculator': sci_calc,
              'Digital Clock': dig_clock,
              'Browser': browse,
              'File Walker': walker,
              'Auto Clicker': clicker}

    for frame in frames:
        mf = frames[frame]
        note.add(mf, text=mf.title)

    while True:
        dig_clock.update_time()
        clicker.update_position()
        root.update()


if __name__ == '__main__':
    main()
