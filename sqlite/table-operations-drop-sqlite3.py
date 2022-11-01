import sqlite3

connection = sqlite3.connect('customers.db')
cursor = connection.cursor()
cursor.execute('drop table products')  # deletes the products table from the database
connection.commit()  # every execute must be committed
connection.close()