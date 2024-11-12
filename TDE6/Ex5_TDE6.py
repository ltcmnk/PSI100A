'''5. Escreva um programa que popule uma matriz (15×7) de números inteiros sorteados dentro do
intervalo 10 a 99. Modifique então a matriz de forma que, caminhando da esquerda para a direita, de
cima para baixo, tenhamos primeiro todos os números pares, depois, os números impares. Mostre a
matriz antes e depois da modificação.'''

import random
def Random():
    return random.randint(10, 99)
m = []

for i in range(15):
    linha = []
    for j in range(7):
        linha.append(Random())
    m.append(linha)

print("Matriz original:")
for linha in m:
    print(linha)

pares = []
impares = []

for linha in m:
    for num in linha:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

nova_matriz = []
todos_numeros = pares + impares

for i in range(15):
    nova_linha = todos_numeros[i * 7:(i + 1) * 7]
    nova_matriz.append(nova_linha)

print("\nMatriz modificada:")
for linha in nova_matriz:
    print(linha)
