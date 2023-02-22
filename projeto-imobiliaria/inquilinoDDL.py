import sqlite3


def alterarTabelaInquilinosAdicionandoColuna():
    try:
        sqlite_connection = sqlite3.connect('imobiliaria.db')
        cursor = sqlite_connection.cursor()
        print('Conexão ativa')

        sql_alter = """alter table inquilinos add aluguel integer"""
        cursor.execute(sql_alter)
        sqlite_connection.commit()
        print('Coluna de aluguel adicionada a inquilinos com sucesso')
        cursor.close()

    except sqlite3.Error as error:
        print('Alterar tabela inquilinos falhou', error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print('Conexão fechada')
