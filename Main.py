import sqlite3
import tkinter as tk
from tkinter import messagebox

con = sqlite3.connect('Data.db')
print("Data being stored")

try:
    con.execute("""CREATE TABLE orders
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order STRING,
    orderstatus INTEGER""")
except Exception:
    print("Table already exists")

class graphicDobot(Tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)

        ButtHeight = 8
        Buttwidth = 20

        self.pos1col = "Black"
        self.pos2col = "Black"
        self.pos3col = "Black"
        self.pos4col = "Black"
        self.pos5col = "Black"        
        self.pos6col = "Black"
        self.pos7col = "Black"        
        self.pos8col = "Black"
        self.pos9col = "Black"
        self.pos10col = "Black"
        self.pos11col = "Black"
        self.pos12col = "Black"
        self.pos13col = "Black"
        self.pos14col = "Black"
        self.pos15col = "Black"
        self.pos16col = "Black"

        self.Build_GUI()

    def Build_GUI(self):
            self.pos1 = tk.Button(self, bg = self.pos1col, command = self.pos1but() , Height = ButtHeight, Width = Buttwidth)
            self.pos2 = tk.Button(self, bg = self.pos2col, command = self.pos2but() , Height = ButtHeight, Width = Buttwidth)
            self.pos3 = tk.Button(self, bg = self.pos3col, command = self.pos3but() , Height = ButtHeight, Width = Buttwidth)
            self.pos4 = tk.Button(self, bg = self.pos4col, command = self.pos4but() , Height = ButtHeight, Width = Buttwidth)
            self.pos5 = tk.Button(self, bg = self.pos5col, command = self.pos5but() , Height = ButtHeight, Width = Buttwidth)
            self.pos6 = tk.Button(self, bg = self.pos6col, command = self.pos6but() , Height = ButtHeight, Width = Buttwidth)
            self.pos7 = tk.Button(self, bg = self.pos7col, command = self.pos7but() , Height = ButtHeight, Width = Buttwidth)
            self.pos8 = tk.Button(self, bg = self.pos8col, command = self.pos8but() , Height = ButtHeight, Width = Buttwidth)
            self.pos9 = tk.Button(self, bg = self.pos9col, command = self.pos9but() , Height = ButtHeight, Width = Buttwidth)
            self.pos10 = tk.Button(self, bg = self.pos10col, command = self.pos10but() , Height = ButtHeight, Width = Buttwidth)
            self.pos11 = tk.Button(self, bg = self.pos11col, command = self.pos11but() , Height = ButtHeight, Width = Buttwidth)
            self.pos12 = tk.Button(self, bg = self.pos12col, command = self.pos12but() , Height = ButtHeight, Width = Buttwidth)
            self.pos13 = tk.Button(self, bg = self.pos13col, command = self.pos13but() , Height = ButtHeight, Width = Buttwidth)
            self.pos14 = tk.Button(self, bg = self.pos14col, command = self.pos14but() , Height = ButtHeight, Width = Buttwidth)
            self.pos15 = tk.Button(self, bg = self.pos15col, command = self.pos15but() , Height = ButtHeight, Width = Buttwidth)
            self.pos16 = tk.Button(self, bg = self.pos16col, command = self.pos16but() , Height = ButtHeight, Width = Buttwidth)

            self.FinBut = tk.Button(self, text = "Finish", command = self.FinishOrder())

            self.pos1.grid(row = 0, column = 0)
            self.pos2.grid(row = 0, column = 1)
            self.pos3.grid(row = 0, column = 2)
            self.pos4.grid(row = 0, column = 3)
            self.pos5.grid(row = 1, column = 0)
            self.pos6.grid(row = 1, column = 1)
            self.pos7.grid(row = 1, column = 2)
            self.pos8.grid(row = 1, column = 3)
            self.pos9.grid(row = 2, column = 0)
            self.pos10.grid(row = 2, column = 1)
            self.pos11.grid(row = 2, column = 2)
            self.pos12.grid(row = 2, column = 3)
            self.pos13.grid(row = 3, column = 0)
            self.pos14.grid(row = 3, column = 1)
            self.pos15.grid(row = 3, column = 2)
            self.pos16.grid(row = 3, column = 3)

            self.FinBut.grid(row = 3, column = 4)
            

    def FinishOrder(self):
        UIColors = [self.pos1col,self.pos2col,self.pos3col,self.pos4col,self.pos5col,self.pos6col,self.pos7col,self.pos8col,self.pos9col,self.pos10col,self.pos11col,self.pos12col,self.pos13col,self.pos14col,self.pos15col,self.pos16col]
        
        redblocks = 0
        greenblocks = 0
        yellowblocks = 0
        blueblocks = 0

        ordernr = []

        for i in UIColors:
            if i == "Black":
                ordernr.append("0")
            elif i == "Red":
                redblocks += 1
                if redblocks > 4:
                    continue
                ordernr.append("1")
            elif i == "Green":
                greenblocks += 1
                if greenblocks > 4:
                    continue
                ordernr.append("2")
            elif i == "Yellow":
                yellowblocks += 1
                if yellowblocks > 4:
                    continue
                ordernr.append("3")
            elif i == "Blue":
                blueblocks += 1
                if bluelocks > 4:
                    continue
                ordernr.append("4")

        if len(ordernr) != 16:
            continue

        order = ''.join([str(elem) for elem in ordernr])

        c = con.cursor()
        c.execute("INSERT INTO orders (order, orderstatus) VALUES (?, ?)", (order, 0))


    def pos1but(self):
        
        match self.pos1col:
            case "Black":
                self.pos1col = "Red"
            case "Red":
                self.pos1col = "Green"
            case "Green":
                self.pos1col = "Blue"
            case "Blue":
                self.pos1col = "Yellow"
            case "Yellow":
                self.pos1col = "Black"
        
    def pos2but(self):
        match self.pos2col:
            case "Black":
                self.pos2col = "Red"
            case "Red":
                self.pos2col = "Green"
            case "Green":
                self.pos2col = "Blue"
            case "Blue":
                self.pos2col = "Yellow"
            case "Yellow":
                self.pos2col = "Black"

    def pos3but(self):
        match self.pos3col:
            case "Black":
                self.pos3col = "Red"
            case "Red":
                self.pos3col = "Green"
            case "Green":
                self.pos3col = "Blue"
            case "Blue":
                self.pos3col = "Yellow"
            case "Yellow":
                self.pos3col = "Black"

    def pos4but(self):
        match self.pos4col:
            case "Black":
                self.pos4col = "Red"
            case "Red":
                self.pos4col = "Green"
            case "Green":
                self.pos4col = "Blue"
            case "Blue":
                self.pos4col = "Yellow"
            case "Yellow":
                self.pos4col = "Black"

    def pos5but(self):
        match self.pos5col:
            case "Black":
                self.pos5col = "Red"
            case "Red":
                self.pos5col = "Green"
            case "Green":
                self.pos5col = "Blue"
            case "Blue":
                self.pos5col = "Yellow"
            case "Yellow":
                self.pos5col = "Black"

    def pos6but(self):
        match self.pos6col:
            case "Black":
                self.pos6col = "Red"
            case "Red":
                self.pos6col = "Green"
            case "Green":
                self.pos6col = "Blue"
            case "Blue":
                self.pos6col = "Yellow"
            case "Yellow":
                self.pos6col = "Black"

    def pos7but(self):
        match self.pos7col:
            case "Black":
                self.pos7col = "Red"
            case "Red":
                self.pos7col = "Green"
            case "Green":
                self.pos7col = "Blue"
            case "Blue":
                self.pos7col = "Yellow"
            case "Yellow":
                self.pos7col = "Black"

    def pos8but(self):
        match self.pos8col:
            case "Black":
                self.pos8col = "Red"
            case "Red":
                self.pos8col = "Green"
            case "Green":
                self.pos8col = "Blue"
            case "Blue":
                self.pos8col = "Yellow"
            case "Yellow":
                self.pos8col = "Black"

    def pos9but(self):
        match self.pos9col:
            case "Black":
                self.pos9col = "Red"
            case "Red":
                self.pos9col = "Green"
            case "Green":
                self.pos9col = "Blue"
            case "Blue":
                self.pos9col = "Yellow"
            case "Yellow":
                self.pos9col = "Black"

    def pos10but(self):
        match self.pos10col:
            case "Black":
                self.pos10col = "Red"
            case "Red":
                self.pos10col = "Green"
            case "Green":
                self.pos10col = "Blue"
            case "Blue":
                self.pos10col = "Yellow"
            case "Yellow":
                self.pos10col = "Black"

    def pos11but(self):
        match self.pos11col:
            case "Black":
                self.pos11col = "Red"
            case "Red":
                self.pos11col = "Green"
            case "Green":
                self.pos11col = "Blue"
            case "Blue":
                self.pos11col = "Yellow"
            case "Yellow":
                self.pos11col = "Black"

    def pos12but(self):
        match self.pos12col:
            case "Black":
                self.pos12col = "Red"
            case "Red":
                self.pos12col = "Green"
            case "Green":
                self.pos12col = "Blue"
            case "Blue":
                self.pos12col = "Yellow"
            case "Yellow":
                self.pos12col = "Black"

    def pos13but(self):
        match self.pos13col:
            case "Black":
                self.pos13col = "Red"
            case "Red":
                self.pos13col = "Green"
            case "Green":
                self.pos13col = "Blue"
            case "Blue":
                self.pos13col = "Yellow"
            case "Yellow":
                self.pos13col = "Black"

    def pos14but(self):
        match self.pos14col:
            case "Black":
                self.pos14col = "Red"
            case "Red":
                self.pos14col = "Green"
            case "Green":
                self.pos14col = "Blue"
            case "Blue":
                self.pos14col = "Yellow"
            case "Yellow":
                self.pos14col = "Black"

    def pos15but(self):
        match self.pos15col:
            case "Black":
                self.pos15col = "Red"
            case "Red":
                self.pos15col = "Green"
            case "Green":
                self.pos15col = "Blue"
            case "Blue":
                self.pos15col = "Yellow"
            case "Yellow":
                self.pos15col = "Black"

    def pos16but(self):
        match self.pos16col:
            case "Black":
                self.pos16col = "Red"
            case "Red":
                self.pos16col = "Green"
            case "Green":
                self.pos16col = "Blue"
            case "Blue":
                self.pos16col = "Yellow"
            case "Yellow":
                self.pos16col = "Black"

root=tk.Tk()

prg = graphicDobot()
prg.master.title("Dobot Builder")
prg.mainloop()