from datetime import datetime

# HarvestLink - Ligando Produtores, Estabelecimentos e Caridade para Alimentar Vidas

# Variáveis globais para armazenar os dados dos produtores, estabelecimentos e instituições de caridade
produtores = []
estabelecimentos = []
instituicoes_caridade = []


# Função para cadastrar um produtor
def cadastrar_produtor():
    # Solicita informações do produtor ao usuário
    nome = input("Nome do produtor: ")

    while True:
        try:
            quantidade = float(input("Quantidade de alimentos excedentes: "))
            break
        except ValueError:
            print("Erro: valor inválido. Digite um número válido para a quantidade de alimentos excedentes.")

    tipo_alimento = input("Tipo de alimento: ")

    while True:
        try:
            data_validade = input("Data de validade (DD/MM/AAAA): ")
            data_validade = datetime.strptime(data_validade, "%d/%m/%Y").strftime("%d/%m/%Y")
            break
        except ValueError:
            print("Erro: formato de data inválido. Digite a data no formato DD/MM/AAAA.")

    localizacao = input("Localização: ")

    # Cria um dicionário com os dados do produtor e adiciona à lista de produtores
    produtor = {
        "nome": nome,
        "quantidade": quantidade,
        "tipo_alimento": tipo_alimento,
        "data_validade": data_validade,
        "localizacao": localizacao
    }

    produtores.append(produtor)
    print("Produtor cadastrado com sucesso!")


# Função para cadastrar um estabelecimento
def cadastrar_estabelecimento():
    # Solicita informações do estabelecimento ao usuário
    nome = input("Nome do estabelecimento: ")
    demanda = float(input("Demanda de alimentos: "))
    disponibilidade = input("Disponibilidade para receber alimentos (S/N): ")

    # Cria um dicionário com os dados do estabelecimento e adiciona à lista de estabelecimentos
    estabelecimento = {
        "nome": nome,
        "demanda": demanda,
        "disponibilidade": disponibilidade
    }

    estabelecimentos.append(estabelecimento)
    print("Estabelecimento cadastrado com sucesso!")


# Função para cadastrar uma instituição de caridade
def cadastrar_instituicao_caridade():
    # Solicita informações da instituição de caridade ao usuário
    nome = input("Nome da instituição de caridade: ")
    contato = input("Informações de contato: ")

    # Cria um dicionário com os dados da instituição de caridade e adiciona à lista de instituições de caridade
    instituicao = {
        "nome": nome,
        "contato": contato
    }

    instituicoes_caridade.append(instituicao)
    print("Instituição de caridade cadastrada com sucesso!")


# Função para buscar correspondências e facilitar a doação de alimentos
def buscar_correspondencias():
    # Solicita o tipo de alimento desejado ao usuário
    tipo_alimento = input("Informe o tipo de alimento desejado: ")

    # Lista para armazenar as correspondências encontradas
    correspondencias = []

    # Percorre a lista de produtores, estabelecimentos e instituições de caridade para identificar correspondências
    for produtor in produtores:
        if produtor["tipo_alimento"].lower() == tipo_alimento.lower() and produtor["quantidade"] > 0:
            for estabelecimento in estabelecimentos:
                if estabelecimento["disponibilidade"].lower() == "s" and estabelecimento["demanda"] > 0:
                    for instituicao in instituicoes_caridade:
                        correspondencias.append((produtor, estabelecimento, instituicao))

    # Verifica se foram encontradas correspondências e exibe os resultados
    if correspondencias:
        print("Correspondências encontradas:")
        for i, (produtor, estabelecimento, instituicao) in enumerate(correspondencias):
            print(f"Correspondência {i + 1}:")
            print("Produtor:", produtor["nome"])
            print("Quantidade de Excedentes:", produtor["quantidade"])
            print("Estabelecimento:", estabelecimento["nome"])
            print("Instituição de Caridade:", instituicao["nome"])
            print("--------------------------------------")
    else:
        print("Nenhuma correspondência encontrada.")


# Função principal do programa
def main():
    print("Bem-vindo ao HarvestLink!")

    while True:
        print("\nOpções:")
        print("1 - Cadastrar produtor")
        print("2 - Cadastrar estabelecimento")
        print("3 - Cadastrar instituição de caridade")
        print("4 - Buscar correspondências")
        print("0 - Sair")

        opcao = input("Selecione uma opção: ")

        if opcao == "1":
            cadastrar_produtor()
        elif opcao == "2":
            cadastrar_estabelecimento()
        elif opcao == "3":
            cadastrar_instituicao_caridade()
        elif opcao == "4":
            buscar_correspondencias()
        elif opcao == "0":
            print("Obrigado por utilizar o HarvestLink. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Execução do programa
if __name__ == "__main__":
    main()




