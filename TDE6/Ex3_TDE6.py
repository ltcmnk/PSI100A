'''3. Elabore um programa que preencha uma matriz quadrada (4x4) de números inteiros, sorteados dentro
do intervalo 100 a 999, garantindo que não haverá nenhuma repetição (os 16 números devem ser
únicos). Encontre então o valor do menor elemento da linha em que se encontra o maior elemento da
matriz. Mostre a matriz e os dois valores encontrados.'''

import random
def Random():
    return random.sample(range(100, 999), 1)

m = []

for i in range(4):
    linha = []
    for j in range(4):
        linha.append(Random())
    m.append(linha)

maiorElem = m[0][0]
maiorPos = (0, 0)

for i in range(4):
    for j in range(4):
        if m[i][j] > maiorElem:
            maiorElem = m[i][j]
            maiorPos = (i, j)


menorElem = m[maiorPos[0]][0]
for valor in m[maiorPos[0]]:
    if valor < menorElem:
        menorElem = valor


print("\nA matriz ficou:")
for linha in m:
    print(linha)

print("\nO maior elemento da matriz é:", maiorElem, "\nO menor elemento de sua linha é:", menorElem)
