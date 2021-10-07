import sqlite3
import Tkinter as tk

con = sqlite3.connect('Data.db')
print("Data being stored")

try:
    con.execute("""CREATE TABLE current
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order STRING,
    orderstatus INTEGER""")
except Exception:
    print("Table already exists")

class graphicDobot(Tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)

        ButtHeight = 50
        Buttwidth = 50

        self.pos1col = "Black"
        pos1 = tk.Button(self, bg = self.pos1col, command = , Height = ButtHeight, Width = Buttwidth)

        self.pos2col = "Black"
        pos2 = tk.Button(self, bg = self.pos2col, command = , Height = ButtHeight, Width = Buttwidth)

        self.pos3col = "Black"
        pos3 = tk.Button(self, bg = self.pos3col, command = , Height = ButtHeight, Width = Buttwidth)

        self.pos4col = "Black"
        pos4 = tk.Button(self, bg = self.pos4col, command = , Height = ButtHeight, Width = Buttwidth)

        self.pos5col = "Black"
        pos5 = tk.Button(self, bg = self.pos5col, command = , Height = ButtHeight, Width = Buttwidth)

        self.pos6col = "Black"
        pos2 = tk.Button(self, bg = self.pos6col, command = , Height = ButtHeight, Width = Buttwidth)

        self.pos7col = "Black"
        pos7 = tk.Button(self, bg = self.pos7col, command = , Height = ButtHeight, Width = Buttwidth)

        self.pos8col = "Black"
        pos8 = tk.Button(self, bg = self.pos8col, command = , Height = ButtHeight, Width = Buttwidth)

        self.pos9col = "Black"
        pos9 = tk.Button(self, bg = self.pos9col, command = , Height = ButtHeight, Width = Buttwidth)

        self.pos10col = "Black"
        pos10 = tk.Button(self, bg = self.pos10col, command = , Height = ButtHeight, Width = Buttwidth)

        self.pos11col = "Black"
        pos11 = tk.Button(self, bg = self.pos11col, command = , Height = ButtHeight, Width = Buttwidth)

        self.pos12col = "Black"
        pos12 = tk.Button(self, bg = self.pos12col, command = , Height = ButtHeight, Width = Buttwidth)

        self.pos13col = "Black"
        pos13 = tk.Button(self, bg = self.pos13col, command = , Height = ButtHeight, Width = Buttwidth)

        self.pos14col = "Black"
        pos14 = tk.Button(self, bg = self.pos14col, command = , Height = ButtHeight, Width = Buttwidth)

        self.pos15col = "Black"
        pos15 = tk.Button(self, bg = self.pos15col, command = , Height = ButtHeight, Width = Buttwidth)

        self.pos16col = "Black"
        pos16 = tk.Button(self, bg = self.pos16col, command = , Height = ButtHeight, Width = Buttwidth)

    def FinishOrder(self):
        UIColors = [self.pos1col,self.pos2col,self.pos3col,self.pos4col,self.pos5col,self.pos6col,self.pos7col,self.pos8col,self.pos9col,self.pos10col,self.pos11col,self.pos12col,self.pos13col,self.pos14col,self.pos15col,self.pos16col]
        
        ordernr = []

        for i in UIColors:
            if i == "Black":
                ordernr.append("0")
            elif i == "Red":
                ordernr.append("1")
            elif i == "Green":
                ordernr.append("2")
            elif i == "Blue":
                ordernr.append("3")
            elif i == "Yellow":
                ordernr.append("4")
        
        order = ''.join([str(elem) for elem in ordernr])


        

        

