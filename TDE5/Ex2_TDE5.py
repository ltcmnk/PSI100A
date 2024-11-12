# 1. Construa a tabela de multiplicação de 1 a 10 utilizando apenas um laço de repetição.

number = int(input("Digite um número inteiro para obter a tabela de multiplicação (tabuada): "))
multiply = 1
print(f'\nTABUADA DO {number}\n')

for multiply in range(1,11):
    result = multiply * number
    print(number, "*", multiply, "=", result)
    multiply += 1
