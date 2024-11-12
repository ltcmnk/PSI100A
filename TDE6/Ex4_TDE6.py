'''4. Escreva um programa que preencha uma matriz quadrada de números inteiros de dimensão (5×5)
com valores inteiros (dentro do intervalo 10 a 99). Para cada uma das figuras abaixo (elabore quatro
versões do programa): mostre a matriz original, mostre a matriz apenas com os valores que estão na
parte hachurada e mostre a soma destes valores:'''

import random

m = [[random.randint(10, 99) for _ in range(5)] for _ in range(5)]

print("\nMatriz original:\n")
for linha in m:
    print(" ".join(f"{x:>2}" for x in linha))

#a)
indicesA = [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
             (0, 2), (1, 2), (3, 2), (4, 2)]

hachuradaA = [[" " for _ in range(5)] for _ in range(5)]
for i, j in indicesA:
    hachuradaA[i][j] = m[i][j]

somaA = sum(m[i][j] for i, j in indicesA)

print("\n\n\nMatriz a)\n")
for linha in hachuradaA:
    print(" ".join(f"{x:>2}" if isinstance(x, int) else "  " for x in linha))
print("\nSoma a) ", somaA)


#b)
indicesB = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
             (1, 0), (1, 4),
             (2, 0), (2, 4),
             (3, 0), (3, 4),
             (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]

hachuradaB = [[" " for _ in range(5)] for _ in range(5)]
for i, j in indicesB:
    hachuradaB[i][j] = m[i][j]

somaB = sum(m[i][j] for i, j in indicesB)

print("\n\n\nMatriz b)\n")
for linha in hachuradaB:
    print(" ".join(f"{x:>2}" if isinstance(x, int) else "  " for x in linha))
print("\nSoma b) ", somaB)


#c)
indicesC = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4),
             (0, 4), (1, 3), (3, 1), (4, 0)]

hachuradaC = [[" " for _ in range(5)] for _ in range(5)]
for i, j in indicesC:
    hachuradaC[i][j] = m[i][j]

somaC = sum(m[i][j] for i, j in indicesC)

print("\n\n\nMatriz c)\n")
for linha in hachuradaC:
    print(" ".join(f"{x:>2}" if isinstance(x, int) else "  " for x in linha))
print("\nSoma c) ", somaC)


#d)
indicesD = [(i, j) for i in range(5) for j in range(5) if (i + j) % 2 == 0]

hachuradaD = [[" " for _ in range(5)] for _ in range(5)]
for i, j in indicesD:
    hachuradaD[i][j] = m[i][j]

somaD = sum(m[i][j] for i, j in indicesD)

print("\n\n\nMatriz d)\n")
for linha in hachuradaD:
    print(" ".join(f"{x:>2}" if isinstance(x, int) else "  " for x in linha))
print("\nSoma d) ", somaD)