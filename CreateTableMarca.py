import sqlite3 as conector

try:
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()

    comando = """ CREATE TABLE Marca (
        id INTEGER NOT NULL,
        nome TEXT NOT NULL,
        sigla CHARACTER(2) NOT NULL,
        PRIMARY KEY (id)
    );"""

    cursor.execute(comando)

    # efetua o commit para salvar as alterações

    conexao.commit()

    print("Tabela criada com sucesso!")

except conector.DatabaseError as err:
    print("Erro de banco de dados:", err)
finally:
    if conexao:
        cursor.close()
        conexao.close()
