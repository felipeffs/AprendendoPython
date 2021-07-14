"""
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5x4x3x2x1 = 120
"""

print('>Fatorial')
n = int(input(' Digite um número: '))
p = n
fatorial = n
while p != 1:
    p -= 1
    fatorial *= p
print('O Fatorial de {} é igual a {}'.format(n, fatorial))
