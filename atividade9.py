#Desenvolva um programa que aplique descontos progressivos com base no valor da compra: desconto de 10% para compras acima de R$100, 15% para compras acima de R$200, seguindo a projeção até R$500, para valores maiores do que esse, o desconto é fixado em 25%.

compra = float(input("Digite o valor da compra: "))
desconto_10 = compra * 0.90
desconto_15 = compra * 0.85
desconto_20 = compra * 0.80 #ja que não há espaço para R$400, colocarei de compras acima de R$350 o desconto de 20%
desconto_25 = compra * 0.75

def valores(compra):
    if compra > 500:
        print(f"Sua compra de R${compra} ganhou um desconto de 25%, ficou em: {desconto_25:.2f}")
    elif compra > 350:
        print(f"Sua compra de R${compra} ganhou um desconto de 20%, ficou em: {desconto_20:.2f}")
    elif compra > 200:
        print(f"Sua compra de R${compra} ganhou um desconto de 15%, ficou em: {desconto_15:.2f}")
    elif compra > 100:
        print(f"Sua compra de R${compra} ganhou um desconto de 10%, ficou em: {desconto_10:.2f}")
    else:
        print("Error, digite um número válido")

valores(compra)