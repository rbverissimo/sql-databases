import sqlite3


def buscarTodosOsMeses():
    try:
        sqliteConnection = sqlite3.connect('imobiliaria.db')
        cursor = sqliteConnection.cursor()
        print('Conectado ao banco de dados')

        sql_select = """select * from meses"""
        cursor.execute(sql_select)
        resultado = cursor.fetchall()
        print('Total de registros: ', len(resultado))

        for r in resultado:
            print('Id:', r[0])
            print('Mês: ', r[1])
            print('\n')

        cursor.close()
    except sqlite3.Error as error:
        print('Leitura não realizada: ', error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('Conexão fechada')


def inserirNovosMeses(listaDeMeses):
    try:
        sqlite_connection = sqlite3.connect('imobiliaria.db')
        cursor = sqlite_connection.cursor()
        print('Conectado ao banco de dados')
        sql_query = """insert into meses(id, mes) values(?, ?);"""
        cursor.executemany(sql_query, listaDeMeses)
        sqlite_connection.commit()
        print(cursor.rowcount, 'linhas afetadas')
        cursor.close()


    except sqlite3.Error as error:
        print('Falha ao inserir várias colunas', error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print('Conexão com o banco de dados fechada')
