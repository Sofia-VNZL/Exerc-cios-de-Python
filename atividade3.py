def combinar (nome1, nome2):

    metade_nome1 = nome1[:len(nome1)//2]
    metade_nome2 = nome2[len(nome2)//2:]
                         
    nome_combinado = metade_nome1 + metade_nome2
    return nome_combinado.capitalize()

def pergunta():
    usuario1 = input("Digite um nome!: ")
    usuario2 = input("Digite outro nome!: ")

    nome_fabuloso = combinar(usuario1, usuario2)
    outro_nome_fabuloso = combinar(usuario2, usuario1)

    print(f"O novo nome criativo é: {nome_fabuloso}")

    confirmacao = input("Gostou do nome? (s/n): ")

    match confirmacao:
        case 's':
            print(f"Fico feliz, {nome_fabuloso}!")
        case 'n':
            print(f"Então que acha de {outro_nome_fabuloso}?")
            resposta = input("Gostei(1) / Não gostei(2)")
            if resposta == '1':
                print(f"Fico feliz, {outro_nome_fabuloso}!")
            else:
                print("Então vamos tentar de novo com outros nomes!")
                pergunta()

pergunta()


