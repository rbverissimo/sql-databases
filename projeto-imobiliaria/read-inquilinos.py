import sqlite3


def buscarTodosInquilinos():
    try:
        sqliteConnection = sqlite3.connect('imobiliaria.db')
        cursor = sqliteConnection.cursor()
        print('Conectado ao banco de dados')

        sql_select = """select * from inquilinos"""
        cursor.execute(sql_select)
        resultado = cursor.fetchall()
        print('Total de registros: ', len(resultado))

        for r in resultado:
            print('Id:', r[0])
            print('Nome: ', r[1])
            print('\n')

        cursor.close()
    except sqlite3.Error as error:
        print('Leitura não realizada: ', error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('Conexão fechada')

buscarTodosInquilinos()