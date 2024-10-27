#Escreva um programa onde o usuário deve adivinhar um número secreto. O programa deve dizer se o palpite está correto, muito alto ou muito baixo.

from random import randint

numero = randint(1, 10)
print("Estou pensando num número do 1 ao 10 e você tem que adivinhar qual é!")
#print(numero)

while True:
    tentativa = int(input("Digite um número!: "))

    if abs(numero - tentativa) == 1:
        print("Quase!") 
    elif numero > tentativa:
        print("Mais alto")
    elif numero < tentativa:
        print("Mais baixo")
    else:
        print(f"Parabéns! {tentativa} era o número no qual eu estava pensando.")
        break
    