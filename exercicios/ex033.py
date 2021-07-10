"""
Faça um programa que leia três números e
mostre qual é o maior e qual é o menor.
"""

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 > n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1
if maior < n3:
    maior = n3
if menor > n3:
    menor = n3

print('Maior número: {}'
      '\nMenor número: {}'.format(maior, menor))
