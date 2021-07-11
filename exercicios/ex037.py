"""
Escreva um programa que leia um número inteiro qualquer e peça
para o usuário escolher qual será a base de conversão:
— 1 para binário
— 2 para octal
— 3 para hexadecimal
"""

n = int(input('Digite um número inteiro na base 10: '))

e = int(input('> Pra qual base deseja converter? \n1- Binário 2- Octal 3- hexadecimal '))

nc = 0
if e == 1:
    nc = bin(n)
elif e == 2:
    nc = oct(n)
elif e == 3:
    nc = hex(n)
else:
    print('\033[31mEscolha inválida\033[31m')
    exit()
print('O resultado é {}'.format(nc[2:]))
