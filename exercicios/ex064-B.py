"""
Crie um programa que leia vários números inteiros pelo teclado. O programa
só vai parar quando o usuário digitar o valor 999, que é a condição de
parada. No final, mostre quantos números foram digitados e qual foi a soma
entre eles (desconsiderando o flag).
"""

soma = q = 0
n = int(input('Digite um número: '))
while n != 999:
    soma += n
    q += 1
    n = int(input('Digite um número: '))
print('{} foram digitados e a soma de seus valores foi {}'.format(q, soma))
