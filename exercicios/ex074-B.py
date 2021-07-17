"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma
tupla. Depois disso, mostre a listagem de números gerados e também indique o
menor e o maior valor que estão na tupla.
"""

from random import randint

numeros = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
maior = menor = 0
print('Os números sorteados foram: ', end='')
for n in numeros:
    print(n, end=' ')
print(f'\nO maior número é {max(numeros)} e o menor é {min(numeros)}')
