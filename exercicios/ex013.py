"""
Faça um algoritmo que leia o salário de um funcionário e mostre seu
novo salário, com 15% de aumento.
"""

salario = float(input('Salário atual do funcionário: R$'))
salario = salario * 1.15
print('Salário do funcionário com 15% de aumento: R${:.2f}'.format(salario))
