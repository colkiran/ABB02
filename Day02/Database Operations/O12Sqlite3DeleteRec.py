import sqlite3

conn = sqlite3.connect(database="playersDB.sqlite3")

cursor = conn.cursor()

cursor.execute("delete from players where playerid = 'PL444'")

conn.commit()

conn.close()


