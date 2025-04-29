


import pymysql

conn = pymysql.connect(host = "localhost", user="root", password="", database = "playersdb")

cursor = conn.cursor()

cursor.execute("update players set playername = 'Pusarla Venkata Sindhu' where playerid = 'PL505'")

conn.commit()
conn.close()

