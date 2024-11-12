'''7. Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos.
Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n, verificar se n é
triangular.'''

a = 0
b = 1
c = 2
x = 0

n = int(input("Digite um número para saber se ele é triangular: "))
while x < n:
    a += 1
    b += 1
    c += 1
    x = a * b * c
if x == n:
    print(f"\n{n} é triangular, pois {a} * {b} * {c} = {n}")
else:
    print(f"\n{n} não é triangular.")
