#Programa para gerenciamento de Estoque

# Função para cadastrar produtos na matriz
def cadastrar_produto(matriz):

    for _ in range(2): #loop para cadastrar x produtos
        nome_do_produto = str(input("Digite o nome do produto: "))
        quantidade = int(input("Digite a quantidade do produto: "))
        preco_unitario = float (input("Digite o preço do produto: "))

        # Adiciona os dados do produto como uma sublista na matriz principal
        matriz.append([nome_do_produto, quantidade, preco_unitario]) 

    return matriz #retorna os dados da matriz



#Função para exibir produtos já cadastrados
def visualizar_produtos(matriz):
    print("\n === PRODUTOS CADASTRADOS ===")
    print("\nNome || Quant || Preço")
    for produto in matriz:
        print(f"{produto[0]} || {produto[1]} || R${produto[2]:.2f}")



#Função para mostrar os produtos com estoque baixo
def controle_estoque(matriz):
    print("\n === CONTROLE DE ESTOQUE ===")
    for produto in matriz:
        if produto[1]<=5:
            print(f"{produto[0]} - ESTOQUE BAIXO")


# Função principal que exibe o menu e gerencia as opções do usuário
def menu():
    matriz = [] # Inicializa a matriz vazia no início do sistema
    while True: 
        print("\n===== SISTEMA DE GERENCIAMENTO DE ESTOQUE ====")
        print("\nSeja bem-vindo!")
        print("\n*MENU*")
        print("\n1. Cadastrar Produto")
        print("\n2. Visualizar produtos")
        print("\n3. Controle do estoque")
        print("\n0. Sair")

        opcao = input("\nEscolha uma opção: ")

        match opcao:
            case "1": #Cadastrar Produto
                matriz = cadastrar_produto(matriz)
                print("\nProduto cadastrado com sucesso!")

            case "2":  # Visualizar produtos
                visualizar_produtos(matriz)

            case "3":  # Controle do estoque
                controle_estoque(matriz)

            case "0": # sair
                print("Saindo do sistema... Até logo!")
                break
            case _: # entrada inválidafo
                print("Opção inválida.")

# Chamada da função principal para iniciar o programa
menu()

