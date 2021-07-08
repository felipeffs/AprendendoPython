from random import choice

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

listaA = [n1, n2, n3, n4]

c = choice(listaA)

print('O aluno(a) escolhido foi {} '.format(c))
