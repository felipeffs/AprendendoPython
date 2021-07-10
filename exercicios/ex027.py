"""
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza
primeiro = Ana
último = Souza
"""

nc = str(input('Nome completo: ')).strip()
nc = nc.split()
ultNomePos = len(nc) - 1

print('Primeiro nome: {} '
      '\nUltimo nome: {}'.format(nc[0], nc[ultNomePos]))
