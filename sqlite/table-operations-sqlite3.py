import sqlite3

connection = sqlite3.connect('customers.db')
cursor = connection.cursor()

# read
for row in cursor.execute('select * from customers'):
    print(row)

connection.close()
