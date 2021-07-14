"""
Faça um programa que leia um número inteiro e diga se ele é ou não um
número primo.
"""

n = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        tot += 1
if tot == 2:
    print('{} é um número primo'.format(n))
else:
    print('{} não é um número primo'.format(n))
