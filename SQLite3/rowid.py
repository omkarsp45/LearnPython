import sqlite3 

connection = sqlite3.connect('customer.db')

cursor = connection.cursor()

cursor.execute("SELECT rowid, * FROM Customers")

# print(cursor.fetchall()) 

items = cursor.fetchall()

for item in items:
    print(str(item[0]) + " " + str(item[1]) + " | " + str(item[2]))
    # print(str(item[0]) + " " + str(item[1]) + " | " + str(item[2]))

connection.commit()

cursor.close()