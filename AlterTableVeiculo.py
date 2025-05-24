import sqlite3 as conector

try:
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()

    comando = """ ALTER TABLE Veiculo 
    ADD motor REAL"""

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
