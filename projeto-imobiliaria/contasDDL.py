import sqlite3

def criarTabelaContas():
    try:
        sqliteConnection = sqlite3.connect('imobiliaria.db')
        cursor = sqliteConnection.cursor()
        print('Conexão ativa')

        sql_create = """CREATE TABLE contas(
                    agua integer not null,
                    luz integer not null,
                    ano_id integer,
                    mes_id integer,
                    prop_id integer,
                    FOREIGN KEY(ano_id) REFERENCES anos(id),
                    FOREIGN KEY(mes_id) REFERENCES meses(id),
                    FOREIGN KEY(prop_id) REFERENCES propriedades(id),
                    PRIMARY KEY(ano_id, mes_id, prop_id)
                    );"""

        cursor.execute(sql_create)
        sqliteConnection.commit()
        print('Tabela contas criada')
        cursor.close()

    except sqlite3.Error as error:
        print('Criar tabela contas falhou: ', error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print('Conexao com banco de dados fechada')
