import sqlite3

connection = sqlite3.connect('customer.db')
cursor = connection.cursor()

cursor.execute("DELETE from Customers WHERE rowid = 3")

connection.commit() 

cursor.execute("SELECT * FROM Customers")
items = cursor.fetchall()
for item in items:
    print(item[0]+" "+item[1])

# connection.commit()

cursor.close()