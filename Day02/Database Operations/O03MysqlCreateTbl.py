
import pymysql

conn = pymysql.connect(host = "localhost", user="root", password="", database = "playersdb")

cursor = conn.cursor()

query = """
create table players(
playerid varchar(7) PRIMARY KEY,
playername varchar(50) not null,
sport varchar(50) not null,
achievement varchar(50) not null
)
"""

cursor.execute(query)

conn.commit()

conn.close()
