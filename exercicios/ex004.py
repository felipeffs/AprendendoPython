
ent = input('Digite qualquer coisa: ')
print('Armazenado como tipo {}'.format(type(ent)))
print('\nO que digitou é Alfanumérico? {} \nÉ Alfabético? {}\nÉ Numérico? {}\nEstá somente em caixa baixa? {}\nEstá somente em caixa alta? {}\nEstá na tabela ascii? {}\nTem somente espaços? {}\nEstá Capitalizada? {}'.format(ent.isalnum(), ent.isalpha(), ent.isnumeric(), ent.islower(), ent.isupper(), ent.isascii(), ent.isspace(), ent.istitle()))
