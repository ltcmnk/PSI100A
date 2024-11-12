'''10. Desenvolva um programa que leia 10 números inteiros e armazene-os em um vetor chamado vLido.
Depois, crie dois outros vetores: vPares, contendo somente os números pares de vLido, e vImpares
contendo somente os números ímpares de vLido. Os vetores vPares e vLido não deverão conter
zeros. Mostre então os três vetores.'''

listRead = []
listEven = []
listOdd = []

for i in range(10):
    numbers = int(input("\nDigite um número inteiro: "))
    listRead.append(numbers)

for numbers in listRead:
    if numbers > 0:
        if numbers % 2 == 0:
            listEven.append(numbers)
        else:
            listOdd.append(numbers)
print(f"\nlistRead = {listRead}\nlistEven = {listEven}\nlistOdd = {listOdd}")
