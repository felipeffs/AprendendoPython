"""
Escreva um programa que faça o computador "pensar" em um
número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
qual foi o número escolhido pelo computador. O programa deverá
escrever na tela se o usuário venceu ou perdeu
"""

import random
from time import sleep

p = random.randint(0, 5)

print('\nVAMOS BRINCAR! ( •̀ ω •́ )✧'
      '\nPensei num número de 0 a 5, agora tente adivinhar se for capaz.')
a = int(input('Bora! \n'))

if a == p:
    print('c-como você conseguiu? (°ロ°)')
else:
    print('( •_•)>⌐■-■')
    sleep(1)
    print('(⌐■_■)')
    sleep(1)
    print('ヾ(⌐■_■)ノ♪ Não se sinta mal pela sua incapacidade, humano.')
