#Faça um programa que simule o lançamento de um dado. O usuário deve escolher quantos dados jogar e o programa deve exibir os resultados.

import random

quantos_dados = int(input("Quantos dados vai jogar?: "))
quantos_lados = int(input("Quantos lados tem seus dados?: "))

resultados = []

for _ in range(quantos_dados):
    resultado = random.randint(1, quantos_lados)
    resultados.append(resultado)

print("Os resultados são: ")
for i, resultado in enumerate(resultados, start=1):
    print(f"Dado {i}: {resultado}")

