import sqlite3

def criarTabelaMes():
    try:
        sqliteConnection = sqlite3.connect('imobiliaria.db')
        cursor = sqliteConnection.cursor()
        print('Conexão ativa')

        sql_create = """CREATE TABLE meses(
                    id INTEGER UNIQUE NOT NULL,
                    mes text UNIQUE NOT NULL,
                    PRIMARY KEY(id AUTOINCREMENT));"""
        cursor.execute(sql_create)
        sqliteConnection.commit()
        print('Tabela de meses criada')
    except sqlite3.Error as error:
        print('Tabela não foi criada: ', error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('Conexão fechada')