import sqlite3


def buscarAnoPorId(ano):
    try:
        sqliteConnection = sqlite3.connect('imobiliaria.db')
        cursor = sqliteConnection.cursor()
        print('Conectado ao banco de dados')

        sql_select_id = """select * from anos where ano = ?"""
        cursor.execute(sql_select_id, (ano,))
        resultado = cursor.fetchall()
        print('Ano buscado:', ano)

        for r in resultado:
            print('Ano', ano[0], 'buscado com sucesso')

        cursor.close()
    except sqlite3.Error as error:
        print('Leitura não realizada: ', error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('Conexão fechada')


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


def deletarAnos(id):
    try:
        sqlite_connection = sqlite3.connect('imobiliaria.db')
        cursor = sqlite_connection.cursor()
        print('Conectado ao banco de dados')

        sql_delete = """DELETE from anos where id ?"""
        cursor.execute(sql_delete, (id,))
        sqlite_connection.commit()
        print('Ano deletado com sucesso')

        cursor.close()

    except sqlite3.Error as error:
        print('Falha ao deletar o ano: ', error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print('Conexão finalizada')
