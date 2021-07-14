"""
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5x4x3x2x1 = 120
"""

print('>Fatorial')
n = int(input(' Digite um número: '))
f = n
for c in range(1, n):
    f *= c
print('Fatorial de {} é igual a {}'.format(n, f))
