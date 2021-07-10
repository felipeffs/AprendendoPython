from random import randint

print('Tente advinhar que número eu pensar em menos tentativas conseguir\n'
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
