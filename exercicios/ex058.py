"""
Melhore o jogo do Exercício 028 onde o computador vai "pensar" em um número
entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.
"""

from random import randint

print('Tente adivinhar que número eu pensar em menos tentativas conseguir\n'
      'Pensei, lesgooo\n')
tentativas = 0
computador = randint(0, 10)
acertou = False
while not acertou:
    jogador = int(input("Qual o seu palpite? "))
    if jogador == computador:
        acertou = True
    elif computador > jogador:
        print('É maior que {}'.format(jogador))
    else:
        print('É menor que {}'.format(jogador))
    tentativas += 1
if tentativas == 1:
    print('Caraleo mlk! Tu é bom mesmo （⊙ｏ⊙）')
elif tentativas < 11:
    print('PARABÉNS!!! Acertou com {} tentativas (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧'.format(tentativas))
else:
    print('Pooorraaa {} tentativas, mandou malzão brother!(っ °Д °;)っ'.format(tentativas))
