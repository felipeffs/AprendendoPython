# 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome da cidade: ')).strip()
cidDiv = cidade.split()

print('A cidade informada começa com "Santo"? {}'.format(cidDiv[0].lower() == 'santo'))
