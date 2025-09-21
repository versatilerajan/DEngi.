import mysql.connector

# ✅ Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="###Rajan@123###",
    database="rajan_db"
)

db_cursor = mydb.cursor()

# ========== DELETE EXAMPLES ==========

# 1. ✅ Delete by ID (most common)
print("1. Deleting student with ID = 5")
db_cursor.execute("DELETE FROM student WHERE id = %s", (5,))
print(f"Deleted {db_cursor.rowcount} record(s)")

# # 2. ✅ Delete by name
# print("\n2. Deleting student named 'Rajan'")
# db_cursor.execute("DELETE FROM student WHERE name = %s", ("Rajan",))
# print(f"Deleted {db_cursor.rowcount} record(s)")

# # 3. ✅ Delete by age condition
# print("\n3. Deleting students older than 24")
# db_cursor.execute("DELETE FROM student WHERE age > %s", (24,))
# print(f"Deleted {db_cursor.rowcount} record(s)")

# # 4. ✅ Delete by city
# print("\n4. Deleting students from 'Mumbai'")
# db_cursor.execute("DELETE FROM student WHERE city = %s", ("Mumbai",))
# print(f"Deleted {db_cursor.rowcount} record(s)")

# # 5. ✅ Delete with multiple conditions
# print("\n5. Deleting students from 'Delhi' who are 22 years old")
# db_cursor.execute("DELETE FROM student WHERE city = %s AND age = %s", ("Delhi", 22))
# print(f"Deleted {db_cursor.rowcount} record(s)")

# # 6. ✅ Delete multiple records by ID list
# print("\n6. Deleting students with IDs 2, 3, 7")
# ids_to_delete = (2, 3, 7)
# placeholders = ",".join(["%s"] * len(ids_to_delete))
# query = f"DELETE FROM student WHERE id IN ({placeholders})"
# db_cursor.execute(query, ids_to_delete)
# print(f"Deleted {db_cursor.rowcount} record(s)")

# # 7. ✅ Delete with age range
# print("\n7. Deleting students between age 20-22")
# db_cursor.execute("DELETE FROM student WHERE age BETWEEN %s AND %s", (20, 22))
# print(f"Deleted {db_cursor.rowcount} record(s)")

# # 8. ✅ Delete using LIKE pattern (partial match)
# print("\n8. Deleting students whose name starts with 'A'")
# db_cursor.execute("DELETE FROM student WHERE name LIKE %s", ("A%",))
# print(f"Deleted {db_cursor.rowcount} record(s)")


# ✅ Commit all changes
mydb.commit()

# ✅ Show remaining records
print("\n" + "="*50)
print("REMAINING RECORDS:")
db_cursor.execute("SELECT * FROM student")
results = db_cursor.fetchall()

if results:
    print("ID | Name     | Age | City")
    print("-" * 30)
    for row in results:
        print(f"{row[0]:2} | {row[1]:8} | {row[2]:3} | {row[3]}")
else:
    print("No records found in the table.")

# ✅ Close connection
db_cursor.close()
mydb.close()
