def sorteia(lista):
    from random import randint
    from time import sleep
    print('Sorteando 5 valores... ', end='')
    for i in range(0, 5):
        r = randint(0, 10)
        lista.append(r)
        sleep(0.3)
        print(f'{r} ', end='')
    sleep(0.4)
    print('| PRONTO!!')


def somaPar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {lista}, temos {soma}.')


numeros = list()
sorteia(numeros)
somaPar(numeros)
