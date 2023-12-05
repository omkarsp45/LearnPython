import sqlite3

connection = sqlite3.connect('customer.db')

cursor = connection.cursor()

cursor.execute('SELECT rowid,* FROM Customers ORDER BY rowid DESC LIMIT 3')

items = cursor.fetchall()

for item in items:
    print(str(item[0])+" "+item[1]+" "+item[2]+" "+item[3])

connection.commit()

cursor.close()
