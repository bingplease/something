'''


iq = IQ
eq = EQ
att = Attractiveness
pr = Personality
ath = Athleticness
ef = Artisticness

'''

from tkinter import *

DOT_RAD = 5

class App(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.winfo_toplevel().title('Judgy Hexagon')

        self.canvas = Canvas(self, height=800, width=560)
        self.canvas.grid(row=1, column=1)

        

        Label(self, text='IQ').grid(row=1, column=1, sticky=N) 
        Label(self, text='\n' * 12 + 'EQ').grid(row=1, column=2, sticky=N)
        Label(self, text='Attractiveness' + '\n' * 12).grid(row=1, column=2,
                                                            sticky=S)
        Label(self, text='Personality').grid(row=1, column=1, sticky=S)
        Label(self, text='Athleticness' + '\n' * 12).grid(row=1, column=0,
                                                         sticky=S)
        Label(self, text='\n' * 12 + 'Artisticness').grid(row=1, column=0,
                                                    sticky=N)

        self.sf = Frame(self)
        self.sf.grid(row=1, column=3)

        self.iqscale = Scale(self.sf, from_=0, to=7, orient=HORIZONTAL)
        self.iqscale.grid(column=1, row=0)
        self.eqscale = Scale(self.sf, from_=0, to=7, orient=HORIZONTAL)
        self.eqscale.grid(column=1, row=1)
        self.attscale = Scale(self.sf, from_=0, to=7, orient=HORIZONTAL)
        self.attscale.grid(column=1, row=2)
        self.prscale = Scale(self.sf, from_=0, to=7, orient=HORIZONTAL)
        self.prscale.grid(column=1, row=3)
        self.athscale = Scale(self.sf, from_=0, to=7, orient=HORIZONTAL)
        self.athscale.grid(column=1, row=4)
        self.efscale = Scale(self.sf, from_=0, to=7, orient=HORIZONTAL)
        self.efscale.grid(column=1, row=5)

        Label(self.sf, text='IQ').grid(row=0, column=0)
        Label(self.sf, text='EQ').grid(row=1, column=0)
        Label(self.sf, text='Attractiveness').grid(row=2, column=0)
        Label(self.sf, text='Personality').grid(row=3, column=0)
        Label(self.sf, text='Athleticness').grid(row=4, column=0)
        Label(self.sf, text='Artisticness').grid(row=5, column=0)

        self.nameentry = Entry(self.sf)
        self.nameentry.grid(row=7, column=1)

        Label(self.sf, text='\n\nName of person\n\n').grid(row=7, column=0)
        
        
        self.namelabel = Label(self, text='Name', font=('Calibri', 20),
                               fg='red')
        self.namelabel.grid(row=1, column=1, sticky=NE)

        self.listup = [(280, y)
                       for y in range(350, -1, -50)]
        self.listupright = [(280+35*((400-y)/25), y)
                            for y in range(375, 199, -25)]
        self.listdownright = [(280+35*((y-400)/25), y)
                              for y in range(425, 601, 25)]
        self.listdown = [(280, y)
                         for y in range(450, 801, 50)]
        self.listdownleft = [(280-35*((y-400)/25), y)
                              for y in range(425, 601, 25)]
        self.listupleft = [(280-35*((400-y)/25), y)
                            for y in range(375, 199, -25)]


##        for i in self.listup:
##            self.canvas.create_oval(i[0] - DOT_RAD, i[1] - DOT_RAD, i[0] + DOT_RAD, i[1] + DOT_RAD,
##                                    fill='black')
##        for i in self.listupright:
##            self.canvas.create_oval(i[0] - DOT_RAD, i[1] - DOT_RAD, i[0] + DOT_RAD, i[1] + DOT_RAD,
##                                    fill='black')
##        for i in self.listdownright:
##            self.canvas.create_oval(i[0] - DOT_RAD, i[1] - DOT_RAD, i[0] + DOT_RAD, i[1] + DOT_RAD,
##                                    fill='black')
##        for i in self.listdown:
##            self.canvas.create_oval(i[0] - DOT_RAD, i[1] - DOT_RAD, i[0] + DOT_RAD, i[1] + DOT_RAD,
##                                    fill='black')
##        for i in self.listdownleft:
##            self.canvas.create_oval(i[0] - DOT_RAD, i[1] - DOT_RAD, i[0] + DOT_RAD, i[1] + DOT_RAD,
##                                    fill='black')
##        for i in self.listupleft:
##            self.canvas.create_oval(i[0] - DOT_RAD, i[1] - DOT_RAD, i[0] + DOT_RAD, i[1] + DOT_RAD,
##                                    fill='black')

        for i in range(8):
            self.canvas.create_polygon([self.listup[i][0],
                                       self.listup[i][1],
                                       self.listupright[i][0],
                                       self.listupright[i][1],
                                       self.listdownright[i][0],
                                       self.listdownright[i][1],
                                       self.listdown[i][0],
                                       self.listdown[i][1],
                                       self.listdownleft[i][0],
                                       self.listdownleft[i][1],
                                       self.listupleft[i][0],
                                       self.listupleft[i][1],],
                                       fill='', width=1, outline='black')
        self.canvas.create_line(self.listupleft[-1][0] + 2,
                                self.listupleft[-1][1],
                                self.listdownleft[-1][0] + 2,
                                self.listdownleft[-1][1])
                                
                                      
    def judge(self, t1, t2, t3, t4, t5, t6):
        iq = self.listup[t1]
        eq = self.listupright[t2]
        att = self.listdownright[t3]
        pr = self.listdown[t4]
        ath = self.listdownleft[t5]
        ef = self.listupleft[t6]

        try:
            self.canvas.delete(self.last_polygon)
        except:
            pass

        self.last_polygon = self.canvas.create_polygon([iq[0],
                                                        iq[1],
                                                        eq[0],
                                                        eq[1],
                                                        att[0],
                                                        att[1],
                                                        pr[0],
                                                        pr[1],
                                                        ath[0],
                                                        ath[1],
                                                        ef[0],
                                                        ef[1],],
                                                        fill='blue',
                                                        width=1,
                                                        outline='blue')
        self.canvas.update()

    def main(self):
        while True:
            self.namelabel.config(text=self.nameentry.get())
            self.judge(self.iqscale.get(),
                       self.eqscale.get(),
                       self.attscale.get(),
                       self.prscale.get(),
                       self.athscale.get(),
                       self.efscale.get())
            self.update()


            
app = App()
app.main()
        
