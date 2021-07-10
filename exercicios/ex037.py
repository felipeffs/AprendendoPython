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
    print('\033[31mescolha inválida\033[31m')
    exit()
print('O resultado é {}'.format(nc[2:]))
