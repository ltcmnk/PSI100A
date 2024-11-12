'''11. Escreva um programa que leia um vetor de números inteiros de 10 posições, aceitando apenas valores
positivos. Modifique então o vetor de forma que, tenhamos primeiro todos os números pares, depois,
os números ímpares. Mostre o vetor antes de depois da modificação.'''

list = []
even = set()
odd = set()

for i in range(10):
    number = int(input("\nDigite um número inteiro: "))
    if number > 0:
        list.append(number)
print("\nO vetor inicial é:", v)

for number in v:
    if number % 2 == 0:
        even.add(number)
    else:
        odd.add(number)

list = [even, odd]
print(f"\nO vetor modificado é: {list}")