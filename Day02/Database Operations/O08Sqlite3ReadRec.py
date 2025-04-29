
import sqlite3
from prettytable import PrettyTable, from_db_cursor

conn = sqlite3.connect(database="playersDB.sqlite3")

cursor = conn.cursor()
cursor.execute("select * from players")

prtyTbl = from_db_cursor(cursor)

conn.close()
prtyTbl.align['playername'] = "l"
prtyTbl.align['sport'] = "l"
prtyTbl.align['achievement'] = "r"

print(prtyTbl)
