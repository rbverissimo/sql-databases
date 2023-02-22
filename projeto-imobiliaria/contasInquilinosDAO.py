import sqlite3


def inserirNovoRegistrodeContasInquilinos(agua, luz, ano_id, mes_id, inq_id):
    try:
        sqlite_connection = sqlite3.connect('imobiliaria.db')
        cursor = sqlite_connection.cursor()
        print('Conexão com o banco de dados realizada')

        sql = """insert into contas_inquilinos (agua, luz, ano_id, mes_id, inq_id) values (?, ?, ?, ?, ?)"""
        data = (agua, luz, ano_id, mes_id, inq_id)
        cursor.execute(sql, data)
        sqlite_connection.commit()
        print('Entrada de dados feita com sucesso')

        cursor.close()

    except sqlite3.Error as error:
        print('Falha ao inserir registro em contas inquilinos', error)

    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print('Conexão com banco de dados fechada')


def inserirNovosRegistrosDeContasInquilinosPorLista(listaDeContas):
    try:
        sqlite_connection = sqlite3.connect('imobiliaria.db')
        cursor = sqlite_connection.cursor()
        print('Conexão com o banco de dados realizada')
        sql_insert = """insert into contas_inquilinos (agua, luz, ano_id, mes_id, inq_id) values (?, ?, ?, ?, ?)"""
        cursor.executemany(sql_insert, listaDeContas)
        sqlite_connection.commit()
        print(cursor.rowcount, ' Registros inseridos por lista em contas_inquilinos')
        cursor.close()
    except sqlite3.Error as error:
        print('Falha ao tentar inserir múltiplos registros por lista em contas_inquilinos: ', error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print('Conexão com o banco de dadso fechada')


def buscarTodasContasInquilinos():
    try:
        sqliteConnection = sqlite3.connect('imobiliaria.db')
        cursor = sqliteConnection.cursor()
        print('Conectado ao banco de dados')

        sql_select = """select * from contas_inquilinos"""
        cursor.execute(sql_select)
        resultado = cursor.fetchall()
        print('Total de registros: ', len(resultado))

        for r in resultado:
            print('Inquilino:', r[4])
            print('Água: ', r[0])
            print('Luz:', r[1])
            print('Mês: ', r[3], ' Ano: ', r[2])

        cursor.close()
    except sqlite3.Error as error:
        print('Leitura da tabela contas_inquilinos não realizada: ', error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('Conexão fechada')
