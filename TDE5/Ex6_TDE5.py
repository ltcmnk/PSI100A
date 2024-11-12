# 6. Ler 4 números inteiros e calcular a soma dos que forem par.

counter = 0
even = []
while counter != 4:
    number = int(input("Digite um número: "))
    if number % 2 == 0:
        even.append(number)
    counter += 1
print(f'\nOs números pares digitados são {even}')
print(f'A soma dos números pares é {sum(even)}')

