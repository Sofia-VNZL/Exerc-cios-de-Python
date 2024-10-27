#Escreva um programa que combine elementos aleatórios de listas diferentes (personagens, ações, locais) para criar uma história curiosa.

import random

nomes = ["Art", "Gaspar", "Morgana", "Isa"]
racas = ["anões", "elfos", "humanos", "gnomos", "dragões"]
paises = ["Valandor", "Nytheria", "Zyrenhold", "Lunaris"]
eventos = ["anuncio de que o Flamengo foi pra série B", "Um cataclismo", "terremoto"]
funcoes = ["bardo", "ladino", "paladino", "Mago", "clérigo", "bárbaro"]
idade = random.randint(15, 300)
vidas = ["tediosa", "tranquila", "díficil", "monotona"]
builds = ["Força extraordinaria", "Capacidade de dormir de pé", "Grande quantidade de Mana", "Resistencia sobrehumana", "Inteligência"]

print("Bem-vindo ao criador de personagens de RPG!")

def criar_historia():
    nome = random.choice(nomes)
    raca = random.choice(racas)
    pais = random.choice(paises)
    evento = random.choice(eventos)
    funcao = random.choice(funcoes)
    vida = random.choice(vidas)
    build = random.choice(builds)

    return f"""A historia do seu personagem começa assim: {nome} levava uma vida {vida} em {pais}, local dos {raca}, 
    mas quando fez {idade}, um {evento} fez que tivesse que fugir de {pais}. Longe de casa, {nome} virou {funcao} e se escondeu por um tempo.
    Mas a paz acabou quando um grupo de aventureiros descobriu que {nome} tinha uma carateristica única: {build}. 
    {nome} era a pessoa indicada para a missão do grupo! então insistiram até aceitar o convite."""


print(criar_historia())
