import sqlite3

def criarTabelaMes():
    try:
        sqliteConnection = sqlite3.connect('imobiliaria.db')
        cursor = sqliteConnection.cursor()
        print('Conexão ativa')

        sql_create = """CREATE TABLE contas(
                    agua integer not null,
                    luz integer not null)"""

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
