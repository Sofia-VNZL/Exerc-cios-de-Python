#Faça um programa que calcule o Índice de Massa Corporal (IMC) do usuário e forneça feedback com base no valor (por exemplo, abaixo do peso, peso normal, sobrepeso).

print("Vamos a calcular seu Índice de Massa Corporal!")
  

altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite sua massa em quilos: "))
imc = peso /(altura**2)


def classificacao(imc):
   match imc:
        case imc if imc < 18.5:
            return "Abaixo do peso"
        case imc if 18.5 <= imc < 24.9:
            return "Peso ideal"
        case imc if 25 <= imc < 29.9:
            return "Sobrepeso"
        case imc if 30 <= imc < 34.9:
            return "Obesidade Grau I"
        case imc if 35 <= imc < 39.9:
            return "Obesidade Grau II"
        case imc if 39.9 < imc:
            return "Obesidade Grau III"
        case _:
            return "Número inválido"

feedback = classificacao(imc)

print(f"O seu indice de massa corporal é de {imc:.2f} kg/m2, clasificado como '{feedback}'")

   