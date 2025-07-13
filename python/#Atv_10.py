#Atv_10

codigo = int(input("Digite o código do cargo: "))
salario = float(input("Digite o salário: "))

if (codigo == 101):
    novo = salario + salario * 0.10
elif (codigo == 102):
    novo = salario + salario * 0.20
elif (codigo == 103):
    novo = salario + salario * 0.30
else:
    novo = salario + salario * 0.40

diferenca = novo - salario
print("Antigo = %f" % salario)
print("Novo = %f" % novo)
print("Diferenca = %f" % diferenca)
