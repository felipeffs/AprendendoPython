"""
Crie um programa que leia dois valores e mostre um menu como o abaixo:
[1] somar
[2] multiplicar
[3] novos números
[4] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""

op = 1
while op != 4:
    op = int(input('>Menu Principal:'
                   '\n    [1] somar'
                   '\n    [2] multiplicar'
                   '\n    [3] maior'
                   '\n    [4] sair\n'))
    if op == 1:
        print('>Somar')
        n = float(input('   Digite o primeiro número: '))
        n2 = float(input('   Digite o segundo número: '))
        r = n + n2
        print('   Resultado: {}\n'.format(r))
    elif op == 2:
        print('>Multiplicar')
        n = float(input('   Digite o primeiro número: '))
        n2 = float(input('   Digite o segundo número: '))
        r = n * n2
        print('   Resultado: {}\n'.format(r))
    elif op == 3:
        print('>Maior')
        n = float(input('   Digite o primeiro número: '))
        n2 = float(input('   Digite o segundo número: '))
        r = n if n > n2 else n2
        print('   Resultado: {}\n'.format(r))
    elif op == 4:
        print()
    else:
        print("Opção Inválida!\n")
