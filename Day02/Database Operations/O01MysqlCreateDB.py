
import pymysql

conn = pymysql.connect(host = "localhost", user="root", password="")

cursor = conn.cursor()

query = "create database playersdb"

cursor.execute(query)

conn.commit()

conn.close()
