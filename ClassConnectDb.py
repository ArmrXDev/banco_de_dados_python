import sqlite3

class ClassConnectDb:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conexao = None
        self.cursor = None

    def connect(self):
        try:
            self.conexao = sqlite3.connect(self.db_name)
            self.cursor = self.conexao.cursor()
            print("Conexão com o banco de dados estabelecida.")
        except sqlite3.Error as erro:
            print("Erro ao conectar ao banco de dados:", erro)

    def close(self):
        if self.conexao:
            self.cursor.close()
            self.conexao.close()
            print("Conexão com o banco de dados fechada.")