import sqlite3

# Connect to database file (if file not existed makes new file)
# connection = sqlite3.connect(':memory:') ->Dont make new file, uses memory temporary and disappers after its use
connection = sqlite3.connect('customer.db')  

# create cursor
cursor = connection.cursor() 

# create table 
# (""" """) ->DocString for multiple instructions
# sqlite3 has only 5 datatypes
cursor.execute("""CREATE TABLE Customers(
        first_name text,
        last_name text,
        email text                     
    )""")

# Datatypes:
# Null : nothing
# Integer : integral numbers
# Real : floatingPoint IEEE 8byte
# Text : string
# Blob : stored as it is(audio file , image file , etc)

# Commit
connection.commit()

# Close Connection(good prac)
connection.close()