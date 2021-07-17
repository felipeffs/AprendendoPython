"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma
tupla. Depois disso, mostre a listagem de números gerados e também indique o
menor e o maior valor que estão na tupla.
"""

from random import randint

numeros = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
maior = menor = 0
print('Os números sorteados foram: ', end='')
for pos, n in enumerate(numeros):
    print(n, end=' ')
    if pos == 0:
        menor = n
        maior = n
    elif menor > n:
        menor = n
    elif maior < n:
        maior = n
print(f'\nO maior número é {maior} e o menor é {menor}')
