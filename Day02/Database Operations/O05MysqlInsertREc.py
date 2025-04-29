
import pymysql

conn = pymysql.connect(host = "localhost", user="root", password="", database = "playersdb")

cursor = conn.cursor()

FL = open("records.txt", "r")
for query in FL.readlines():
    print(query)
    cursor.execute(query)

conn.commit()

conn.close()
FL.close()