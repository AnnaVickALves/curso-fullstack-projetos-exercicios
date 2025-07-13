0#Lista de exercícios 1 - UC1

#Questão 1: Crie um programa que realize cálculo de ICM.
'''
nome = input("Digite seu nome: ")
altura = float (input("Digite sua altura: "))
peso = float (input("Digite seu peso: "))

imc = peso/(altura**2)

print ("%s, seu imc: %f " % (nome, imc))
'''
#Questão 2: Crie um programa que leia dois números e exiba qual é o maior.
'''
num1 = int (input("Digite o primeiro número: "))
num2 = int (input("Digite o segundo número: "))

if num1 > num2:
    print(f"O número {num1}, é maior.")
else:
    print(f"O número {num2}, é maior.")
'''



#Questão 3: Crie um programa que pergunte uma senha ao usuário e continue pedindo até que ele acerte a senha correta.

'''
senha_correta = "python 123"
tentativa = input("Digite a senha: ")

while senha_correta != tentativa:
    tentativa = input("Senha incorreta. Tente novamente")
        
print(f"Acesso liberado.")
'''

#Questão 4: Crie um programa que leia o nome de 5 pessoas usando o for e armazene em uma lista. Depois exiba todos os nomes.
'''listanomes = [] #cria lista vazia
for i in range(5):  #pede 5 nomes
    nome = input(f"Digite o nome da pessoa {i + 1 }: ")
    listanomes.append(nome) #.append(): metodo que adiciona um nome
    print("\nNomes digitados") #\n: quebra de linha
    for nome in listanomes:
        print(nome)
'''


#Questão 5: Crie um programa em PYthon que: 
#   Solicite ao usuário que insira valores inteiros para preencher uma matriz 2x2(ou seja 2 linhas e 2 colunas)
#   Armazene os valores em uma estrutura de matriz (listas de listas)
#   Ao final,exiba a matriz formatada linha por linha
'''
matriz = []
for i in range(2): #O que significa range?
    linha = []

    for j in range(2):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        linha.append(valor) # O que significa append?

print("\Matriz 2x2")
for linha in matriz:
    print(linha)
'''
