import sqlite3

connection = sqlite3.connect('customers.db')
cursor = connection.cursor()  # this guy here is responsible to operate the database

cursor.execute('create table customers(year_joined integer, customer_name text, occupation text)')

customer_list = [(1998, "Anivaldo Soares", "Plumber"),
                 (2002, "Gerald Ferraz", "Journalist"),
                 (2002, "Ana da Silva", "Journalist"),
                 (2005, "Renato Tavares", "Butcher"),
                 (1999, "Maria Rogeria", "Economist")
                 ]

cursor.executemany('insert into customers values(?,?,?)', customer_list)

connection.close()