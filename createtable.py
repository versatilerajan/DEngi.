import mysql.connector
#Here we connect with databses (rajan_db) and create a table students
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="###Rajan@123###",
    database="rajan_db"
)

db_cursor = mydb.cursor()

db_cursor.execute("CREATE TABLE IF NOT EXISTS students (name VARCHAR(255), age INT(3), city VARCHAR(255))")

