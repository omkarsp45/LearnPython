import sqlite3

connection = sqlite3.connect('customer.db')

cursor = connection.cursor()

# Query the database
cursor.execute("SELECT * FROM Customers")

# Fetch values
# print(cursor.fetchone())
# print(cursor.fetchmany(2))
print(cursor.fetchall())

connection.commit()

connection.close()