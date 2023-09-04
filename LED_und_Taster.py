import sqlite3

cursor = sqlite3.connect("LED und Taster.db")
conn = cursor.cursor()

conn.execute(open("setup.sql").read())
cursor.commit()



