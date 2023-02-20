import sqlite3


def inserirNovoInquilino(id, nome):
    try:
        sqliteConn = sqlite3.connect('imobiliaria.db')
        cursor = sqliteConn.cursor()
        print('Conexão com o banco de dados realizada')

        sql = """insert into inquilinos (id, nome) values (?, ?)"""
        data = (id, nome)
        cursor.execute(sql, data)
        sqliteConn.commit()
        print('Entrada de dados feita com sucesso')

        cursor.close()

    except sqlite3.Error as error:
        print('Falha ao inserir', error)
    finally:
        if sqliteConn:
            sqliteConn.close()
            print('Conexão com banco de dados fechada')


# nome = "Agmar"
# inserirNovoInquilino(1, nome)
inserirNovoInquilino(2, 'Branca')
