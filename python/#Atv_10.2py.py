#Atv_10.2
#Match Case

codigo = int(input("Digite o código do cargo: "))
salario = float(input("Digite o salário: "))

match codigo:
    case 101:
        novo = salario + salario * 0.10
    case 102:
        novo = salario + salario * 0.20
    case 103:
        novo = salario + salario * 0.30
    case _ :
        novo = salario + salario * 0.40

diferenca = novo - salario
print("Antigo = %.2f" % salario)
print("Novo = %.2f" % novo)
print("Diferenca = %.2f" % diferenca)