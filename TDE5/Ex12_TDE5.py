'''12. Construa um programa que sugira uma aposta de Mega-Sena ou seja, um algoritmo que gera e mostra
um conjunto de 6 números aleatórios entre [1, 60] sem repetição. Em seguida, obtenha a aposta do
usuário (sem repetição) e indique quantos acertos ele teve.'''

import random
bet = []
right = 0

def getRandom():
    return random.sample(range(1, 61), 6)

for i in range(6):
    number = int(input("\nDigite um número para sua aposta: "))
    bet.append(number)

random = [getRandom()]
for i in range(len(bet)):
    if bet[i] == random:
        right += 1

print(f"\nOs números sorteados na Mega foram: {random}\nVocê acertou {right} números dos sorteados")
