#Desenvolva um programa que verifique se uma palavra ou frase inserida pelo usuário é um palíndromo (lê-se igual de trás para frente).

palavra = input("Digite uma palavra e descubra se é um políndromo!!!: ").lower()

if palavra == palavra[::-1]:
    print("É um políndromo!")
else:
    print("Não é um políndromo :(")