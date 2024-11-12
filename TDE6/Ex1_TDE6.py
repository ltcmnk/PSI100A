'''Desenvolva um programa que leia uma matriz quadrada de números inteiros de dimensão (4×4), e
então coloque em um outro vetor de 4 posições o maior valor encontrado na coluna da matriz cujo
índice é o mesmo do vetor, ou seja, o maior valor da coluna zero da matriz na posição zero do vetor e
assim por diante. Mostre então a matriz, o vetor e a média aritmética do vetor.'''

m = []
v = [0] * 4

for i in range(4):
    linha = []
    for j in range(4):
        valorM = int(input(f"\nDigite um valor inteiro para [{i}]x[{j}]: "))
        linha.append(valorM)
    m.append(linha)
print(m)

for j in range(4):
    maior = m[0][j]
    for i in range(1, 4):
        if m[i][j] > maior:
            maior = m[i][j]
    v[j] = maior

print("\nA matriz ficou: ")
for linha in m:
    print(linha)

print("\nOs maiores valores por coluna: ")
print(v)

media = sum(v) / len(v)

print("\nMédia do vetor: ", media)
