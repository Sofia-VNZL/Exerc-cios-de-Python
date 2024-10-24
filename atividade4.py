numero1 = int(input("Digite um número: "))
operador = input("Digite um operador (+, -, *, /): ")
numero2 = int(input("Digite um outro número: "))

if operador == '+':
    resultado = numero1 + numero2
elif operador == '-':
    resultado = numero1 - numero2
elif operador == '*':
    resultado = numero1 * numero2
elif operador == '/':
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Erro: Divisão por zero"
else:
    resultado = "Operador inválido"

print(f"O resultado foi: {resultado}")

