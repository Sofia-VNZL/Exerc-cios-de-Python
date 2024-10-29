#Crie um programa que apresente ao usuário uma série de escolhas (como em uma história) e conduza a diferentes resultados com base nessas escolhas.

import random

# Dados de personagem e narrativa reutilizada:
nomes = ["Art", "Gaspar", "Morgana", "Isa"]
racas = ["anão", "elfo", "humano", "gnomo", "dragão"]
paises = ["Valandor", "Nytheria", "Zyrenhold", "Lunaris"]
funcoes = ["bardo", "ladino", "paladino", "mago", "clérigo", "bárbaro"]
eventos = ["anúncio que o Flamengo foi para a série B", "cataclismo", "terremoto", "enchente devastadora"]
builds = ["força extraordinária", "capacidade de dormir em pé", "grande quantidade de mana", "resistência sobre-humana", "inteligência"]

# Geração de personagem da outra atividade reutilizando:
nome = random.choice(nomes)
raca = random.choice(racas)
pais = random.choice(paises)
funcao = random.choice(funcoes)
build = random.choice(builds)
idade = random.randint(15, 300)


print(f"Bem-vindo, aventureiro! Sua jornada começa agora.")
print(f"Seu personagem é {nome}, um {raca} de {idade} anos que vive em {pais}.")
print(f"Ele possui uma habilidade única: {build}.")
print(f"Recentemente, um {random.choice(eventos)} abalou {pais}, forçando {nome} a sair em uma nova aventura.")

#atividade 15 em questão:
def escolha_caminho():
    print("\nVocê chega a uma bifurcação no caminho. Para onde você deseja ir?")
    print("1. Ir para a cidade próxima em busca de abrigo.")
    print("2. Explorar uma misteriosa floresta.")
    escolha = input("Escolha 1 ou 2: ")
    
    if escolha == "1":
        cidade()
    elif escolha == "2":
        floresta()
    else:
        print("Escolha inválida. Tente novamente.")
        escolha_caminho()

def cidade():
    print("\nVocê decide ir para a cidade. No caminho, você encontra um grupo de mercadores que oferece uma poção mágica.")
    print("1. Aceitar a poção.")
    print("2. Recusar educadamente e seguir seu caminho.")
    escolha = input("Escolha 1 ou 2: ")

    if escolha == "1":
        print(f"\n{nome} bebe a poção e sente uma energia renovada! Sua habilidade {build} é aprimorada, e ele se torna um herói local.")
    elif escolha == "2":
        print(f"\n{nome} decide recusar a poção. Mais tarde, descobre que os mercadores eram na verdade feiticeiros malignos. Foi uma sábia decisão!")
    else:
        print("Escolha inválida. Tente novamente.")
        cidade()

def floresta():
    print("\nVocê entra na floresta e encontra um velho sábio que oferece um teste de coragem.")
    print("1. Aceitar o teste.")
    print("2. Recusar e seguir em frente.")
    escolha = input("Escolha 1 ou 2: ")

    if escolha == "1":
        print(f"\n{nome} enfrenta o teste e sai vitorioso! Ganha um amuleto que aumenta sua habilidade: {build}.")
    elif escolha == "2":
        print(f"\n{nome} segue em frente, mas o velho sábio o amaldiçoa. Sua jornada será cheia de desafios adicionais!")
    else:
        print("Escolha inválida. Tente novamente.")
        floresta()


escolha_caminho()
