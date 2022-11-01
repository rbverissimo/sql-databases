import sqlite3

connection = sqlite3.connect('customers.db')
cursor = connection.cursor()

# create a new table in customers db
cursor.execute('create table job_type (type text, job_id text)')
# inserting a single piece of data

job_type_list = [("Communication", "0001"),
                 ("Finance", "0002"),
                 ("Services", "0003")]

cursor.executemany("insert into job_type values (?,?)", job_type_list)

connection.commit()

connection.close()
