#Estrutura de Seleção (if, elif, else, match case)
'''1. Verifique se um número inteiro informado é par ou ímpar. Dica: use o operador `%` para 
verificar o resto da divisão por 2.
'''

num = int(input("Digite um número: "))
if (num % 2 == 0):
  print(f"{num} é um número par")
else:
  print(f"{num} é um número ímpar")
