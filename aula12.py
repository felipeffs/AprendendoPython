nome = str(input('Qual é o seu nome? ')).strip().lower()

if nome == 'gustavo':
    print('Que nome bonito!')
elif nome == 'pedro' or nome == 'maria' or nome == 'paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'ana cláudia jéssica juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome.capitalize()))
