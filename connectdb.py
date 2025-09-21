import mysql.connector
# connect with root and make a databse
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="###Rajan@123###"
)

db_cursor = mydb.cursor()

db_cursor.execute("CREATE DATABASE IF NOT EXISTS rajan_db")
