"""
Refaça o Exercício 051, lendo o primeiro termo e a razão de uma PA, mostrando
os 10 primeiros termos da progressão usando a estrutura while.
"""

ptermo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão: '))
c = 1
termo = ptermo
print('PA: ', end='')
while c <= 10:
    print(termo, end=' ')
    termo += razao
    c += 1
