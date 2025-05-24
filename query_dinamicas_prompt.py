import ClassConnectDb as connect
import ClassObjetos as Pessoa
import ClassObjetos as Marca
import ClassObjetos as Veiculo

db = connect.ClassConnectDb("./meu_banco.db")
db.connect()
#prompt add pessoa, veiculo e marca opção 1, 2 e 3
def add_pessoa():
    # Garante que CPF seja um número inteiro
    while True:
        try:
            cpf = int(input("Digite o CPF da pessoa (somente números): "))
            break
        except ValueError:
            print("Erro: CPF deve conter apenas números. Tente novamente.")
    
    nome = input("Digite o nome da pessoa: ")
    
    # Obtém data de nascimento e converte para formato YYYY-MM-DD para SQLite
    while True:
        data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")
        try:
            # Converte de DD/MM/AAAA para YYYY-MM-DD (formato SQLite)
            partes = data_nascimento.split('/')
            if len(partes) == 3 and len(partes[0]) == 2 and len(partes[1]) == 2 and len(partes[2]) == 4:
                data_formatada = f"{partes[2]}-{partes[1]}-{partes[0]}"
                break
            else:
                print("Formato de data inválido. Use DD/MM/AAAA.")
        except:
            print("Formato de data inválido. Use DD/MM/AAAA.")
    
    # Tratamento robusto para a entrada de óculos
    while True:
        resp_oculos = input("A pessoa usa óculos? (s/n): ").lower()
        if resp_oculos in ['s', 'n']:
            usa_oculos = (resp_oculos == 's')
            break
        else:
            print("Entrada inválida! Digite 's' para sim ou 'n' para não.")
    
    # Cria o objeto pessoa com os dados validados
    nova_pessoa = Pessoa.Pessoa(cpf, nome, data_formatada, usa_oculos)
    
    # Adiciona a nova pessoa ao banco de dados
    db.cursor.execute("INSERT INTO Pessoa (cpf, nome, nascimento, oculos) VALUES (?, ?, ?, ?)", 
                      (nova_pessoa.cpf, nova_pessoa.nome, nova_pessoa.data_nascimento, nova_pessoa.usa_oculos))
    db.conexao.commit()
    print("Pessoa adicionada com sucesso!")

def add_marca():
    # Garante que o ID da marca seja um número inteiro
    while True:
        try:
            id_marca = int(input("Digite o ID da marca (somente números): "))
            break
        except ValueError:
            print("Erro: ID deve conter apenas números. Tente novamente.")
    
    nome = input("Digite o nome da marca: ")
    
    nova_marca = Marca.Marca(id_marca, nome)
    
    # Garantir que a sigla tenha exatamente 2 caracteres
    sigla = nova_marca.sigla
    if len(sigla) < 2:
        # Se a sigla tiver menos de 2 caracteres, preenche com X até ter 2
        sigla = sigla.ljust(2, 'X')
    elif len(sigla) > 2:
        # Se a sigla tiver mais de 2 caracteres, corta para os 2 primeiros
        sigla = sigla[:2]
    
    # Adiciona a nova marca ao banco de dados
    db.cursor.execute("INSERT INTO Marca (id, nome, sigla) VALUES (?, ?, ?)", 
                      (id_marca, nova_marca.nome, sigla))
    db.conexao.commit()
    print("Marca adicionada com sucesso!")

def add_veiculo():
    # Validação da placa (deve ter exatamente 7 caracteres)
    while True:
        placa = input("Digite a placa do veículo (7 caracteres): ").upper()
        if len(placa) == 7:
            break
        else:
            print("Erro: A placa deve ter exatamente 7 caracteres. Tente novamente.")
    
    # Validação do ano (deve ser um número inteiro)
    while True:
        try:
            ano = int(input("Digite o ano do veículo: "))
            break
        except ValueError:
            print("Erro: O ano deve ser um número inteiro. Tente novamente.")
    
    cor = input("Digite a cor do veículo: ")
    
    # Validação do CPF do proprietário (deve ser um número inteiro)
    while True:
        try:
            proprietario = int(input("Digite o CPF do proprietário (somente números): "))
            break
        except ValueError:
            print("Erro: CPF deve conter apenas números. Tente novamente.")
    
    # Validação do ID da marca (deve ser um número inteiro)
    while True:
        try:
            marca = int(input("Digite o ID da marca: "))
            break
        except ValueError:
            print("Erro: O ID da marca deve conter apenas números. Tente novamente.")

    while True:
        try:
            motor = int(input("Digite o motor do veículo: "))
            break
        except ValueError:
            print("Erro: O motor deve conter apenas números. Tente novamente.")
    
    novo_veiculo = Veiculo.Veiculo(placa, ano, cor, motor, proprietario, marca)
    
    # Adiciona o novo veículo ao banco de dados
    db.cursor.execute("INSERT INTO Veiculo (placa, ano, cor,motor, proprietario, marca) VALUES (?,?, ?, ?, ?, ?)", 
                      (novo_veiculo.placa, novo_veiculo.ano, novo_veiculo.cor, novo_veiculo.motor ,novo_veiculo.proprietario, novo_veiculo.marca))
    db.conexao.commit()
    print("Veículo adicionado com sucesso!")

def main():
    while True:
        print("Escolha uma opção:")
        print("1. Adicionar Pessoa")
        print("2. Adicionar Marca")
        print("3. Adicionar Veículo")
        print("4. Sair")
        
        opcao = input("Opção: ")
        
        if opcao == '1':
            add_pessoa()
        elif opcao == '2':
            add_marca()
        elif opcao == '3':
            add_veiculo()
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")
    
    db.close()

if __name__ == "__main__":
    main()
