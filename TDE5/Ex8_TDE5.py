'''8. A Amplitude amostral é uma medida de dispersão, ela é calculada como a diferença entre o valor
máximo e o valor mínimo de uma amostra. Elabore um programa que leia um vetor de 10 posições
inteiras e então mostre o valor máximo, o valor mínimo e a amplitude amostral do conjunto
fornecido.'''

list = []

for i in range(10):
    numbers = int(input("\nDigite um número inteiro: "))
    list.append(numbers)
min = min(list)
max = max(list)
amplitude = max - min
print(f"\nA lista dos números digitados é {list}\nO valor mínimo é {min}\
      \nO valor máximo é {max}\nA amplitude amostral é {amplitude}\n")

