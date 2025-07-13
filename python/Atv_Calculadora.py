#Calculadora executar as quatros operações (+,-,/,*), até o usuário pedir pra parar

operacao = (input("Escolha uma operação (+,-,*,/): "))
a = int (input("Digite o primeiro valor: "))
b = int (input("Digite o segundo valor: "))

if operacao == "+":
    print(a+b)
elif operacao == "-":
    print(a-b)
elif operacao == "*":
    print(a*b)
elif operacao == "/":
    print(a/b)
 