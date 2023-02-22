import sqlite3

def joinContasComInquilinos():
    try:
        sqlite_connection = sqlite3.connect('imobiliaria.db')
        cursor = sqlite_connection.cursor()
        print('Conexão ativa com banco de dados')

        sql_join = """SELECT i.nome, i.aluguel, c.agua, c.luz, c.ano_id, c.mes_id 
                    FROM contas_inquilinos c 
                    INNER JOIN inquilinos i 
                    ON c.inq_id = i.id 
                    ORDER BY i.nome"""
        cursor.execute(sql_join)
        resultado = cursor.fetchall()

        for r in resultado:
            print(r)
        cursor.close()
    except sqlite3.Error as error:
        print('Join entre colunas contas_inquilinos e inquilinos falhou: ', error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print('Conexão fechada')