print('\033[7;31;107mOlá, Mundo!\033[m')
print('\033[1;36;107mAtende logo!\033[m')

a = 7
b = 89

print('Os valores são \033[7;35m{}\033[m e \033[4;34m{}\033[m'.format(a, b))

nome = 'Helena'

print('Olá! Muito prazer em te conhecer, {}{}{}!'.format('\033[4;32m', nome, '\033[m'))

# dicionário
cores = {'limpa': '\033[m',
         'verde sublinhado': '\033[4;32m'}

# método colorize pesquisar
