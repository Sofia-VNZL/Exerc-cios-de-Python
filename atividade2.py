def pergunta():
    casos = int(input("Deseja converter minutos em horas(1) ou horas em minutos(2)?: "))

    match casos:
        case 1:
            minutos_horas()
        case 2:
            horas_minutos()

def minutos_horas():
    minutos = int(input("Digite o tempo em minutos para converter em horas: "))

    min_h = int(minutos / 60)
    min_min = int(minutos % 60)

    print (f"{minutos} equivale a {min_h} hora(s) con {min_min} minuto(s)")

    reverter = input("deseja reverter a operação? (s / n)")

    if reverter == 's':
        print(f"{min_h}:{min_min} h equivale a {minutos} min")
    else:
        print("Fim da operação")


def horas_minutos():
    horas = int(input("Digite o numero de horas para converter em min: "))
    min = int(input("Caso tenha minutos restando das horas digitadas, por favor escrever, caso contrario digite '00': "))

    h_min = int(horas * 60 + min)

    print(f"{horas}:{min} equivale a um total de {h_min} min")

pergunta()