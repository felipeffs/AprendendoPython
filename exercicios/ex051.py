"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""

ptermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão: '))

for c in range(ptermo, ptermo + (10 * razao), razao):
    print(c, end=' ')
