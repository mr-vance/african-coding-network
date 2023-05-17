import mysql.connector

Connection = mysql.connector.connect(
    host="db4free.net",
    user="mr_vance",
    password="ax123456ax",
    database="mr_vance_db"
)

Cursor = Connection.cursor()
Cursor.execute("SELECT * FROM friends WHERE gender='Male'")
Results = Cursor.fetchall()

for Row in Results:
    print(Row)

Connection.close()