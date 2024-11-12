'''7. Considerando a mesma tabela da questão anterior, desenvolva um programa que permita ao usuário
informar várias cidades em sequência, até inserir um código finalizador. Mostre então as cidades que
compõem o roteiro fornecido, a distância de cada percurso intermediário e a distância total do roteiro
fornecido.'''

distancias = {
    'CURITIBA': {'CURITIBA': 0, 'FLORIANÓPOLIS': 310, 'PORTO ALEGRE': 716, 'SÃO PAULO': 408, 'RIO DE JANEIRO': 852},
    'FLORIANÓPOLIS': {'CURITIBA': 310, 'FLORIANÓPOLIS': 0, 'PORTO ALAGRE': 470, 'SÃO PAULO': 705, 'RIO DE JANEIRO': 1144},
    'PORTO ALEGRE': {'CURITIBA': 716, 'FLORIANÓPOLIS': 470, 'PORTO ALAGRE': 0, 'SÃO PAULO': 1119, 'RIO DE JANEIRO': 1553},
    'SÃO PAULO': {'CURITIBA': 408, 'FLORIANÓPOLIS': 705, 'PORTO ALEGRE': 1119, 'SÃO PAULO': 0, 'RIO DE JANEIRO': 429},
    'RIO DE JANEIRO': {'CURITIBA': 852, 'FLORIANÓPOLIS': 1144, 'PORTO ALEGRE': 1553, 'SÃO PAULO': 429, 'RIO DE JANEIRO': 0}
}

rota = []
total = 0

print("Cidades: \nCuritiba, Florianópolis, Porto Alegre, São Paulo, Rio de Janeiro.")
while True:
    cid = input("Digite o nome de uma cidade, ou [fim] para finalizar: ").upper()

    if cid == 'FIM':
        break

    if cid in distancias:
        rota.append(cid)
    else:
        print("\nCidade inválida!")

if len(rota) > 1:
    print("\nRoteiro fornecido: ", " -> ".join(rota))

    for i in range(len(rota) - 1):
        cid1 = rota[i]
        cid2 = rota[i + 1]

        if cid2 in distancias[cid1]:
            distancia = distancias[cid1][cid2]
            total += distancia
            print(f"\nDe {cid1} até {cid2} = {distancia} km")
        else:
            print(f"Não há rota direta entre {cid1} e {cid2}.")

    print(f"\nDistância total do roteiro: {total} km")
else:
    print("Você deve fornecer ao menos duas cidades para calcular a distância.")


