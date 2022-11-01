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
cursor.execute('select * from job_type where type=:c', {"c": "Communication"})
job_type_search = cursor.fetchall()

print("\n")
print(job_type_search)

# note that it doesn't alter the database itself
for i in journalist_search:
    new_line =[job_type_search[0][0] if value == "Journalist" else value for value in i]
    print(new_line)

connection.close()
