#Atv_11
# Para ser apta a doar sangue a pessoa deve ter entre 18 e 65 e pesar no mínimo 50kg.
#Escreva um alogoritmo que leia a idade e o peso de uma pessoa e apresente na tela uma mensagem 
#informando se ela pode ser doadora ou não

idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))

if 18 <= idade <= 65 and peso >= 50:
    print("Você pode doar sangue.")
else:
    print("Sua idade e/ou peso não permitem doar sangue.")


