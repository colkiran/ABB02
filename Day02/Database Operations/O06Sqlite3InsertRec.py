
import sqlite3

conn = sqlite3.connect(database="playersDB.sqlite3")

cursor = conn.cursor()

FL = open("records.txt", "r")
for query in FL.readlines():
    print(query)
    cursor.execute(query)

conn.commit()

conn.close()
FL.close()