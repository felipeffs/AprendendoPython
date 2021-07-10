"""
Escreva um programa que pergunte o salário de um funcionário e
calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, Calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
"""

s = float(input('Salário do funcionário: R$'))

if s > 1250:
    s = s * 1.1
else:
    s = s * 1.15

print('O novo salário é {:.2f}'.format(s))
