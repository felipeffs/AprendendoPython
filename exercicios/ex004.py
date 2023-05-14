"""
Faça um programa que leia algo pelo teclado e mostre na tela o seu
tipo primitivo e todas as informações possíveis sobre ele.
"""

ent = input('Digite qualquer coisa: ')
print('Armazenado como tipo {}'.format(type(ent)))
print('\nO que digitou é alfanumérico? {} '
      '\nÉ alfabético? {}'
      '\nÉ numérico? {}'
      '\nEstá somente em caixa baixa? {}'
      '\nEstá somente em caixa alta? {}'
      '\nEstá na tabela ascii? {}'
      '\nTem somente espaços? {}'
      '\nEstá capitalizada? {}'.format(ent.isalnum(), ent.isalpha(), ent.isnumeric(), ent.islower(), ent.isupper(),
                                       ent.isascii(), ent.isspace(), ent.istitle()))
