import os
import time
import filecmp
import shutil
import webbrowser
import ctypes
import _thread
from tkinter import (Tk, BooleanVar, Button, Checkbutton, Frame, IntVar,
                     Label, LabelFrame, Menu, Radiobutton, Text, Toplevel,
                     END, N, S, E, W,)
from tkinter.filedialog import askopenfilename
from tkinter.colorchooser import askcolor
from tkinter.messagebox import (showinfo, showerror)
from tkinter.ttk import Separator

MANAGER_USERS = [
    'xiufei',
    's-feio',
    ]

POLICY_USERS = [
    'xiufei',
    's-feio',
    's-libo',
    's-wuju',
    's-lianga',]

manager_use = os.getlogin() in MANAGER_USERS
policy_use = os.getlogin() in POLICY_USERS

#PREFERENCES is a file that stores the custon image path for CLassPolicy.
PREFERENCES = f'{os.path.dirname(__file__)}\\preferences.txt'
if not os.path.exists(PREFERENCES):
    open(PREFERENCES, 'w+').close()
    os.system('attrib +s +h ' + PREFERENCES)

class PolicyFrame(Frame):
    '''
    ClassPolicy screen record blocker.
    A custom image can be used.
    '''
    def __init__(self, master, title):
        Frame.__init__(self, master)
        self.grid()

        self.block = BooleanVar()
        self.block.set(True)
        self.use_custom = BooleanVar()
        self.use_custom.set(False)

        self.title = title

        self.l1 = Label(self,
                        text='The last time your teacher used ClassPolicy')
        self.l1.grid(row=0)

        self.last_used = Text(self, height=1, width=30)
        self.last_used.grid(row=1)
        self.last_used.insert(END, 'Has not used yet')

        self.l2 = Label(self, text='Current time')
        self.l2.grid(row=0, column=1)

        self.current = Text(self, height=1, width=20)
        self.current.grid(row=1, column=1)

        self.options = Frame(self)
        self.options.grid(row=2, column=0, columnspan=2, sticky=W)

        self.b_change = Button(self.options, text='Change Custom Image',
                               command=self.change_custom)
        self.b_change.grid()

        self.b_get_location = Button(self.options, text='Custom Image View',
                                     command=self.view_custom)
        self.b_get_location.grid(row=0, column=1)

        self.blocking = Checkbutton(self.options, text='Block CP',
                                    var=self.block, onvalue=True,
                                    offvalue=False)
        self.blocking.grid(row=0, column=2)

        self.using_custom = Checkbutton(self.options, text='Use Custom Image',
                                   var=self.use_custom, onvalue=True,
                                   offvalue=False)
        self.using_custom.grid(row=0, column=3)

    def format_time(self, now=time.localtime()):
        '''
        For
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
 
    def check(self):
        if self.use_custom.get() == 1 and self.get_custom() != '':
            #Using custom image
            try:
                shutil.copy(self.get_custom(),
                        f'c:\\classpolicy\\{os.getlogin()}.jpeg')
            except:
                pass
                        #Copies personal file to ClassPolicy folder

            try:
                same = filecmp.cmp(
                    self.get_custom(),
                    f'c:\\classpolicy\\{os.getlogin()}.jpeg')
            except:
                same = False
            if same == False:
                self.insert_last_used()
                try:
                    os.remove(f'c:\\classpolicy\\{os.getlogin()}.jpeg')
                except:
                    pass

        elif self.use_custom.get() == 1 and self.get_custom() == '':
            #Need to set a custom image
            self.change_custom()

        else:
            #Not using custom image
            if os.path.exists(f'c:\\classpolicy\\{os.getlogin()}.jpeg'):
                #If the ClassPolicy file gets created
                self.insert_last_used()
                try:
                    os.remove(f'c:\\classpolicy\\{os.getlogin()}.jpeg')
                except:
                    pass

    def update(self):
        self.insert_time()

    def get_custom(self):
        try:
            with open(PREFERENCES, 'r') as file:
                content = file.read()
                file.close()
                return content
        except PermissionError:
            showerror(title=' denied', message='''
Could not get the custom image.
Check your permissions.''')
            self.use_custom.set(0)

    def change_custom(self):
        content = askopenfilename(title='Open image')
        if content != '':
            try:
                with open(PREFERENCES, 'w+') as file:
                    file.write(content)
                    file.close()
            except PermissionError as err:
                print(err)
                self.use_custom.set(0)

        else:
            self.use_custom.set(0)

    def view_custom(self):
        pass

    def insert_time(self):
        self.current.delete(1.0, END)
        self.current.insert(END, self.format_time(time.localtime()))

    def insert_last_used(self):
        self.last_used.delete(1.0, END)
        self.last_used.insert(END, self.format_time(time.localtime()))


class ManagerFrame(Frame):
    def __init__(self, master, title):
        Frame.__init__(self, master)
        self.grid()

        self.title = title
        self.user32 = ctypes.WinDLL('user32')

        self.window_action = IntVar()
        self.window_action.set(2) #2 is minimixe, 3 is maximize, 4 is restore

        self.windowing = False
        self.block = False

        self.window_label = Label(self, text='Enter the window ID (s)',
                                  width=24)
        self.window_label.grid()

        self.entry = Text(self,
                          height=1, width=10)
        self.entry.grid(row=1, sticky=W)
        self.entry2 = Text(self,
                           height=1, width=10)
        self.entry2.grid(row=1, sticky=E)

        self.get_button = Button(self, text='Get Window ID',
                                 command=self.get)
        self.get_button.grid(row=2, column=0, sticky=W)

        self.start_button = Button(self, text='Start',
                                   command=self.toggle_start)
        self.start_button.grid(row=2, column=0, sticky=E)

        self.action_choice_1 = Radiobutton(self, text='Minimize',
                                           variable=self.window_action,
                                           value=2)
        self.action_choice_1.grid(row=0, column=1)

        self.action_choice_2 = Radiobutton(self, text='Maximize',
                                           variable=self.window_action,
                                           value=3)
        self.action_choice_2.grid(row=1, column=1)
        self.action_choice_3 = Radiobutton(self, text='Restore',
                                           variable=self.window_action,
                                           value=4)
        self.action_choice_3.grid(row=2, column=1, sticky=W)

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

    def toggle_start(self):
        '''
        Changes the value of self.windowing.
        '''
        self.windowing = not self.windowing
        print(self.windowing)

    def window_action(self):
        '''
        Start constantly doing things to windows.
        '''
        #Makes it work with both window IDs and window titles
        if (self.entry.get(1.0, END).strip() == '' and
            self.entry2.get(1.0, END).strip() == ''):
            showerror(title='Nah', message='No Window IDs')
            self.toggle_start()
            return
        
        try:
            int(self.entry.get(1.0, END))
            self.window_id = int(self.entry.get(1.0, END))
        except:
            self.window_id = self.user32.FindWindowW(None,
                                                     self.entry.get(1.0, END))
        
        print(self.user32.ShowWindow(self.window_id,
                               self.window_action.get()))

        #REpeat for second entry box
        try:
            int(self.entry2.get(1.0, END))
            self.window_id2 = int(self.entry2.get(1.0, END))
        except:
            self.window_id2 = self.user32.FindWindowW(None,
                                                      self.entry2.get(1.0, END))
        
        print(self.user32.ShowWindow(self.window_id2,
                               self.window_action.get()))

        self.block = True
        self.start_button.config(text='Stop', command=self.stop_window_action)

    def stop_window_action(self):
        '''
        Stops constantly doing things to windows.
        '''
        self.block = False
        self.start_button.config(text='Start')
        
    def get(self):
        '''
        Gets a window id.
        '''
        time.sleep(3)
        #Puts the ID into the correct box.
        if self.entry.get(1.0, END).strip() == '':
            self.entry.delete(1.0, END)
            self.entry.insert(END, self.user32.GetForegroundWindow())
        else:
            self.entry2.delete(1.0, END)
            self.entry2.insert(END, self.user32.GetForegroundWindow())


class Menubar(Menu):
    def __init__(self, root):
        Menu.__init__(self, root)
        self.root = root
        self.root.config(menu=self)

        self.options = Menu(self)
        self.options.add_command(label='Background Color',
                                 command=self.change_background)
        self.options.add_command(label='Text Color',
                                 command=self.change_text)
        self.options.add_command(label='Text Box Color',
                                 command=self.change_text_box)
        self.options.add_command(label='Text Box Text Color',
                                 command=self.change_text_box_text)

        self.add_cascade(label='Options', menu=self.options)

        self.help = Menu(self)
        self.help.add_command(label='About ClassPolicy', command=self.about)


        self.add_cascade(label='Help', menu=self.help)
        


    def change_background(self):
        color = askcolor()[1]
        self.root.config(bg=color)
        for i in self.root.grid_slaves():
            i.config(bg=color)
            for j in i.grid_slaves():
                j.config(bg=color)
                for k in j.grid_slaves():
                    k.config(bg=color)
                    for l in k.grid_slaves():
                        l.config(bg=color)
        
        

    def change_text(self):
        pass

    def change_text_box(self):
        pass

    def change_text_box_text(self):
        pass

    def about(self):
        tk = Toplevel(self.root)
        tk.title('About NoPolicy')
        Label(tk, text='NoPolicy', font=('Calibri', 20)).grid()
        Label(tk, text='BSD ClassPolicy Disabler and Window Manager').grid()
        Label(tk, text='\n\n\n\nemail: usemsedge@gmail.com').grid()
        Label(tk, text='https://www.github.com/pyva-group').grid()
        
        
        


def main():
    '''
    Opens up a window with both a manager and a screen record blocker.
    '''
    root = Tk()
    root.title('NoPolicy')
    
    #Strange.
##    try:
    root.iconbitmap(f'{os.getcwd()}\\pyva_icon.bmp')
##    except:
##        pass

    if policy_use and manager_use:
        #Can use both apps.
        frame = LabelFrame(root, text='Screen Record Blocker')
        frame.grid(columnspan=2, padx=10, pady=10)
        
        policy = PolicyFrame(frame, 'policy')
        policy.grid()
        
        frame2 = LabelFrame(root, text='Window Manager')
        frame2.grid(padx=10, pady=10)
    
        window = ManagerFrame(frame2, 'manager')
        window.grid()
        
        settings = LabelFrame(root, text='Settings')
        settings.grid(row=1, column=1, padx=10, pady=10)

    elif policy_use:
        #Can only use the blocker.
        frame = LabelFrame(root, text='Screen Record Blocker')
        frame.grid(padx=10, pady=10)
        
        policy = PolicyFrame(frame, 'policy')
        policy.grid()

        settings = LabelFrame(root, text='Settings')
        settings.grid(row=0, column=1, padx=10, pady=10)

    elif manager_use:
        #CAn only use the window manager.
        frame2 = LabelFrame(root, text='Window Manager')
        frame2.grid(padx=10, pady=10)
    
        window = ManagerFrame(frame2, 'manager')
        window.grid()

        settings = LabelFrame(root, text='Settings')
        settings.grid(row=0, column=1, padx=10, pady=10)

    top = BooleanVar()
    stay = Checkbutton(settings, text='Stay On Top', variable=top,
                       onvalue=True, offvalue=False)
    
    stay.grid()
    Button(settings, text='Quit', command=lambda: root.destroy()).grid()

    menu = Menubar(root)

    user = ctypes.WinDLL('user32')

    while True:
        if policy_use:
            if policy.block.get():
                #Check 
                policy.check()
            policy.update()
        if manager_use:
            if window.windowing:
                #Do action to window.
                window.window_action()
            else:
                window.stop_window_action()
        if top.get():
            #Stays on top of all other windows and cannot be minimized.
            if not root.winfo_ismapped():
                root.attributes('-topmost', 1)
                root.deiconify()

        root.update()
      

if __name__ == '__main__':
    main()
