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

def menu (saldo):
    while True:
        print("\n===== CAIXA ELETRÔNICO ====")
        print("\nSeja bem-vindo!")
        print("\n*MENU*")
        print("\n1. Depositar")
        print("\n2. Sacar")
        print("\n3. Ver Saldo")
        print("\n0. Sair")
        opcao = input("\nEscolha uma opção: ")

        match opcao:
                case "1": #Depositar
                    saldo = depositar(saldo)
                
                case "2": #Sacar
                   saldo = sacar(saldo)


                case "3": #Ver Saldo
                    saldo = verSaldo(saldo)
                
                case "0":
                    print("\nSaindo do sistema... Até logo!")
                    break
            
                case _:
                    print("\nOpção inválida. Tente novamente.")  
                    break  
            


def depositar(saldo):
    while True:
        deposito = float(input("\nDigite o valor que deseja depositar: "))
        if deposito <= 0:
            print("\nNão é possível depositar esse valor! Tente novamente.")
        else:
            saldo = saldo + deposito
            print("\nDeposito efetuado com sucesso!")
            break
    voltar_ao_menu()
    return saldo


def sacar(saldo):
    saque = float(input("\nDigite o valor que deseja sacar: "))
    if saldo == 0:
        print("\nSaldo insuficiente! Tente novamente.")
    else:
        saldo = saldo - saque
        print("\nSaque efetuado com sucesso!") 
        print("\nTecle (M) para voltar ao menu", menu) 
        return saldo

def verSaldo(saldo):
    print(f"\nSeu saldo é {saldo:.2f}")
    voltar_ao_menu()
    return saldo
    


def voltar_ao_menu():
    while True:
        voltar = input("\nTecle 'M' para voltar ao menu: ").upper() #O .upper() é um método de string em Python que transforma todas as letras minúsculas em maiúsculas.
        if voltar == "M":
            return  # volta para o menu principal (encerra essa função)
        else:
            print("Entrada inválida. Tente novamente.")

            

       

menu(saldo)


        





