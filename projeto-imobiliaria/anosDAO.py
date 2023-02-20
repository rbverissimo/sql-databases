import sqlite3

def inserirNovoAno(id, ano):
    try:
        sqlite_connection = sqlite3.connect('imobiliaria.db')
        cursor = sqlite_connection.cursor()
        print('Conexão com o banco de dados realizada')

        sql = """insert into anos (id, ano) values (?, ?)"""
        data = (id, ano)
        cursor.execute(sql, data)
        sqlite_connection.commit()
        print('Entrada de dados feita com sucesso')

        cursor.close()

    except sqlite3.Error as error:
        print('Falha ao inserir', error)

    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print('Conexão com banco de dados fechada')