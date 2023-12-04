import sqlite3

connection = sqlite3.connect('customer.db')

cursor = connection.cursor()

# Insert One Data into database file
# cursor.execute("INSERT INTO Customers VALUES('Rahul', 'Patil', 'rahulsp3003@gmail.com')")

# Insert Multiple Values
many_customers = [
    ('Ramesh','Patil', 'omyapvt0405@gmail.com'),
    ('Suresh','Patil', 'suraj201@gmail.com'),
    ('Suresh','Bhosale', 'suraj201@gmail.com')
    ]

cursor.executemany("INSERT INTO Customers VALUES(?,?,?)", many_customers)

connection.commit()

connection.close()