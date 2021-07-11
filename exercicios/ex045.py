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
adversário = choice(p)

print('--'*20)
print('PEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('E TESOOOOURA!')
print('--'*20)

if e == 'papel' and adversário == 'tesoura':
    print('Você jogou papel....\n'
          'MAS eu tesoura\n'
          'MWHAHAHAHAH')
elif e == 'papel' and adversário == 'pedra':
    print('V-você jogou papel....\n'
          'na minha pedra\n'
          'INJUSTO!!!!')
elif e == 'pedra' and adversário == 'papel':
    print('Peguei a pedra que tacaste\n'
          'COM MEU LINDO PAPEL\n'
          '>:)')
elif e == 'pedra' and adversário == 'tesoura':
    print('A sua pedra foi muito dura\n'
          'com a minha tesourinha escolar\n'
          'vou arranjar uma tesoura mais forte, vai vendo >:(')
elif e == 'tesoura' and adversário == 'papel':
    print('A sua tesoura passou cortando o meu papel\n'
          'Em uma velocidade inacreditável\n'
          'Tá roubando!!!')
elif e == 'tesoura' and adversário == 'pedra':
    print('A sua tesoura foi esmagada pela minha FUCKING PEDRA!!!!\n'
          'hihihihi\n'
          'Não fique triste, melhore!')
elif e == adversário:
    print('Nosso poder é equivalente, empatamos')
else:
    print('{}????\n'
          'Não sabe ler???'.format(e))
