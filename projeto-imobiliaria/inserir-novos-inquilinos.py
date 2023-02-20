import sqlite3

try:
    sqliteConn = sqlite3.connect('imobiliaria.db')
    cursor = sqliteConn.cursor()
    print('Conexão com o banco de dados realizada')

    sql = """insert into inquilinos (nome) values (?)"""
    data = ('Agmar')
    cursor.execute(sql, data)
    sqliteConn.commit()
    print('Entrada de dados feita com sucesso')

    cursor.close()

except sqlite3.Error as error:
    print('Failed to insert', error)
finally:
    if sqliteConn:
        sqliteConn.close()
        print('Conexão com banco de dados fechada')

