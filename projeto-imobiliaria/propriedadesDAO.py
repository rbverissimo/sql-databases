import sqlite3


def buscarPropriedadePorId(id):
    try:
        sqliteConnection = sqlite3.connect('imobiliaria.db')
        cursor = sqliteConnection.cursor()
        print('Conectado ao banco de dados')

        sql_select_id = """select * from propriedades where id = ?"""
        cursor.execute(sql_select_id, (id,))
        resultado = cursor.fetchall()
        print('Id buscado:', id)

        for r in resultado:
            print('Nome', r[1])
            print('Endereço: ', r[2])

        cursor.close()
    except sqlite3.Error as error:
        print('Leitura não realizada: ', error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('Conexão fechada')


def buscarTodasPropriedades():
    try:
        sqliteConnection = sqlite3.connect('imobiliaria.db')
        cursor = sqliteConnection.cursor()
        print('Conectado ao banco de dados')

        sql_select = """select * from propriedades"""
        cursor.execute(sql_select)
        resultado = cursor.fetchall()
        print('Total de registros: ', len(resultado))

        for r in resultado:
            print('Id: ', r[0])
            print('Nome: ', r[1])
            print('Endereço', r[2])
            print('\n')

        cursor.close()

    except sqlite3.Error as error:
        print('Leitura não realizada', error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('Conexão fechada')


def inserirNovaPropriedade(id, nome, endereco):
    try:
        sqlite_connection = sqlite3.connect('imobiliaria.db')
        cursor = sqlite_connection.cursor()
        print('Conexão com o banco de dados realizada')

        sql = """insert into propriedades (id, nome, endereco) values (?, ?, ?)"""
        data = (id, nome, endereco)
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
