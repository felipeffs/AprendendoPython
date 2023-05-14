"""
Crie um programa que faça o computador jogar Jokenpô com você.
"""

from random import choice
from time import sleep

print('-='*20)
print('Duelo de PEDRA, PAPEL E TESOURA')
print('-='*20)
e = str(input('Vai jogar pedra, papel ou tesoura?\n')).strip().lower()
p = ['pedra', 'papel', 'tesoura']
adversario = choice(p)

print('--'*20)
print('PEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('E TESOOOOURA!')
print('--'*20)

if e == 'papel' and adversario == 'tesoura':
    print('Você jogou papel....\n'
          'MAS eu tesoura\n'
          'MWHAHAHAHAH')
elif e == 'papel' and adversario == 'pedra':
    print('V-você jogou papel....\n'
          'na minha pedra\n'
          'INJUSTO!!!!')
elif e == 'pedra' and adversario == 'papel':
    print('Peguei a pedra que tacaste\n'
          'COM MEU LINDO PAPEL\n'
          '>:)')
elif e == 'pedra' and adversario == 'tesoura':
    print('A sua pedra foi muito dura\n'
          'com a minha tesourinha escolar\n'
          'vou arranjar uma tesoura mais forte, vai vendo >:(')
elif e == 'tesoura' and adversario == 'papel':
    print('A sua tesoura passou cortando o meu papel\n'
          'Em uma velocidade inacreditável\n'
          'Tá roubando!!!')
elif e == 'tesoura' and adversario == 'pedra':
    print('A sua tesoura foi esmagada pela minha FUCKING PEDRA!!!!\n'
          'hihihihi\n'
          'Não fique triste, melhore!')
elif e == adversario:
    print('Nosso poder é equivalente, empatamos')
else:
    print('{}????\n'
          'Não sabe ler???'.format(e))
