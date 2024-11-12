'''13. Desenvolva um programa que leia um vetor de 20 posições inteiras e o coloque em ordem crescente,
utilizando a seguinte estratégia de ordenação:
• selecione o elemento do vetor de 20 posições que apresenta o menor valor;
• troque este elemento pelo primeiro;
• repita estas operações, envolvendo agora apenas os 19 elementos restantes (trocando o de
menor valor com a segunda posição), depois os 18 elementos (trocando o de menor valor com a
terceira posição), depois os 17, 16 e assim por diante, até restar um único elemento, o maior
deles.'''

list = []
for i in range(20):
        number = int(input("\nDigite um número inteiro: "))
        list.append(number)

print(f"\nVetor original: {list}")

for i in range(len(v)):
    menor = i
    for m in range(i + 1, len(list)):
        if list[m] < list[menor]:
            menor = m
    list[i], list[menor] = list[menor], list[i]

print(f"\nVetor ordenado: {list}")


