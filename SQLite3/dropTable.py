import sqlite3

connection = sqlite3.connect('customer.db')
cursor = connection.cursor()

cursor.execute("DROP TABLE Customers")

connection.commit()

print(cursor.fetchall())

cursor.close()