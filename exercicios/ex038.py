"""
Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:
— O primeiro valor é maior
— O segundo valor é maior
— Não existe valor maior, os dois são iguais
"""

n1 = int(input('\033[7;30;107m>>Comparador de números<<\033[m\n'
               'Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print('O \033[35m primeiro valor \033[m é \033[34m maior \033[m')
elif n1 == n2:
    print('\033[35mNão existe\033[m valor maior, os dois são \033[34m iguais \033[m')
else:
    print('O \033[35m segundo valor \033[m é \033[34m maior \033[m')
