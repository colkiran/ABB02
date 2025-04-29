
import pymysql

conn = pymysql.connect(host = "localhost", user="root", password="", database = "playersdb")

cursor = conn.cursor()

cursor.execute("delete from players where playerid = 'PL444'")

conn.commit()

conn.close()

