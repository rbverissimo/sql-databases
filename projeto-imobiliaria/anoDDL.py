import sqlite3

def criarTabelaAno():
    try:
        sqliteConnection = sqlite3.connect('imobiliaria.db')
        cursor = sqliteConnection.cursor()
        print('Conexão ativa')

        sql_create = """CREATE TABLE anos(
                    id INTEGER UNIQUE NOT NULL,
                    ano integer UNIQUE NOT NULL,
                    PRIMARY KEY(id AUTOINCREMENT));"""
        cursor.execute(sql_create)
        sqliteConnection.commit()
        print('Tabela de ANOS criada')
    except sqlite3.Error as error:
        print('Tabela não foi criada: ', error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('Conexão fechada')