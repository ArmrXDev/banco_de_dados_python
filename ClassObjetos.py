class Pessoa:
    def __init__(self, cpf, nome, data_nascimento, usa_oculos):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.usa_oculos = usa_oculos

class Marca:
    def __init__(self, id_marca, nome):
        self.id_marca = id_marca
        self.nome = nome
        self.sigla = self.gerar_sigla(nome)

    def gerar_sigla(self, nome):
        # Gera uma sigla a partir do nome da marca
        partes = nome.split()
        sigla = ''.join([parte[0].upper() for parte in partes])
        return sigla[:2]
    
class Veiculo:
    def __init__(self, placa, ano, cor, motor ,proprietario, marca):
        self.placa = placa
        self.ano = ano
        self.cor = cor
        self.motor = motor
        self.proprietario = proprietario
        self.marca = marca