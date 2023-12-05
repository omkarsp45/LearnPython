import sqlite3

connection = sqlite3.connect('customer.db')
cursor = connection.cursor()

# Deletes Table From Database
cursor.execute("DROP TABLE Customers")

connection.commit()

print(cursor.fetchall())

cursor.close()