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

iq = IQ
eq = EQ
att = Attractiveness
inn = Innocence
ath = Athleticness
art = Artisticness

'''

from tkinter import *

class App(Tk):
    def __init__(self, *args, **kwargs):
        '''
        the ui stuff
        '''
        super().__init__(*args, **kwargs)

        self.winfo_toplevel().title('Judgy Hexagon')

        #Menu for a bit of documentation and help
        self.menu = Menu(self)
      


        #the main canvas to show the hexagon
        self.canvas = Canvas(self, height=800, width=560)
        self.canvas.grid(row=1, column=1)

        
        #the labels to make clear which side is which
        Label(self, text='IQ', font=('Calibri', 20)).grid(row=1,
                                                          column=1, sticky=N) 
        Label(self, text='\n' * 6 + 'EQ',
              font=('Calibri', 20)).grid(row=1, column=2, sticky=N)
        Label(self, text='Attractiveness' + '\n' * 6,
              font=('Calibri', 20)).grid(row=1, column=2, sticky=S)
        Label(self, text='Innocence',
              font=('Calibri', 20)).grid(row=1, column=1, sticky=S)
        Label(self, text='Athleticism' + '\n' * 6,
              font=('Calibri', 20)).grid(row=1, column=0, sticky=S)
        Label(self, text='\n' * 6 + 'Artisticness',
              font=('Calibri', 20)).grid(row=1, column=0, sticky=N)

        #frame to put all the sliders in
        self.sf = Frame(self)
        self.sf.grid(row=1, column=3)

        self.iqscale = Scale(self.sf, from_=0, to=7, orient=HORIZONTAL)
        self.iqscale.grid(column=1, row=0)
        self.eqscale = Scale(self.sf, from_=0, to=7, orient=HORIZONTAL)
        self.eqscale.grid(column=1, row=1)
        self.attscale = Scale(self.sf, from_=0, to=7, orient=HORIZONTAL)
        self.attscale.grid(column=1, row=2)
        self.innscale = Scale(self.sf, from_=0, to=7, orient=HORIZONTAL)
        self.innscale.grid(column=1, row=3)
        self.athscale = Scale(self.sf, from_=0, to=7, orient=HORIZONTAL)
        self.athscale.grid(column=1, row=4)
        self.artscale = Scale(self.sf, from_=0, to=7, orient=HORIZONTAL)
        self.artscale.grid(column=1, row=5)

        Label(self.sf, text='IQ').grid(row=0, column=0)
        Label(self.sf, text='EQ').grid(row=1, column=0)
        Label(self.sf, text='Attractiveness').grid(row=2, column=0)
        Label(self.sf, text='Innocence').grid(row=3, column=0)
        Label(self.sf, text='Athleticism').grid(row=4, column=0)
        Label(self.sf, text='Artisticness').grid(row=5, column=0)

        #put the person's name in here
        self.nameentry = Entry(self.sf)
        self.nameentry.grid(row=7, column=1)

        Label(self.sf, text='\n\nName of person\n\n').grid(row=7, column=0)
        
        
        self.namelabel = Label(self, text='Name', font=('Calibri', 20),
                               fg='red')
        self.namelabel.grid(row=1, column=1, sticky=NE)

        #6 lists of points for each of the 6 lines
        self.listup = [(280, y)
                       for y in range(400, -1, -50)]
        self.listupright = [(280+35*((400-y)/25), y)
                            for y in range(400, 199, -25)]
        self.listdownright = [(280+35*((y-400)/25), y)
                              for y in range(400, 601, 25)]
        self.listdown = [(280, y)
                         for y in range(400, 801, 50)]
        self.listdownleft = [(280-35*((y-400)/25), y)
                              for y in range(400, 601, 25)]
        self.listupleft = [(280-35*((400-y)/25), y)
                            for y in range(400, 199, -25)]


        #Draw the 8 hexagons
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
                                      
    def judge(self, t1, t2, t3, t4, t5, t6):
        '''
        Draws the filled-in polygon in blue.
        '''

        #Get which point each level of trait is
        iq = self.listup[t1]
        eq = self.listupright[t2]
        att = self.listdownright[t3]
        pr = self.listdown[t4]
        ath = self.listdownleft[t5]
        ef = self.listupleft[t6]

        #REmove the last shape if possible
        try:
            self.canvas.delete(self.last_polygon)
        except:
            pass

        #Draw the new polygon
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
        '''
        Constantly draws the new polygon.
        Constantly updates the name.
        '''
        while True:
            #Update the name
            self.namelabel.config(text=self.nameentry.get())

            #Call judge() on the values of the sliders
            self.judge(self.iqscale.get(),
                       self.eqscale.get(),
                       self.attscale.get(),
                       self.innscale.get(),
                       self.athscale.get(),
                       self.artscale.get())
            self.update()


if __name__ == '__main__':    
    app = App()
    app.main()
            
