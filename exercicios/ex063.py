"""
Escreva um programa que leia um número n inteiro qualquer e mostre na tela
os n primeiros elementos de uma Sequência de Fibonacci.
Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8
"""

print('> Sequência de Fibonacci')
n = int(input('   Quantidade de números: '))
c = 2
tanterior = 0
tsucessor = 1
print('  S: 0 → 1', end=' ')
while c != n:
    soma = tanterior + tsucessor
    print('→ {}'.format(soma), end=' ')
    tanterior = tsucessor
    tsucessor = soma
    c += 1
