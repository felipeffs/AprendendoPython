"""
Desenvolva um programa que leia as duas notas de um aluno,
calcule e mostre a sua média.
"""

nota1 = float(input('Insira a nota da primeira prova do Aluno: '))
nota2 = float(input('Insira a nota da segunda prova do Aluno: '))
media = (nota1+nota2)/2
print('A média de Aluno é {:.2f}'.format(media))
