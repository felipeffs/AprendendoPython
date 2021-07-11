"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de
nascimento de um atleta e mostre sua categoria, de acordo com a idade:
— Até 9 anos: MIRIM
— Até 14 anos: INFANTIL
— Até 19 anos: JUNIOR
— Até 25 anos: SÊNIOR
— Acima: MASTER
"""

from datetime import date

ano = int(input('Ano de Nascimento do Atleta: '))

idade = date.today().year - ano

cat = 'master'
if idade <= 9:
    cat = 'mirim'
elif idade <= 14:
    cat = 'infantil'
elif idade <= 19:
    cat = 'junior'
elif idade <= 20:
    cat = 'sênior'

print('O atleta tem {} anos\nClassificação {}'.format(idade, cat.upper()))
