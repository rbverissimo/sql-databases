import sqlite3


def inserirNovosInquilinos(listaDeInquilinos):


    try:
        sqliteConnection = sqlite3.connect('imobiliaria.db')
        cursor = sqliteConnection.cursor()
        print('Conectado ao banco de dados')

        sql_query = """insert into inquilinos(nome) values(?)"""


    except sqlite3.Error as error:
        print('Falha ao inserir várias colunas')
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('Conexão com o banco de dados fechada')
