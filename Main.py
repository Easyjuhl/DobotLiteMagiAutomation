import sqlite3
import Tkinter as tk

con = sqlite3.connect('Data.db')
print("Data being stored")

try:
    con.execute("""CREATE TABLE current
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order STRING""")
except Exception:
    print("Table already exists")

class graphicDobot(Tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)

        ButtHeight = 50
        Buttwidth = 50

        pos1col = "Black"
        pos1 = tk.Button(self, bg = pos1col, command = , Height = ButtHeight, Width = Buttwidth)
        
        pos2col = "Black"
        pos2 = tk.Button(self, bg = pos2col, command = , Height = ButtHeight, Width = Buttwidth)

        pos3col = "Black"
        pos3 = tk.Button(self, bg = pos3col, command = , Height = ButtHeight, Width = Buttwidth)

        pos4col = "Black"
        pos4 = tk.Button(self, bg = pos4col, command = , Height = ButtHeight, Width = Buttwidth)

    def FinishOrder(self):
        Order = ''
        OrderInList=[]

        

