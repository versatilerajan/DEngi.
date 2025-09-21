import mysql.connector

# ✅ Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="###Rajan@123###",
    database="rajan_db"
)

db_cursor = mydb.cursor()

# ✅ Drop existing table and create new one with AUTO_INCREMENT ID
db_cursor.execute("DROP TABLE IF EXISTS student")
db_cursor.execute("""
    CREATE TABLE student (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        age INT,
        city VARCHAR(100)
    )
""")

# ✅ List of students (name, age, city)
students = [
    ("Rajan", 23, "Bangalore"),
    ("Shivani", 22, "Delhi"),
    ("Amit", 24, "Mumbai"),
    ("Priya", 21, "Chennai"),
    ("Arjun", 25, "Hyderabad"),
    ("Meera", 20, "Kolkata"),
    ("Karan", 26, "Pune"),
    ("Simran", 23, "Jaipur")
]

# ✅ Insert multiple rows
db_cursor.executemany(
    "INSERT INTO student (name, age, city) VALUES (%s, %s, %s)",
    students
)

# ✅ Commit changes
mydb.commit()

print(f"{db_cursor.rowcount} records inserted successfully.")

# ✅ Close connection
db_cursor.close()
mydb.close()
