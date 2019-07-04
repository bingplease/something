import sys
import os
import time
import ctypes
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




class ClickerFrame(Frame):
    '''
    Auto clicker with one location.
    '''
    def __init__(self, master, title):
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
        self.pos = Text(self, height=0, wi#A group of function that simulate clicks.
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

dth=11, font=('Calibri, 14'))
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
        
if __name__ == '__main__':
    root = Tk()
    clicker = ClickerFrame(root, 'clicker')
    clicker.pack()
    while True:
        clicker.update_position()
        root.update()
        
