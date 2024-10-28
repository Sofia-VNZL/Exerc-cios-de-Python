#Crie um programa que classifique as palavras inseridas pelo usuário como curtas (menos de 5 letras) ou longas (5 letras ou mais).

palavras = input("Digite uma palavra no contador mágico de palavras: ").split()

for carateres in palavras:
    if len(carateres) < 5:
        print(f"Essa é uma palavra curta de {len(carateres)} letras")
    else:
        print(f"Essa é uma palavra longa de {len(carateres)} letras")


