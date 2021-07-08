import random
from time import sleep
p = random.randint(0, 5)

print('\nVAMOS BRINCAR ( •̀ ω •́ )✧\nPensei num número de 0 a 5, agora tente advinhar se for capaz')
a = int(input('Bora\n'))

if a == p:
    print('c-como você conseguiu? (°ロ°)')
else:
    print('( •_•)>⌐■-■')
    sleep(1)
    print('(⌐■_■)')
    sleep(1)
    print('ヾ(⌐■_■)ノ♪ Não se sinta mal pela sua incapacidade humano')
