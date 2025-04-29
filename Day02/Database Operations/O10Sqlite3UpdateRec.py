
import sqlite3

conn = sqlite3.connect(database="playersDB.sqlite3")


cursor = conn.cursor()

cursor.execute("update players set playername = 'Pusarla Venkata Sindhu' where playerid = 'PL505'")

conn.commit()
conn.close()

