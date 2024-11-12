'''6. A distância rodoviária entre algumas capitais brasileiras está disponível na tabela abaixo. Para
consultar a distância basta cruzar as cidades origem e destino, ou seja, a distância entre Curitiba e
São Paulo é de 408 km.
Construa um programa que inicialize uma matriz contendo as distâncias apresentadas na tabela acima
e que então informe ao usuário o tempo necessário para percorrer duas cidades por ele fornecidas.'''

distancias = {
    'CURITIBA': {'CURITIBA': 0, 'FLORIANÓPOLIS': 310, 'PORTO ALEGRE': 716, 'SÃO PAULO': 408, 'RIO DE JANEIRO': 852},
    'FLORIANÓPOLIS': {'CURITIBA': 310, 'FLORIANÓPOLIS': 0, 'PORTO ALAGRE': 470, 'SÃO PAULO': 705, 'RIO DE JANEIRO': 1144},
    'PORTO ALEGRE': {'CURITIBA': 716, 'FLORIANÓPOLIS': 470, 'PORTO ALAGRE': 0, 'SÃO PAULO': 1119, 'RIO DE JANEIRO': 1553},
    'SÃO PAULO': {'CURITIBA': 408, 'FLORIANÓPOLIS': 705, 'PORTO ALEGRE': 1119, 'SÃO PAULO': 0, 'RIO DE JANEIRO': 429},
    'RIO DE JANEIRO': {'CURITIBA': 852, 'FLORIANÓPOLIS': 1144, 'PORTO ALEGRE': 1553, 'SÃO PAULO': 429, 'RIO DE JANEIRO': 0}
}

print("Cidades: \nCuritiba, Florianópolis, Porto Alegre, São Paulo, Rio de Janeiro.")

cid1 = input("\nDigite a cidade inicial: ").upper()
cid2 = input("\nDigite a cidade final: ").upper()
veloc = float(input("\nDigite a velocidade média em km/h: "))

if cid1 in distancias and cid2 in distancias[cid1]:
    distancia = distancias[cid1][cid2]
    tempo = distancia / veloc
    print(f"\nPara ir de {cid1} até {cid2} em {veloc} k/h, leva {tempo:.2f} horas.")
else:
    print("\nCidade(s) inválida(s)!")

