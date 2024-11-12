# 4. Leia dois valores reais do teclado, calcular e imprimir na tela:
# 5. a) A soma destes valores b) O produto deles c) O quociente entre eles

numberOne = int(input("Digite o primeiro número inteiro: "))
numberTwo = int(input("Digite o segundo número inteiro: "))

if numberOne < numberTwo:
    quociente = numberTwo / numberOne
else:
    quociente = numberOne / numberTwo

print(f'\nSoma: {numberOne + numberTwo}\nProduto: {numberOne * numberTwo}\nQuociente: {quociente}')
