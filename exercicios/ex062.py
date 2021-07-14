"""
Melhore o Exercício 061, perguntando para o usuário se ele quer mostrar
mais alguns termos. O programa encerra quando ele disser que quer mostrar
0 termos.
"""

ptermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão: '))
c = 0
termo = 0
print('PA: ', end='')
while c != 10:
    termo = ptermo + c * razao
    print(termo, end=' ')
    c += 1
t = 1
while t != 0:
    c = 0

    while c != t:
        termo += razao
        print(termo, end=' ')
        c += 1
