'''
senha_correta = "python 123"
tentativa = ""

while tentativa != senha_correta:
    tentativa = input("Digite a senha: ")
    if tentativa != senha_correta:
        print(f"Senha incorreta. Tente novamente")
    else: 
        print(f"Acesso liberado.")
'''
#------------------------------------------------------------------------------------------------
'''Faça um programa que peça um número maior que 1 ao usuário. 
Em seguida, imprima todos os números, de 1 até o número que o usuário informou

num = 1 #define o valor de num como 1
max = int(input("Digite um número maior que um: ")) #max é definido como inteiro e lhe é atribuido a pergunta
while num <= max:# Enquanto num for menor ou igual ao max (numero digitado pelo usuario)
    print(num) # mostrar o num
    num += 1 # e depois o num vai receber +1
   '''
#--------------------------------------------------------------------------------------------------------
'''
carteira = float(input("O lanche é 7,00, quanto você tem?"))
troco = carteira - 7.00
print("Você tem %.2f reais de troco" %troco)
'''

#----------------------------------------
'''listanomes = [] #cria lista vazia
for i in range(5):  #pede 5 nomes
    nome = input(f"Digite o nome da pessoa {i + 1 }: ")
    listanomes.append(nome) #.append(): metodo que adiciona um nome
    print("\nNomes digitados") #\n: quebra de linha
    for nome in listanomes:
        print(nome)
'''
#-------------------------------------------------------------------------------------------
'''
listafrutas = []
for i in range(3):
    fruta = input(f"Digite o nome de uma fruta de sua preferência: ")

'''
#------------------------------------------------------------------------------------------
'''
matriz = [] #cria uma matriz

for i in range(3): 
    linha = []

    for j in range(3):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor)   
    matriz.append(linha)

print("\nMatriz 3x3: ")
for linha in matriz:
    print(linha)
'''

#------------------------------------------------------------------------------------------------

nome = input("Digite seu nome: ")
altura = float (input("Digite sua altura: "))
peso = float (input("Digite seu peso: "))

imc = peso/(altura**2)

print ("%s, seu imc: %f " % (nome, imc))