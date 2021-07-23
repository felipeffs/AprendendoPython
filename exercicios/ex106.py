"""
Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar
o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o
programa se encerrará.
OBS: use cores.
"""


def titulo(texto, letra=int(), fundo=int(), estilo=int()):
    tam = len(texto) + 4
    cor = f'\033[{estilo}:{letra}:{fundo}m'
    print(f'{cor}', end='')
    print(f'~'*tam)
    print(f'  ' + texto.title().strip() + '  ')
    print(f'~'*tam)
    print('\033[m', end='')


def ajuda():
    from time import sleep
    while True:
        titulo('SISTEMA DE AJUDA PyHELP', 97, 44, 1)
        duvida = str(input('Função ou Biblioteca >> ')).strip()
        duvida = duvida.replace('()', '')
        if duvida.lower() == 'fim':
            break
        titulo(f"Acessando o manual do comando '{duvida}'", 97, 46, 1)
        sleep(0.5)
        print('\033[:30:107m', end='')
        help(duvida)
        print('\033[m', end='')
        sleep(2)
    titulo('Até Logo', 30, 45)


ajuda()
