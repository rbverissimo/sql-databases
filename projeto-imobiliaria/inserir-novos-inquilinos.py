import sqlite3


def inserirNovosInquilinos(listaDeInquilinos):
    try:
        sqlite_connection = sqlite3.connect('imobiliaria.db')
        cursor = sqlite_connection.cursor()
        print('Conectado ao banco de dados')
        sql_query = """insert into inquilinos(id, nome) values(?, ?);"""
        cursor.executemany(sql_query, listaDeInquilinos)
        sqlite_connection.commit()
        print(cursor.rowcount, 'linhas afetadas')
        cursor.close()


    except sqlite3.Error as error:
        print('Falha ao inserir várias colunas', error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print('Conexão com o banco de dados fechada')
