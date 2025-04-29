

import sqlite3

conn = sqlite3.connect(database="playersDB.sqlite3")

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
