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
            print('Aluguel', r[2])
            print('\n')

        cursor.close()
    except sqlite3.Error as error:
        print('Leitura não realizada: ', error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('Conexão fechada')


def buscarInquilinosPorId(id):
    try:
        sqliteConnection = sqlite3.connect('imobiliaria.db')
        cursor = sqliteConnection.cursor()
        print('Conectado ao banco de dados')

        sql_select_id = """select * from inquilinos where id = ?"""
        cursor.execute(sql_select_id, (id,))
        resultado = cursor.fetchall()
        print('Id buscado:', id)

        for r in resultado:
            print('Nome', r[1])
            print('Aluguel', r[2])

        cursor.close()
    except sqlite3.Error as error:
        print('Leitura não realizada: ', error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('Conexão fechada')


def inserirNovoInquilino(id, nome):
    try:
        sqlite_connection = sqlite3.connect('imobiliaria.db')
        cursor = sqlite_connection.cursor()
        print('Conexão com o banco de dados realizada')

        sql = """insert into inquilinos (id, nome) values (?, ?)"""
        data = (id, nome)
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


def atualizarAluguelInquilinoPorId(id, aluguel):
    try:
        sqlite_connection = sqlite3.connect('imobiliaria.db')
        cursor = sqlite_connection.cursor()
        print('Conectado ao banco de dados')

        sql_update = """update inquilinos set aluguel = ? where id = ?"""
        data = (aluguel, id)
        cursor.execute(sql_update, data)
        sqlite_connection.commit()
        print("Registro atualizado com sucesso")
        cursor.close()
    except sqlite3.Error as error:
        print('Atualização de inquilino falhou: ', error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print('Conexão finalizada')


def atualizarAluguelInquilinosPorLista(listaDeInquilinos):
    try:
        sqlite_connection = sqlite3.connect('imobiliaria.db')
        cursor = sqlite_connection.cursor()
        print('Conectado ao banco de dados')

        sql_update_multiplo = """update inquilinos set aluguel = ? where id = ?"""
        cursor.executemany(sql_update_multiplo, listaDeInquilinos)
        sqlite_connection.commit()
        print(cursor.rowcount, ' registros alterados com sucesso')
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print('Falha ao tentar alterar múltiplos registros na tabela inquilinos: ', error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print('Conexao com banco de dados fechada')
