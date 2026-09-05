import sqlite3

conn = sqlite3.connect("pipeline.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM weather")
print("total rows:", cursor.fetchone())

cursor.execute("SELECT COUNT(DISTINCT time) FROM weather")
print("distinct timestamps:", cursor.fetchone())

cursor.execute("SELECT MIN(time), MAX(time) FROM weather")
print("time range:", cursor.fetchone())

conn.close()