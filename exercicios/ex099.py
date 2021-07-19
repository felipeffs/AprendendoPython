"""
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros
com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual
deles é o maior.
"""


def maior(*valores):
    from time import sleep

    print('='*50)
    print('Analisando...')
    print(f'Os valores informados foram: ')
    m = 0
    tam = len(valores)
    for pos, v in enumerate(valores):
        sleep(0.3)
        if pos < tam - 2:
            print(f'{v}, ', end='')
        elif pos < tam - 1:
            print(f'{v} e ', end='')
        else:
            print(v)
        if pos == 0:
            m = v
        elif v > m:
            m = v
    print(f'Totalizando {tam} valores ao todo.')
    print(f'O maior valor foi o {m}.')


maior(1, 2, 3, 4, 5, 16, 7, 8, 9, 0, 10)
maior(4, 7, 0)
maior(1, 99)
maior(50)
maior()
