'''
O programa ele solicita um número, verificar se é válido e faz uma soma de 1 até o número digitado, depois imprime a soma 
'''

soma=0

num = int (input("Digite um número: "))
while num <= 0:
    num = int(input("Número inválido, digite outro número: "))

for i in range(0,num+1):
    soma += i

print(soma)

