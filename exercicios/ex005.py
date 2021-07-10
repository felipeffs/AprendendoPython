"""
Faça um programa que leia um número inteiro e mostre na tela o seu
sucessor e seu antecessor.
"""

e = int(input('>>>>>>>>>>Visualizador de Números Vizinhos<<<<<<<<<<'
              '\nDigite um Número: '))
print('O Antecessor de {} é {} e o Sucessor é {}'.format(e, e-1, e+1))
