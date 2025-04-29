
import sqlite3

conn = sqlite3.connect(database="playersDB.sqlite3")

conn.commit()

conn.close()
