import sqlite3

def criarTabelasContasInquilinos():
    try:
        sqliteConnection = sqlite3.connect('imobiliaria.db')
        cursor = sqliteConnection.cursor()
        print('Conexão ativa')

        sql_create = """CREATE TABLE contas_inquilinos(
                    agua integer not null,
                    luz integer not null,
                    ano_id integer,
                    mes_id integer,
                    inq_id integer,
                    FOREIGN KEY(ano_id) REFERENCES anos(ano),
                    FOREIGN KEY(mes_id) REFERENCES meses(id),
                    FOREIGN KEY(inq_id) REFERENCES inquilinos(id),
                    PRIMARY KEY(ano_id, mes_id, inq_id)
                    );"""

        cursor.execute(sql_create)
        sqliteConnection.commit()
        print('Tabela contas_inquilinos criada')
        cursor.close()

    except sqlite3.Error as error:
        print('Criar tabela contas_inquilinos falhou: ', error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('Conexao com banco de dados fechada')