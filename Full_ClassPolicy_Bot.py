'''
This is a bot that blocks ClassPolicy (the screen record part).
Your teacher or parent can no longer see what you are doing.

This is also a bot that blocks minimization.
Your teacher cannot minimize your windows.

There are many options.

Be careful using this.
I am not resposible for anything that you get in trouble for.
'''

import os
import time
import filecmp
import shutil
import webbrowser
import ctypes

from _thread import start_new_thread
from tkinter import (Tk, Frame, Menu, Button, Radiobutton, Text, Label, IntVar,
                     END, N, S, E, W, DISABLED)
from tkinter.ttk import Combobox
from tkinter.colorchooser import askcolor
from tkinter.messagebox import (showinfo, showerror)
from tkinter.filedialog import askopenfilename

PREFERENCES = f'c:\\users\\{os.getlogin()}\\preferences.txt'

class ClassPolicy:
    '''
    This window will block the screen recording part
    and the minimization part of
    ClassPolicy and APParent.
    '''
    def __init__(self):
        #Creates a preferences file for the custom image
        if not os.path.exists(PREFERENCES):
            open(PREFERENCES, 'w+').close()
            os.system('attrib +s +h ' + PREFERENCES)

        self.user32 = ctypes.WinDLL('user32')
        self.disclaimers()
        self.create_ui()
        self.main()

    def disclaimers(self):
        '''
        Checks if the user is authorized.
        '''
        #People it has been sold to.
        if (#os.getlogin() != 's-libo' and #Bowen
            #os.getlogin() != 's-liangai' and #Aileen
            #os.getlogin() != 's-wuju' and #Justin
            os.getlogin() != 's-feio' and
            os.getlogin() != 'xiufei'):
            os.remove(__file__)
            showerror(title='Unauthorized use',
                      message='You are not authorized to use this.')
            
            showinfo(title='What now',
                     message='''The software was wiped from your computer.
                     Go actually buy a copy.''')
            raise
            exit()
            
    def create_ui(self):
        '''
        Creates the UI of the ClassPolicy bot.
        '''
        self.root = Tk()
        self.root.title('ClassPolicy')

        #Everything will use this font.
        self.font=('Calibri', 12)
        
        self.create_policy_frame()
        self.create_manager_frame()
        self.create_menus()

        self.policy_frame.grid()
        self.manager_frame.grid(column=0, row=1)

        self.root.resizable(width=False, height=False)
        self.root.config(menu=self.menubar)
        self.root.update()

	#Creating the window
    def create_policy_frame(self):
        '''
        Creates the frame of the screen record blocker.
        '''
        self.policy_frame = Frame(self.root)       


        #The UI.
        self.l1 = Label(self.policy_frame,
                        text='The last time your teacher used ClassPolicy',
                        font=self.font)
        self.l1.grid(row=0)

        self.last_used = Text(self.policy_frame, height=1, width=30,
                              font=self.font)
        self.last_used.grid(row=1)
        self.last_used.insert(END, 'Has not used yet')

        self.l2 = Label(self.policy_frame, text='Current time',
                        font=self.font)
        self.l2.grid(row=0, column=1)

        self.current = Text(self.policy_frame, height=1, width=17,
                            font=self.font)
        self.current.grid(row=1, column=1)

    def create_manager_frame(self):
        '''
        Creates the frame of the window manager.
        '''
        self.manager_frame = Frame(self.root)

        self.window_action = IntVar()
        self.window_action.set(2) #2 is minimixe, 3 is maximize, 4 is restore

        self.block = False

        self.window_label = Label(self.manager_frame,
                                  text='  Enter the window ID (s)  ',
                                  font=self.font)
        self.window_label.grid()

        self.entry = Text(self.manager_frame, font=self.font,
                          height=1, width=9)
        self.entry.grid(row=1, sticky=W)
        self.entry2 = Text(self.manager_frame, font=self.font,
                           height=1, width=9)
        self.entry2.grid(row=1, sticky=E)

        self.get_button = Button(self.manager_frame, text='Get Window ID',
                                 command=self.get, font=self.font)
        self.get_button.grid(row=2, column=0, sticky=W)

        self.start_button = Button(self.manager_frame, text='Start',
                                   command=self.start_block, font=self.font)
        self.start_button.grid(row=2, column=0, sticky=E)

        self.action_choice_1 = Radiobutton(self.manager_frame, text='Minimize',
                                           variable=self.window_action,
                                           value=2, font=self.font)
        self.action_choice_1.grid(row=0, column=1)

        self.action_choice_2 = Radiobutton(self.manager_frame, text='Maximize',
                                           variable=self.window_action,
                                           value=3, font=self.font)
        self.action_choice_2.grid(row=1, column=1)
        self.action_choice_3 = Radiobutton(self.manager_frame, text='Restore',
                                           variable=self.window_action,
                                           value=4, font=self.font)
        self.action_choice_3.grid(row=2, column=1, sticky=W)
    
    def create_menus(self):
        '''
        Created the menus.
        '''

        #IntVars for the menu options.
        self.stay_on_top = IntVar()
        self.stay_on_top.set(1)
        self.block_classpolicy = IntVar()
        self.block_classpolicy.set(1)
        self.use_custom = IntVar()
        self.use_custom.set(0)

        
        self.menubar = Menu(self.root, tearoff=0)

        #Option menu
        self.option_menu = Menu(self.menubar, tearoff=0)

        self.option_menu.add_command(label='Background Color',
                                    command=self.color)
        self.option_menu.add_command(label='Text Color',
                                    command=self.tcolor)
        self.option_menu.add_command(label='Text Box Background Color',
                                    command=self.bcolor)
        self.option_menu.add_command(label='Text Box Text Color',
                                    command=self.btcolor)
        self.option_menu.add_command(label='NOTE: COLORS ARE GLITCHY',          
                                     state=DISABLED)
        self.option_menu.add_separator()

        self.option_menu.add_checkbutton(label='Stay On Top',
                                        variable=self.stay_on_top,
                                        onvalue=1, offvalue=0)

        #Help menu
        self.help_menu = Menu(self.menubar, tearoff=0)
        self.help_menu.add_command(label='About this program',
                                   command=self.info)
        self.help_menu.add_command(label='About ClassPolicy',
                                   command=self.policyhelp)
        self.help_menu.add_command(label='Window Blocker help',
                                   command=self.show_help)

        self.help_menu.add_separator()
        self.help_menu.add_command(label='Take a short survey',
                                     command=self.open_survey)

        #File menu
        self.file_menu = Menu(self.menubar, tearoff=0)


        self.file_menu.add_checkbutton(label='Use Custom Image',
                                          variable=self.use_custom,
                                          onvalue=1, offvalue=0)
        self.file_menu.add_command(label='Change Custom Image',
                                      command=self.save_location)
        self.file_menu.add_command(label='View Custom Image',
                                      command=self.view_image)
        self.file_menu.add_separator()


        self.file_menu.add_checkbutton(label='Block ClassPolicy',
                                          variable=self.block_classpolicy,
                                          onvalue=1, offvalue=0)        
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Exit',
                                   command=self.policy_frame.destroy)

        #Add menus to root
        self.menubar.add_cascade(label='File', menu=self.file_menu)
        self.menubar.add_cascade(label='Properties', menu=self.option_menu)
        self.menubar.add_cascade(label='Help', menu=self.help_menu)

    #Customization
    def change_text(self):
        def on_closing():
            self.font = (str(font_name.get()), int(font_size.get()))
            top.destroy()

        top = Toplevel(self.root)
        
    def color(self):
        '''
        Changes the background color.

        So far, the only color changing thing that works fully.
        '''
        c = askcolor(title='Change background color')[1]
        self.root.config(background=c)
        self.l1.config(background=c)
        self.l2.config(background=c)
        self.window_label.config(background=c)
        self.manager_frame.config(background=c)
        self.policy_frame.config(background=c)
        self.action_choice_1.config(background=c)
        self.action_choice_2.config(background=c)
        self.action_choice_3.config(background=c)

        self.get_button.config(background=c)
        self.start_button.config(background=c)
        
    def tcolor(self):
        '''
        Changes the text color.
        '''
        c = askcolor(title='Change text color')[1]
        self.l1.config(fg=c)
        self.l2.config(fg=c)

    def bcolor(self):
        '''
        Changes the text box background color.
        '''
        c = askcolor(title='Change text box background color')[1]
        self.current.config(bg=c)
        self.last_used.config(bg=c)

    def btcolor(self):
        '''
        Changes the text box text color.
        '''
        c = askcolor(title='Change text box text color')[1]
        self.current.config(fg=c)
        self.last_used.config(fg=c)

    def info(self):
        '''
        About this program.
        '''
        showinfo(title='About this program',
                 message='''A quickly assembled ClassPolicy blocker.

Functions:

Blocks ClassPolicy
Checks if ClassPolicy is being used
Automatically shows or hides any window
''')

    def policyhelp(self):
        '''
        Explains how ClassPolicy works.
        '''
        text='''This document has 3 sections.
1: What ClassPolicy does
2: How it works
3:How it is blocked.
---------------------------------------------------------------------
1
'ClassPolicy is a simple, secure and powerful classroom
orchestration software for Windows devices.' - classpolicy.com
Basically, it lets the teachers know what you are doing.
There are two things the teacher can do.
Class View: The teacher sees low-quality versions of all screens.
Individual: They can view one person's screen in high-quality.

It can also create a lock screen on your computer that will disable it.

It can also prevent certain windows from opening.

2
This is how ClassPolicy gets your screen.
Your teacher presses the 'Update' button on their computer.
First, it creates a .jpeg file and a .bmp file.
These are screenshots of your screens.
The .jpeg file is what is shown on Class View.
It will update on your teacher's computer.

3
The .jpeg file is deletable.
This program constantly deletes or replaces that file.
If a screenshot appears, that means ClassPolicy is being used.
'''
        showinfo(title='About ClassPolicy', message=text)

    def open_survey(self):
        '''
        Opens the survey link in the default web browser.
        '''
        webbrowser.open('https://forms.gle/ajsKru5EzrwZAiPE8')
        showinfo(title=f'Thanks, {os.getlogin()}',
                 message='Thanks for wanting to improve this service.')

    #Functions of the screen record blocker

    def get_location(self):
        '''
        Sees what is currently in the preferences.txt file.
        '''
        with open(PREFERENCES, 'r') as file:
            content = file.read()
            file.close()
            return content

    def save_location(self):
        '''
        Chooses a new image file.
        '''
        content = askopenfilename(title='Open image')
        if content != '':
            with open(PREFERENCES, 'w') as file:
                file.write(content)
                file.close()

        else:
            self.use_custom.set(0)

    def view_image(self):
        '''
        Shows file path of current image.
        '''
        showinfo(title='File path', message=self.get_location())

    def insert_last_used(self):
        '''
        Inserts the current time imto the last used box.
        '''
        try:
            self.last_used.delete(1.0, END)
            self.last_used.insert(END, self.format_time(time.localtime()))
            self.root.update()
        except:
            pass

    def insert_current_time(self):
        '''
        Inserts the current time into the current time box.
        '''
        try:
            self.current.delete(1.0, END)
            self.current.insert(END, self.format_time(time.localtime()))
            self.root.update()
        except:
            pass


    def format_time(self, now=time.localtime()):
        '''
        Formats the current time into a more readable format.
        '''
        now = list(now)
        if now[5] < 10:
            now[5] = '0' + str(now[5])
        if int(now[3]) == 0:
            now[3] = 12
        if len(str(now[3])) == 1:
            now[3] = '0' + str(now[3])
        if len(str(now[4])) == 1:
            now[4] = '0' + str(now[4])
        return str(str(now[3]) + ':' + str(now[4]) + ':' + str(now[5]) +
                   '  ' + str(now[1]) + '/' + str(now[2]) + '/' + str(now[0]))

    def check_classpolicy(self):
        if self.use_custom.get() == 1 and self.get_location() != '':            #Using custom image
            try:
                shutil.copy(self.get_location(),
                        f'c:\\classpolicy\\{os.getlogin()}.jpeg')
            except:
                pass
                        #Copies personal file to ClassPolicy folder

            try:
                same = filecmp.cmp(
                    self.get_location(),
                    f'c:\\classpolicy\\{os.getlogin()}.jpeg')
            except:
                same = False
            if same == False:
                self.insert_last_used()
                try:
                    os.remove(f'c:\\classpolicy\\{os.getlogin()}.jpeg')
                except:
                    pass

        elif self.use_custom.get() == 1 and self.get_location() == '':
            #Need to set a custom image
            self.save_location()

        else:
            #Not using custom image
            if os.path.exists(f'c:\\classpolicy\\{os.getlogin()}.jpeg'):
                #If the ClassPolicy file gets created
                self.insert_last_used()
                try:
                    os.remove(f'c:\\classpolicy\\{os.getlogin()}.jpeg')
                except:
                    pass

    #Functions for the window manager

    def start_block(self):
        '''
        Start constantly doing things to windows.
        '''
        #Makes it work with both window IDs and window titles
        if (self.entry.get(1.0, END).strip() == '' and
            self.entry2.get(1.0, END).strip() == ''):
            return
        
        try:
            int(self.entry.get(1.0, END))
            self.window_id = int(self.entry.get(1.0, END))
        except:
            self.window_id = self.user32.FindWindowW(None,
                                                     self.entry.get(1.0, END))

        #REpeat for second entry box
        try:
            int(self.entry2.get(1.0, END))
            self.window_id2 = int(self.entry2.get(1.0, END))
        except:
            self.window_id2 = self.user32.FindWindowW(None,
                                                     self.entry2.get(1.0, END))
        if self.window_id2 == 0 and self.window_id == 0:
            return

        self.block = True
        self.start_button.config(text='Stop', command=self.stop_block)

    def stop_block(self):
        '''
        Stops constantly doing things to windows.
        '''
        self.block = False
        self.start_button.config(text='Start', command=self.start_block)
        self.root.update()
        
    def get(self):
        '''
        Gets a window id.
        '''
        self.root.update()
        time.sleep(3)
        #Puts the ID into the correct box.
        if self.entry.get(1.0, END).strip() == '':
            self.entry.delete(1.0, END)
            self.entry.insert(END, self.user32.GetForegroundWindow())
        else:
            self.entry2.delete(1.0, END)
            self.entry2.insert(END, self.user32.GetForegroundWindow())

    def survey(self):
        '''
        Opens up the feedback survey.
        '''
        webbrowser.open()
        showinfo(master=self.root, title='Thanks, ' + os.getlogin(),
                 message='Thanks for wanting to improve this service.')

    def show_help(self):
        '''
        Shows some help.
        '''
        showinfo(master=self.root, title='Help', message='''
How to use this software:

To get a window ID, click on the Get Window ID button.
There will be a 3 second countdown, in which you
will need to select a window by clicking on it.
Then, the window ID will be entered into the entry box.

If you know for sure the window title, just enter that into the box.

Tips:
During the AP Parent screen lock, use the Minimize function on it.

During the ClassPolicy window minimizer, use the Restore function.
Select the window you want to have open because after
ClassPolicy starts there is no way to get it.

If you want to open up multiple windows, then
''')

    def main(self):
        '''
        Main loop.

        Replaces or deletes the ClassPolicy file.
        Checks if ClassPolicy is being used.
        Updates the UI.
        Does things to windows.
        '''
        while True:
            if self.block_classpolicy.get() == 1:
                self.check_classpolicy()

            self.insert_current_time()

            if self.block:
                #Actual modifying of the chosen windows.
                if self.window_id != 0:
                    self.user32.ShowWindow(int(self.window_id),
                                           int(self.window_action.get()))
                if self.window_id2 != 0:
                    self.user32.ShowWindow(int(self.window_id2),
                                           int(self.window_action.get()))

            if self.stay_on_top.get() == 1:
                self.root.attributes('-topmost', 1)
                if not self.root.winfo_ismapped():
                    self.root.deiconify()

                    
if __name__ == '__main__':
    start_new_thread(ClassPolicy, ())
