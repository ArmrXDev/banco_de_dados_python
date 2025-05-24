import sqlite3 as conector

try:
    conexao = conector.connect("./meu_banco.db")
    cursor = conexao.cursor()

    comando = """ CREATE TABLE Veiculo (
        placa CHARACTER(7) NOT NULL,
        ano INTEGER NOT NULL,
        cor TEXT NOT NULL,
        proprietario INTEGER NOT NULL,
        marca INTEGER NOT NULL,
        PRIMARY KEY (placa),
        FOREIGN KEY (proprietario) REFERENCES Pessoa(cpf),
        FOREIGN KEY (marca) REFERENCES Marca(id)
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
