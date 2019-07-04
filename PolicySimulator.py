from tkinter import *
import os
import _thread

FILE = f'c:\\classpolicy\\{os.getlogin()}.jpeg'

class SimFrame(Frame):
    def __init__(self, master, title):
        Frame.__init__(self, master)
        self.grid()

        self.title = title

        self.update_button = Button(self, text='Update ClassPolicy',
                                    command=self.place_file,
                                    font=('Calibri', 24))
        self.update_button.grid(padx=10, pady=10)

    @staticmethod
    def place_file():
        with open(FILE, 'w+') as f:
            f.close()


def main():
    root = Tk()
    root.title('ClassPolicy Simulator')
    root.attributes('-topmost', 1)
    l = LabelFrame(root, text='Click to simulate ClassPolicy')
    l.grid(padx=10, pady=10)
    s = SimFrame(l, 'thing')
    s.grid()

    root.mainloop()

if __name__ == '__main__':
    _thread.start_new_thread(main, ())
