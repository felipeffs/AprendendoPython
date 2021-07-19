"""
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer
como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex:
escreva('Olá, Mundo!)
Saída:
~~~~~~~~~~~~~
 Olá, Mundo!
~~~~~~~~~~~~~
"""


def escreva(texto):
    tam = len(texto) + 4
    print('~'*tam)
    print('  ' + texto.title().strip() + '  ')
    print('~'*tam)


escreva(str(input('Digite uma frase: ')))
