import sqlite3

connection = sqlite3.connect('customers.db')

customer_list = [(1998, "Anivaldo Soares", "Plumber"),
                 (2002, "Gerald Ferraz", "Journalist"),
                 (2002, "Ana da Silva", "Journalist"),
                 (2005, "Renato Tavares", "Butcher"),
                 (1999, "Maria Rogeria", "Economist")
                 ]

connection.close()