"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
▸ O nome com todas as letras maiúsculas e minúsculas.
▸ Quantas letras ao todo (sem considerar espaços).
▸ Quantas letras tem o primeiro nome.
"""

a = str(input('Nome Completo: ')).strip()

print('Nome todo em minúsculo: {}'.format(a.lower()))
print('Nome todo em maiúsculo {}'.format(a.upper()))
print('Quantidade de letras sem contar espaços: {}'.format(len(a) - a.count(' ')))
print('Quantidade de letras no primeiro nome: {}'.format(a.find(' ')))
