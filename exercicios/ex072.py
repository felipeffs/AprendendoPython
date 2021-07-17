"""
Crie um programa que tenha um tupla totalmente preenchida com uma contagem
por extenso, de zero até vinte. Seu programa deverá ler um número pelo
teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

numeros = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',\
          'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
print('-' * 50)
while True:
    while True:
        pos = input('Digite um número entre 0 e 20: ')
        if pos.isdigit():
            pos = int(pos)
            if 20 >= pos >= 0:
                break
        print('Número Inválido! Tente Novamente')
    print('-' * 50)
    print(f'Você digitou o número {numeros[pos]}')
    print('-' * 50)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja repetir? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        print('-' * 50)
        break
