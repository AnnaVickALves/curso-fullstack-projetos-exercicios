#Atv_14 Caixa eletrônico simples
#Enunciado: Simule um caixa eletrônico que:
#Começa com R$ 1000,00 de saldo
#Oferece opções:
#Ver saldo/Sacar/Depositar/Sair
#Use while, if/else, e match/case para controlar o fluxo.

'''
 # def - é a representação de uma função. Funções são blocos de código que você pode reutilizar#
def nome_da_funcao(parâmetros):
    # bloco de código
    return resultado  # (opcional)


    #Passar saldo como argumento permite que cada função trabalhe com ele de forma isolada e segura.
'''


saldo = 1000


def depositar(saldo):
    while True:
        deposito = float(input("Digite o valor que deseja depositar: "))
        if deposito <= 0:
            print("Não é possível depositar esse valor! Tente novamente.")
        else:
            saldo = saldo + deposito
            print("Deposito efetuado com sucesso!")
            break
    voltar_ao_menu()



def sacar(saldo):
    saque = float(input("Digite o valor que deseja sacar: "))
    if saldo == 0:
        print("Saldo insuficiente! Tente novamente.")
    else:
        saldo = saldo - saque
        print("Saque efetuado com sucesso!") 
        print("Tecle (M) para voltar ao menu", menu) 



def menu (saldo):
    while True:
        print("\n===== CAIXA ELETRÔNICO ====")
        print("\nSeja bem-vindo!")
        print("\n*MENU*")
        print("\n1. Depositar")
        print("\n2. Sacar")
        print("\n3. Ver Saldo")
        print("\nn0. Sair")
        opcao = input("Escolha uma opção: ")

        match opcao:
            case 1: #Depositar
                saldo = depositar(saldo)

            case 2:  # Sacar
                saldo = sacar(saldo)

            case 3:  # Ver Saldo
                print(f"Seu saldo é R$ {saldo:.2f}")
                voltar_ao_menu()

            case 0:
                print("Saindo do sistema... Até logo!")
                break

            case _:
                print("Opção inválida. Tente novamente.")





menu























#-------------------------------------------------------------------------------------------------
def voltar_ao_menu():
    while True:
        voltar = input("\nTecle 'M' para voltar ao menu: ").upper() #O .upper() é um método de string em Python que transforma todas as letras minúsculas em maiúsculas.
        if voltar == "M":
            return  # volta para o menu principal (encerra essa função)
        else:
            print("Entrada inválida. Tente novamente.")