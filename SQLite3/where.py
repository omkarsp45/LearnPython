import sqlite3

connection = sqlite3.connect('customer.db')

cursor = connection.cursor()

# cursor.execute('SELECT * FROM Customers WHERE last_name = "Patil"')
# -----------OR------------- #
# We Can also use logical operators for finding data which has real/integral type of data.
cursor.execute('SELECT * FROM Customers WHERE last_name LIKE "%le"')

items = cursor.fetchall()

for item in items:
    print(item[0])

connection.commit()

cursor.close()
