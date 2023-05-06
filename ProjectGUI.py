import tkinter
from tkinter import *
from tkinter.ttk import *
import ServerConnection as SC
import mysql.connector

conn = mysql.connector.connect(user='Aus', password='Alpaca44!', host='LAPTOP-PV1LLGSA', database='baseball')

class Box:
    def __init__(self, gui):
        tableNames = SC.GrabTables(conn)
        dlabel = Label(gui, text="Pick a player or team and a given category.\nTeams begin with 'team_'.").grid(column=1, row=1, padx=300)
        dFrame = Frame(gui)
        dFrame.grid(column=1, row=2, padx=300)
        self.clicked_val = tkinter.StringVar()
        Drop = Combobox(dFrame, textvariable=self.clicked_val)
        Drop['values'] = tableNames
        Drop.grid(column=1, row=2, padx=300)

        # Creating button to actually show stats
        Drop.bind("<<ComboboxSelected>>", self.Table)

    def Table(self, gui):
        root = Tk() # Creating a new window
        conn = mysql.connector.connect(user='Aus', password='Alpaca44!', host='LAPTOP-PV1LLGSA', database='baseball')
        temp = self.clicked_val.get() # Referencing the clicked object
        data = SC.GrabAllData(conn, temp)
        for i in range(len(data)):
            self.e = Entry(root, width=100, font=('Arial', 10, 'bold'))
            self.e.grid(row=i, column=0)
            self.e.insert(END, data[i])


# Creating the outline and the title
gui = Tk()
gui.title("3380 Project - Austin Brewer")
gui.geometry('1000x1000')
label = Label(gui, text="MLB Database").grid(column=1, row=0, pady=25, padx=300)

# Making the box and the table

b=Box(gui)



gui.mainloop()
