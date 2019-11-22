'''
This is a program to implement the judgy hexagons from real life.
Idea by Aileen Liang/Hanting Li
Implemented in Python by Owen Fei


Tutorial on judgy hexagons in real life:
First, draw like 8 nested hexagons.
Connect all the points with 6 lines.
Label each of the lines with a trait (should be the traits below).
For each of the traits, rank them from 1-8 and draw the point on the line.
The outer hexagons are higher.
Now, connect all 6 points, and color in the polygon made by them.
'''

from tkinter import (Tk, Frame, Label, Scale, Canvas, Menu, N, S, E, W,
                     SE, SW, NE, NW, messagebox as msg, HORIZONTAL, Entry, END)

class App(Tk):
    def __init__(self, *args, **kwargs):
        '''
        the ui stuff
        '''
        super().__init__(*args, **kwargs)
        

        self.winfo_toplevel().title('Judgy Hexagon')

        #Menu for a bit of documentation and help
        self.menu = Menu(self)
        self.menu.add_command(label='Help', command=self.help)
        self.menu.add_command(label='People', command=self.people)
        self.config(menu=self.menu)
        


        #the main canvas to show the hexagon
        self.canvas = Canvas(self, height=566, width=800)
        self.canvas.grid(row=1, column=1)

        
        #frame to put all the sliders in
        self.sf = Frame(self)
        self.sf.grid(row=1, column=3)

        #entries for the trait names (with default values)
        self.sl1 = Entry(self.sf)
        self.sl1.grid(row=0, column=0)
        self.sl1.insert(END, 'IQ')
        self.sl2 = Entry(self.sf, text='EQ')
        self.sl2.grid(row=1, column=0)
        self.sl2.insert(END, 'EQ')
        self.sl3 = Entry(self.sf)
        self.sl3.grid(row=2, column=0)
        self.sl3.insert(END, 'Attractiveness')
        self.sl4 = Entry(self.sf)
        self.sl4.grid(row=3, column=0)
        self.sl4.insert(END, 'Personality')
        self.sl5 = Entry(self.sf)
        self.sl5.grid(row=4, column=0)
        self.sl5.insert(END, 'Athleticism')
        self.sl6 = Entry(self.sf)
        self.sl6.grid(row=5, column=0)
        self.sl6.insert(END, 'Artisticness')


        #sliders
        self.t1scale = Scale(self.sf, from_=0, to=9, orient=HORIZONTAL)
        self.t1scale.grid(column=1, row=0)
        self.t2scale = Scale(self.sf, from_=0, to=9, orient=HORIZONTAL)
        self.t2scale.grid(column=1, row=1)
        self.t3scale = Scale(self.sf, from_=0, to=9, orient=HORIZONTAL)
        self.t3scale.grid(column=1, row=2)
        self.t4scale = Scale(self.sf, from_=0, to=9, orient=HORIZONTAL)
        self.t4scale.grid(column=1, row=3)
        self.t5scale = Scale(self.sf, from_=0, to=9, orient=HORIZONTAL)
        self.t5scale.grid(column=1, row=4)
        self.t6scale = Scale(self.sf, from_=0, to=9, orient=HORIZONTAL)
        self.t6scale.grid(column=1, row=5)

        #the labels to make clear which line is which trait
        self.l1 = Label(self, text=self.sl1.get(),
              font=('Calibri', 20))
        self.l1.grid(row=1, column=2, sticky=E) 
        self.l2 = Label(self, text=self.sl2.get(),
              font=('Calibri', 20))
        self.l2.grid(row=1, column=1, sticky=SE)
        self.l3 = Label(self, text=self.sl3.get(),
              font=('Calibri', 20))
        self.l3.grid(row=1, column=1, sticky=SW)
        self.l4 = Label(self, text=self.sl4.get(),
              font=('Calibri', 20))
        self.l4.grid(row=1, column=0, sticky=W)
        self.l5 = Label(self, text=self.sl5.get(),
              font=('Calibri', 20))
        self.l5.grid(row=1, column=1, sticky=NW)
        self.l6 = Label(self, text=self.sl6.get(),
              font=('Calibri', 20))
        self.l6.grid(row=1, column=1, sticky=NE) #:)



        #put the person's name in here
        self.nameentry = Entry(self.sf)
        self.nameentry.grid(row=7, column=1)

        Label(self.sf, text='\n\nName of person\n\n').grid(row=7, column=0)
        
        
        self.namelabel = Label(self, text='Name', font=('Calibri', 20), fg='red')
        self.namelabel.grid(row=0, column=1)

        
        #6 lists of points
        self.listright = [(400+40*i, 200*2**0.5)
                          for i in range(10)]
        self.listrightdown = [(400+20*i, 200*2**0.5+i*20*2**0.5)
                              for i in range(10)]
        self.listleftdown = [(400-20*i, 200*2**0.5+i*20*2**0.5)
                              for i in range(10)]
        self.listleft = [(400-40*i, 200*2**0.5)
                         for i in range(10)]
        self.listleftup = [(400-20*i, 200*2**0.5-i*20*2**0.5)
                           for i in range(10)]
        self.listrightup = [(400+20*i, 200*2**0.5-i*20*2**0.5)
                            for i in range(10)]
        


        
        #Draw the 10 hexagons
        for i in range(10):
            self.canvas.create_polygon([self.listright[i][0],
                                        self.listright[i][1],
                                        self.listrightdown[i][0],
                                        self.listrightdown[i][1],
                                        self.listleftdown[i][0],
                                        self.listleftdown[i][1],
                                        self.listleft[i][0],
                                        self.listleft[i][1],
                                        self.listleftup[i][0],
                                        self.listleftup[i][1],
                                        self.listrightup[i][0],
                                        self.listrightup[i][1],],
                                        fill='', width=1, outline='black')
            
    def help(self):
        msg.showinfo(title='Help', message='''
How to use this app:
Move around the sliders and enter a name.
Type your 6 character traits in the 6 entries.
Then, take a snip of the part without the sliders.

Tutorial on judgy hexagons in real life:
First, draw like 8 nested hexagons.
Connect all the points with 6 lines.
Label each of the lines with a trait (should be the traits below).
For each of the traits, rank them from 1-8 and draw the point on the line.
The outer hexagons are higher.
Now, connect all 6 points, and color in the polygon made by them.''')

    def people(self):
        msg.showinfo(title='People', message='''
List of people related to this:

Ideas: Aileen Liang (probably more this person), Hanting Li
Python implementation: Owen Fei
Another app to check out: Owen Zhang''')

                                      
    def judge(self, t1, t2, t3, t4, t5, t6):
        '''
        Draws the filled-in polygon in blue.
        '''

        #Get which point each level of trait is
        t1 = self.listright[t1]
        t2 = self.listrightdown[t2]
        t3 = self.listleftdown[t3]
        t4 = self.listleft[t4]
        t5 = self.listleftup[t5]
        t6 = self.listrightup[t6]

        #REmove the last shape if possible
        try:
            self.canvas.delete(self.last_polygon)
        except:
            pass

        #Draw the new polygon
        self.last_polygon = self.canvas.create_polygon([t1[0],
                                                        t1[1],
                                                        t2[0],
                                                        t2[1],
                                                        t3[0],
                                                        t3[1],
                                                        t4[0],
                                                        t4[1],
                                                        t5[0],
                                                        t5[1],
                                                        t6[0],
                                                        t6[1],],
                                                        fill='blue',
                                                        width=1,
                                                        outline='blue')
        self.canvas.update()

    def main(self):
        '''
        Constantly draws the new polygon.
        Constantly updates the name.
        '''
        while True:
            #Update the name
            self.namelabel.config(text=self.nameentry.get())

            #Call judge() on the values of the sliders
            self.judge(self.t1scale.get(),
                       self.t2scale.get(),
                       self.t3scale.get(),
                       self.t4scale.get(),
                       self.t5scale.get(),
                       self.t6scale.get())

            #Updates the labels with trait names.
            self.l1.config(text=self.sl1.get())
            self.l2.config(text=self.sl2.get())
            self.l3.config(text=self.sl3.get())
            self.l4.config(text=self.sl4.get())
            self.l5.config(text=self.sl5.get())
            self.l6.config(text=self.sl6.get())
            

            
            self.update()

            
        


if __name__ == '__main__':    
    app = App()
    app.main()
            
