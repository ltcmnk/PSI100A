'''9. Elabore um programa que leia um vetor de 10 posições inteiras. Depois, solicite para o usuário um
número que ele gostaria de pesquisar neste vetor, caso o número exista no vetor, mostre em qual(is)
posição(ões) ele foi encontrado e quantas ocorrências foram detectadas.'''

list = []
position = []

for i in range(10):
    numbers = int(input("\nDigite um número inteiro: "))
    list.append(numbers)

numberFinder = int(input("\nDigite um número que gostaria de buscar no vetor: "))
cont = 0

for i in range(len(list)):
    if list[i] == numberFinder:
        position.append(i)
        cont += 1
if cont > 0:
    print(f"\nO número {numberFinder} está na(s) posição(ões) {position} e apareceu {cont} vez(es).")
else:
    print("\nO número não está no vetor.")


