import sqlite3


def criarTabelaAno():
    try:
        sqliteConnection = sqlite3.connect('imobiliaria.db')
        cursor = sqliteConnection.cursor()
        print('Conexão ativa')

        sql_create = """CREATE TABLE anos(
                    ano INTEGER UNIQUE NOT NULL,
                    PRIMARY KEY(ano AUTOINCREMENT));"""

        cursor.execute(sql_create)
        sqliteConnection.commit()
        print('Tabela de ANOS criada')
    except sqlite3.Error as error:
        print('Tabela não foi criada: ', error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('Conexão fechada')


def dropTabelaAnos():
    try:
        sqliteConnection = sqlite3.connect('imobiliaria.db')
        cursor = sqliteConnection.cursor()
        print('Conexão ativa')

        sql_drop = """drop table anos"""
        cursor.execute(sql_drop)
        sqliteConnection.commit()
        print('Tabela Excluída')

    except sqlite3.Error as error:
        print('Erro: ', error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('Conexão fechada com o banco de dados')
