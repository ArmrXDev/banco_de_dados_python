import sqlite3

conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()
try:

    comando = """ INSERT INTO Pessoa (cpf, nome,nascimento,oculos)
        VALUES (1234567890, 'João da Silva', '1990-01-01', 1) """

    cursor.execute(comando)
    conexao.commit()

    print("Dados inseridos com sucesso!")

except sqlite3.Error as erro:
    print("Erro ao inserir dados:", erro)
finally:
    if conexao:
        cursor.close()
        conexao.close()
        print("Conexão com o banco de dados fechada.")
