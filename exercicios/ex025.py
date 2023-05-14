"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem
"SILVA" no nome.
"""

nome = str(input('Nome: ')).strip()

print('Possui Silva no nome? {}'.format('SILVA' in nome.upper()))
