

import pymysql

from prettytable import PrettyTable, from_db_cursor

conn = pymysql.connect(host = "localhost", user="root", password="", database = "playersdb")

cursor = conn.cursor()
cursor.execute("select * from players")

prtyTbl = from_db_cursor(cursor)

conn.close()
prtyTbl.align['playername'] = "l"
prtyTbl.align['sport'] = "l"
prtyTbl.align['achievement'] = "r"

print(prtyTbl)
