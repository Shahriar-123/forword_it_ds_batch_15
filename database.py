import mysql

db = mysql.connector.connect(
    host="localhost", user="root", password="",
)
print(db)