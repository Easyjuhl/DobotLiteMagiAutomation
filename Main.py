import sqlite3

con = sqlite3.connect('Data.db')
print("Data being stored")

try:
    con.execute("""CREATE TABLE current
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order STRING""")
except Exception:
    print("Table already exists")

