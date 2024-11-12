# 3. Leia três números do teclado e verificar se o primeiro é maior que a soma dos outros dois.

numberOne = int(input("Digite um número inteiro: "))
numberTwo = int(input("Digite outro número inteiro: "))
numberThree = int(input("Digite um último número inteiro: "))

sumNumbers = numberTwo + numberThree 

if sumNumbers < numberOne:
    print(f'\nO número {numberOne} é maior que a soma de {numberTwo} e {numberThree}, que tem um total de {sumNumbers}')
else:
    print(f'\nO primeiro número digitado, {numberOne}, não é maior que a soma de {numberTwo} e {numberThree} que tem um total de {sumNumbers}')