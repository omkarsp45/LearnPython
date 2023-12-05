import sqlite3 

connection = sqlite3.connect('customer.db')

cursor = connection.cursor()

# Update Records
cursor.execute("""UPDATE Customers SET first_name= 'Omkar' WHERE email LIKE 'omya%'
               """)

connection.commit()

# Fetch And Print
cursor.execute("SELECT * FROM Customers")
items = cursor.fetchall()
for item in items:
    print(str(item[0]) + " " + str(item[1]) + " | " + str(item[2]))

connection.commit()

cursor.close()