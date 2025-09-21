import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="###Rajan@123###",
    database="rajan_db"
)

db_cursor = mydb.cursor()

# ✅ Create table if it does not exist
db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS student (
        id INT PRIMARY KEY,
        name VARCHAR(100),
        age INT,
        city VARCHAR(100)
    )
""")

# Insert data
db_cursor.execute(
    "INSERT INTO student (id, name, age, city) VALUES (%s, %s, %s, %s)",
    (1, 'Rajan', 23, 'Bangalore')
)

# ✅ Commit the transaction
mydb.commit()

print("Data Inserted Successfully")

# Close connection
db_cursor.close()
mydb.close()
