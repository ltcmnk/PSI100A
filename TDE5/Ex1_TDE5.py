# 1. Construa a tabela de multiplicação de 1 a 10. (Ex: 1x1 = 1, 1x2=2, 10x10 =100)

number = int(input("Digite um número inteiro para obter a tabela de multiplicação (tabuada): \n"))
multiply = 1
print(f'\nTABUADA DO {number}\n')

for multiply in range(1,11):
    result = multiply * number
    print(f'{number} * {multiply} = {result}')
    multiply += 1
