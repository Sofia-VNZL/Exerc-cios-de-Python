#Escreva um programa que permita ao usuário votar em três opções diferentes e, no final, exiba o número de votos de cada opção.

def votacao():
    maca = 0
    banana = 0
    morango = 0

    while True:
        voto = input("Ecolha entre Maçã (1), Banana (2) ou Morango (3) ou digite 'Fim': ").lower()

        if voto == 'fim':
            break 
    
        if voto == 'maça' or voto == '1':
            maca += 1
        elif voto == 'banana' or voto == '2':
            banana += 1
        elif voto == 'morango' or voto == '3':
            morango += 1
        else:
            print("Voto nulo!!!!")
    print(f"""Resultado da Votação:
    Maçã: {maca} votos
    Banana: {banana} votos
    Morango: {morango} votos""")

votacao()