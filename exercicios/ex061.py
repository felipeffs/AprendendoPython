"""
Refaça o Exercício 051, lendo o primeiro termo e a razão de uma PA, mostrando
os 10 primeiros termos da progressão usando a estrutura while.
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
