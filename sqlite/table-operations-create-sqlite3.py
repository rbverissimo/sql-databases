import sqlite3

connection = sqlite3.connect('customers.db')
cursor = connection.cursor()

# create a new table in customers db
cursor.execute('create table products (name_product text, product_id text)')
# inserting a single piece of data
cursor.execute("insert into products values (?,?)", ("Cooking Lessons", "0789"))

connection.commit()

connection.close()
