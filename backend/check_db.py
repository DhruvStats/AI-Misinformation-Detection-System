import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

rows = cursor.execute("SELECT * FROM predictions").fetchall()

for row in rows:
    print(row)

conn.close()