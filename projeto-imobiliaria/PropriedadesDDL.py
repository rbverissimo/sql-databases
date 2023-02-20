import sqlite3


def dropTablePropriedades():
    try:
        sqliteConnection = sqlite3.connect('imobiliaria.db')
        cursor = sqliteConnection.cursor()
        print('Conexão ativa')

        sql_drop = """drop table propriedades"""
        cursor.execute(sql_drop)
        sqliteConnection.commit()
        print('Tabela Excluída')

    except sqlite3.Error as error:
        print('Erro: ', error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('Conexão fechada com o banco de dados')

def dropTablePropriedadesOld():
    try:
        sqliteConnection = sqlite3.connect('imobiliaria.db')
        cursor = sqliteConnection.cursor()
        print('Conexão ativa')

        sql_drop = """drop table propriedades_old"""
        cursor.execute(sql_drop)
        sqliteConnection.commit()
        print('Tabela Excluída')

    except sqlite3.Error as error:
        print('Erro: ', error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('Conexão fechada com o banco de dados')


def createTablePropriedades():
    try:
        sqliteConnection = sqlite3.connect('imobiliaria.db')
        cursor = sqliteConnection.cursor()
        print('Conexão ativa')

        sql_create = """CREATE TABLE propriedades(
                    id integer not null unique,
                    nome text not null,
                    endereco text not null,
                    PRIMARY KEY(id autoincrement));"""

        cursor.execute(sql_create)
        sqliteConnection.commit()
        print('Tabela propriedades criada')
        cursor.close()

    except sqlite3.Error as error:
        print('Erro ao criar a tabela: ', error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('Conexão fechada')






