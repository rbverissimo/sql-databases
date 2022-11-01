import sqlite3

connection = sqlite3.connect('customers.db')
cursor = connection.cursor()

# read
for row in cursor.execute('select * from customers'):
    print(row)


print("\n")

# reading specific rows
cursor.execute('select * from customers where occupation=:c', {"c": "Journalist"})
journalist_search = cursor.fetchall()
print(journalist_search)

connection.close()
