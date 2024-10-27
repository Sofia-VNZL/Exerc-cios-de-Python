#Crie um programa que pergunte a idade do usuário e verifique se ele é maior de idade ou não.

idade = int(input("Escreva a sua idade: "))

def verificacao(idade):
    if idade >= 18:
        return "Maior de idade"
    elif 18 > idade:
        return "Menor de idade"
    else:
        return "idade tem que ser um numero!" 


print(f"Você tem {idade} anos? então é {verificacao(idade)}")
