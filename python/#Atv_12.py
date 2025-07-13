#Atv_12
# Uma determinada companhia aérea só contrata aeromoças que preeencham os seguintes requisitos:
#Ter idade igual ou superior a 24 anos / ter altura igual ou superior a 1.70 / falar com fluência 2 ou mais idiomas.
#Escreva um algoritmo que leia a idade, a altura e a quantidade de idiomas falados com fluência de uma candidata e imprima
#uma mensagem informando se essa candidata atende ou não aos requisitos da companhia aérea

sexo = input("Qual seu sexo(F ou M)? ")
idade = int(input("Qual sua idade: "))
altura = float(input("Qual sua altura: "))
idiomas = int(input("Qual quantos idiomas você fala fluêntemente: "))


if sexo == "F" and idade >= 24 and altura >= 1.70 and idiomas >= 2 :
    print("Parabéns! Você passou!")
else:
    print("Infelizmente você não atendeu a todos os critérios!")