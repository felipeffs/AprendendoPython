"""
Crie um programa que leia um número inteiro
e mostre na tela se é PAR ou ÍMPAR.
"""

n = int(input('Digite um número: '))

print('{} é Par'.format(n) if (n % 2) == 0 else '{} é Ímpar'.format(n))
