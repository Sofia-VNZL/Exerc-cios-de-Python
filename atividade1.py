def calcular_operacoes(num1, num2):
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    divisao = num1 / num2 if num2 != 0 else "Erro: Divisão por zero!"
    divisao_inteira = num1 // num2 if num2 != 0 else "Erro: Divisão inteira por zero!"
    
    print(f"Soma: {soma}")
    print(f"Subtração: {subtracao}")
    print(f"Multiplicação: {multiplicacao}")
    print(f"Divisão: {divisao}")
    print(f"Divisão Inteira: {divisao_inteira}")


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))


calcular_operacoes(num1, num2)

