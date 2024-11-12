'''2. Implemente um programa que permita multiplicar uma matriz de ordem (3×3) de números inteiros
fornecida pelo usuário por um número também fornecido pelo usuário.
Lembrete: para multiplicar uma matriz Am×n por um escalar k, basta multiplicar cada entrada aij
de A por k.
Assim, a matriz resultante B será também da ordem (m×n) e bij = k * aij.
'''

mA = []
mB = []

for i in range(3):
    linha = []
    for j in range(3):
        valorA = int(input(f"\nDigite um valor inteiro para [{i}]x[{j}]: "))
        linha.append(valorA)
    mA.append(linha)

k = int(input("\nDigite o número inteiro pelo qual gostaria de multiplicar os valores na matriz: "))
for i in range(0, 3):
    linha = []
    for j in range(3):
        valorB = (mA[i][j]) * k
        linha.append(valorB)
    mB.append(linha)

print("\nA matriz era: ")
for linha in mA:
    print(linha)

print("\nA matriz ficou: ")
for linha in mB:
    print(linha)
