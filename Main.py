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