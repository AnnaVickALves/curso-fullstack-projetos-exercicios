#Atv_13
#A prefeitura de uma cidade abriu uma linha de crédito para os funcionário estatutários. O valor máximo da prestação não
#poderá ultrapassar 30% do salário bruto. Fazer um programa que permita entrar com o salário bruto e o valor da prestação
#e informar se o empréstimo pode ou não ser concedido.

salario = float(input("Digite o salário R$: "))
prestacao = float(input("Digite o valor da prestação R$: "))

limite = salario * 3.0

if prestacao <= limite:
    print("Emprétimo Aprovado!")
else:
    print("Emprétimo Negado.A prestação excede 30% do salário")