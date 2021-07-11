"""
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que
passou do prazo.
"""
# EXTRA: Adicionar o gênero e mostrar se o alistamento é obrigatório ou não.

import datetime

ano = int(input('Qual o seu ano de nascimento? '))
atual = datetime.date.today().year
idade = atual - ano
sexo = str(input('Qual o seu gênero? ')).strip()[0]

if 'm' in sexo.lower():
    if idade == 18:
        print('Está na hora de se alistar no exército brasileiro.')
    elif idade < 18:
        print('falta {} ano(s) para se alistar.'.format(18 - idade))
        print('Seu alistamento será em {}.'.format(atual + (18 - idade)))
    else:
        print('Já passou {} ano(s), se não se alistou se aliste imediatamente.'.format(idade - 18))
        print('Deveria ter se alistado em {}.'.format(atual + (18 - idade)))
else:
    if idade == 18:
        print('Está apta para se alistar no exército brasileiro mas o alistamento militar não é obrigatório.')
    elif idade < 18:
        print('Ainda falta {} ano(s) para poder se alistar '
              'mas o alistamento militar não é obrigatório.'.format(18 - idade))
        print('Estará apta em {}.'.format(atual + (18 - idade)))
    else:
        print('Já tem {} anos que pode se alistar mas o alistamento militar não é obrigatório.'.format(idade - 18))
        print('Está apta desde {}.'.format(atual + (18 - idade)))
