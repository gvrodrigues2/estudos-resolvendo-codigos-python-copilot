
numero1 = float(input("Por favor, insira o primeiro número: "))

numero2 = float(input("Por favor, insira o segundo número: "))

operacao = input("Por favor, escolha a operação (+, -, *, /): ")

if operacao == '+':
    resultado = numero1 + numero2
elif operacao == '-':
    resultado = numero1 - numero2
elif operacao == '*':
    resultado = numero1 * numero2
elif operacao == '/':
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Erro: divisão por zero"
else:
    resultado = "Operação inválida"

print("Resultado: ", resultado)